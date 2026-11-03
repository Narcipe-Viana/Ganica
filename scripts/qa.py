#!/usr/bin/env python3
"""Checagens automáticas do site da Ganica.

Roda sobre o site já gerado em _site/ (rode `npx @11ty/eleventy` antes).
Se qualquer checagem falhar, o script sai com código 1 e NADA deve ser publicado.

Uso:
  python3 scripts/qa.py                  # tudo, inclusive navegador (mobile 390px e desktop 1280px)
  python3 scripts/qa.py --sem-navegador  # só checagens de estrutura (usado no GitHub Actions)
  python3 scripts/qa.py --artigo SLUG    # mesmas checagens, com relatório focado num artigo
"""
import hashlib
import html
import json
import re
import sys
import unicodedata
from html.parser import HTMLParser
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SITE = RAIZ / "_site"
ARTIGOS_SRC = RAIZ / "src" / "artigos"
BLOQUEIO = RAIZ / "editorial" / "bloqueio.sha256"
URL_BASE = "https://ganica.com.br"

erros, avisos = [], []


def erro(pagina, msg):
    erros.append(f"[ERRO] {pagina}: {msg}")


def aviso(pagina, msg):
    avisos.append(f"[aviso] {pagina}: {msg}")


class Extrator(HTMLParser):
    """Separa texto visível, links, ids, h1 e blocos JSON-LD."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.texto, self.links, self.ids, self.h1, self.jsonld = [], [], set(), [], []
        self.imgs, self.title, self.meta = [], [], {}
        self._em_title = False
        self._pilha_ignorar = 0
        self._em_jsonld = False
        self._em_h1 = False
        self._buf = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            self.ids.add(a["id"])
        if tag == "a" and a.get("href"):
            self.links.append(a["href"])
        if tag == "img":
            self.imgs.append(a)
        if tag == "meta" and a.get("name"):
            self.meta[a["name"]] = a.get("content", "")
        if tag == "link" and a.get("rel") == "canonical":
            self.meta["canonical"] = a.get("href", "")
        if tag == "title":
            self._em_title = True
        if tag == "script" and a.get("type") == "application/ld+json":
            self._em_jsonld, self._buf = True, []
        elif tag in ("script", "style", "noscript"):
            self._pilha_ignorar += 1
        if tag == "h1":
            self._em_h1, self._h1buf = True, []

    def handle_endtag(self, tag):
        if tag == "script" and self._em_jsonld:
            self.jsonld.append("".join(self._buf))
            self._em_jsonld = False
        elif tag in ("script", "style", "noscript") and self._pilha_ignorar:
            self._pilha_ignorar -= 1
        if tag == "h1" and self._em_h1:
            self.h1.append(" ".join("".join(self._h1buf).split()))
            self._em_h1 = False

    def handle_data(self, data):
        if self._em_title:
            self.title.append(data)
            self._em_title = False
            return
        if self._em_jsonld:
            self._buf.append(data)
            return
        if self._pilha_ignorar:
            return
        self.texto.append(data)
        if self._em_h1:
            self._h1buf.append(data)


def normalizar(s):
    s = unicodedata.normalize("NFKD", s.lower())
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.findall(r"[a-z0-9]+", s)


def carregar_bloqueio():
    if not BLOQUEIO.exists():
        return set()
    return {l.strip() for l in BLOQUEIO.read_text().splitlines() if l.strip() and not l.startswith("#")}


def termos_bloqueados(texto, hashes):
    """Compara 1 a 3 palavras seguidas, via hash: a lista de nomes protegidos
    (clientes, agência parceira) nunca fica legível neste repositório público."""
    if not hashes:
        return 0
    palavras = normalizar(texto)
    achados = 0
    for n in (1, 2, 3):
        for i in range(len(palavras) - n + 1):
            termo = " ".join(palavras[i:i + n])
            if hashlib.sha256(termo.encode()).hexdigest() in hashes:
                achados += 1
    return achados


def frontmatter(md_path):
    import yaml  # PyYAML
    txt = md_path.read_text(encoding="utf-8")
    partes = txt.split("---", 2)
    return yaml.safe_load(partes[1]) or {}, partes[2]


def checar_estrutura(foco=None):
    hashes = carregar_bloqueio()
    if not SITE.exists():
        erro("_site", "site não foi gerado; rode `npx @11ty/eleventy` antes")
        return
    paginas = sorted(SITE.rglob("*.html"))
    ids_por_pagina = {}
    extraidos = {}
    for p in paginas:
        ex = Extrator()
        ex.feed(p.read_text(encoding="utf-8"))
        rel = "/" + str(p.relative_to(SITE)).replace("index.html", "")
        extraidos[rel] = ex
        ids_por_pagina[rel] = ex.ids

    for arq in ("feed.xml", "llms.txt", "robots.txt", "logo-ganica.png", "favicon-48.png", "apple-touch-icon.png"):
        if not (SITE / arq).exists():
            erro(arq, "não foi gerado")
    sitemap = (SITE / "sitemap.xml").read_text(encoding="utf-8") if (SITE / "sitemap.xml").exists() else ""
    if not sitemap:
        erro("sitemap.xml", "não existe")

    artigos_publicados = {}
    for md in sorted(ARTIGOS_SRC.glob("*.md")):
        fm, corpo = frontmatter(md)
        if not fm.get("rascunho"):
            artigos_publicados[f"/{fm.get('slug')}.html"] = (fm, corpo, md.name)

    for rel, ex in extraidos.items():
        texto = html.unescape(" ".join(ex.texto))
        pg = rel

        # 1. Travessão proibido no texto visível
        n = texto.count("—")
        if n:
            trecho = texto[max(0, texto.find("—") - 60): texto.find("—") + 40].strip()
            erro(pg, f"{n} travessão(ões) no texto visível. Ex.: \"…{trecho}…\"")

        # 2. Exatamente um H1
        if len(ex.h1) != 1:
            erro(pg, f"esperado 1 H1, encontrados {len(ex.h1)}")

        # 2b. SEO básico de toda página
        if not ex.title or not 20 <= len(ex.title[0].strip()) <= 70:
            aviso(pg, f"title ausente ou fora de 20 a 70 caracteres: {ex.title[:1]}")
        desc_pg = ex.meta.get("description", "")
        if not desc_pg:
            erro(pg, "sem meta description")
        if not ex.meta.get("canonical", "").startswith(URL_BASE):
            erro(pg, "sem canonical absoluto")
        for img in ex.imgs:
            if img.get("alt") in (None, ""):
                erro(pg, f"imagem sem alt: {img.get('src')}")
            if not img.get("width") or not img.get("height"):
                erro(pg, f"imagem sem width/height (causa CLS): {img.get('src')}")

        # 3. JSON-LD válido
        for bloco in ex.jsonld:
            try:
                json.loads(bloco)
            except json.JSONDecodeError as e:
                erro(pg, f"JSON-LD inválido: {e}")

        # 4. Links internos apontam para páginas e âncoras que existem
        for href in ex.links:
            if not href.startswith("/") or href.startswith("//"):
                continue
            caminho, _, ancora = href.partition("#")
            caminho = caminho or "/"
            alvo = SITE / caminho.lstrip("/")
            if caminho.endswith("/"):
                alvo = alvo / "index.html"
            if not alvo.exists():
                erro(pg, f"link interno quebrado: {href}")
            elif ancora and ancora not in ids_por_pagina.get(caminho, set()):
                erro(pg, f"âncora inexistente: {href}")

        # 5. Nomes protegidos (clientes, parceiros)
        achados = termos_bloqueados(texto, hashes)
        if achados:
            erro(pg, f"{achados} ocorrência(s) de nome protegido (cliente/parceiro). Anonimize antes de publicar.")

    # 6. Regras específicas de artigo
    for url, (fm, corpo, nome) in artigos_publicados.items():
        if foco and fm.get("slug") != foco:
            continue
        ex = extraidos.get(url)
        if ex is None:
            erro(url, f"artigo {nome} não foi gerado")
            continue
        if url not in sitemap:
            erro(url, "ausente do sitemap.xml")
        desc = fm.get("description") or ""
        if not 70 <= len(desc) <= 230:
            aviso(url, f"meta description com {len(desc)} caracteres (ideal 120 a 160)")
        if len(fm.get("seo_title") or fm.get("title") or "") > 70:
            aviso(url, "título SEO acima de 70 caracteres (pode ser cortado no Google)")
        for campo in ("title", "slug", "date", "description", "deck", "breadcrumb", "fontes", "card_kicker", "card_resumo"):
            if not fm.get(campo):
                erro(url, f"campo obrigatório vazio: {campo}")
        if not fm.get("resumo") or len(fm["resumo"]) < 3:
            erro(url, "resumo rápido precisa de pelo menos 3 itens")
        if fm.get("usa_dado_cliente"):
            texto_total = corpo + " " + json.dumps(fm, ensure_ascii=False, default=str)
            decimais = re.findall(r"\d+,\d+\s?%|\d+\.\d+\s?%", texto_total)
            reais = re.findall(r"R\$\s?\d", texto_total)
            if decimais:
                erro(url, f"estudo com dado de cliente tem percentual com casas decimais: {decimais[:3]}. Use número arredondado ou relativo.")
            if reais:
                erro(url, "estudo com dado de cliente tem valor em reais. Use exemplo hipotético declarado ou número relativo.")
        og = fm.get("imagem_og") or f"/assets/og/{fm.get('slug')}.png"
        if not (SITE / og.lstrip("/")).exists():
            erro(url, f"imagem de compartilhamento não existe: {og} (rode python3 scripts/og.py)")
        data_pub = str(fm.get("date") or "")
        rc = fm.get("resposta_curta") or ""
        if data_pub >= "2026-11-01" or rc:
            n_rc = len(re.findall(r"\w+", rc))
            if not 35 <= n_rc <= 80:
                erro(url, f"resposta_curta com {n_rc} palavras; precisa de 40 a 70 (resposta direta ao título, citável por IA)")
            if data_pub >= "2026-11-01" and not fm.get("fontes_urls"):
                erro(url, "fontes_urls vazio: liste os links das fontes primárias citadas")
        else:
            aviso(url, "sem resposta_curta (bloco de resposta direta, importante para GEO)")
        palavras = len(re.findall(r"\w+", re.sub(r"<[^>]+>", " ", corpo)))
        if palavras < 900:
            erro(url, f"corpo com {palavras} palavras; mínimo 900 para um estudo")
        if corpo.count("\n## ") < 4:
            erro(url, "corpo precisa de pelo menos 4 seções (##)")
        links_internos = [l for l in re.findall(r"\]\((/[^)]*)\)|href=\"(/[^\"]*)\"", corpo)]
        if not links_internos:
            erro(url, "corpo sem nenhum link interno (diagnóstico, outro estudo)")
        headline = None
        for bloco in ex.jsonld:
            try:
                for item in json.loads(bloco).get("@graph", []):
                    if item.get("@type") == "BlogPosting":
                        headline = item.get("headline")
            except Exception:
                pass
        if headline and ex.h1 and " ".join(headline.split()) != ex.h1[0]:
            erro(url, "headline do schema diferente do H1")

    # 7. Slugs únicos
    slugs = [fm.get("slug") for fm, _, _ in artigos_publicados.values()]
    if len(slugs) != len(set(slugs)):
        erro("artigos", "há slugs repetidos")


def checar_navegador(foco=None):
    import asyncio
    import functools
    import http.server
    import threading

    from playwright.async_api import async_playwright

    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(SITE))
    http.server.SimpleHTTPRequestHandler.log_message = lambda *a: None
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
    porta = srv.server_address[1]
    threading.Thread(target=srv.serve_forever, daemon=True).start()

    paginas = ["/", "/estudos/"] + [
        "/" + p.name for p in sorted(SITE.glob("*.html")) if p.name != "index.html"
    ]
    if foco:
        paginas = ["/", "/estudos/", f"/{foco}.html"]
    pasta = RAIZ / ".qa"
    pasta.mkdir(exist_ok=True)

    async def rodar():
        async with async_playwright() as p:
            nav = await p.chromium.launch()
            for largura in (390, 1280):
                ctx = await nav.new_context(viewport={"width": largura, "height": 900})
                pg = await ctx.new_page()
                erros_js = []
                pg.on("pageerror", lambda e: erros_js.append(str(e)))
                for caminho in paginas:
                    erros_js.clear()
                    await pg.goto(f"http://127.0.0.1:{porta}{caminho}", wait_until="load")
                    # sem animação de rolagem (o site usa scroll-behavior:smooth)
                    await pg.evaluate("document.documentElement.style.scrollBehavior='auto'")
                    excesso = await pg.evaluate("document.documentElement.scrollWidth - window.innerWidth")
                    if excesso > 0:
                        erro(caminho, f"rolagem horizontal de {excesso}px em {largura}px de largura")
                    largos = await pg.evaluate("""[...document.querySelectorAll('.prose *')]
                        .filter(e => !e.closest('.data-table-wrap') && e.getBoundingClientRect().right > window.innerWidth + 1)
                        .slice(0, 3).map(e => e.tagName + ' ' + (e.textContent || '').trim().slice(0, 40))""")
                    for l in largos:
                        erro(caminho, f"elemento vaza da tela em {largura}px: {l}")
                    imgs = await pg.evaluate("""(async () => {
                        const r = [];
                        for (const i of document.images) { i.loading = 'eager'; }
                        await new Promise(res => setTimeout(res, 400));
                        for (const i of document.images) { if (!i.complete || i.naturalWidth === 0) r.push(i.getAttribute('src')); }
                        return r; })()""")
                    for i in imgs:
                        erro(caminho, f"imagem não carregou: {i}")
                    for e in erros_js:
                        erro(caminho, f"erro de JavaScript ({largura}px): {e}")
                    nome = (caminho.strip("/").replace("/", "_").replace(".html", "") or "home")
                    await pg.screenshot(path=str(pasta / f"{nome}-{largura}.png"), full_page=True)
                await ctx.close()
            await nav.close()

    asyncio.run(rodar())
    srv.shutdown()


def main():
    args = sys.argv[1:]
    foco = args[args.index("--artigo") + 1] if "--artigo" in args else None
    checar_estrutura(foco)
    if "--sem-navegador" not in args:
        checar_navegador(foco)
    for a in avisos:
        print(a)
    for e in erros:
        print(e)
    if erros:
        print(f"\nREPROVADO: {len(erros)} erro(s). Não publique.")
        sys.exit(1)
    print(f"\nAPROVADO ({len(avisos)} aviso(s)). Capturas em .qa/")


if __name__ == "__main__":
    main()
