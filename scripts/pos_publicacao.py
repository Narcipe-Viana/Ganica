#!/usr/bin/env python3
"""Depois de cada publicação (roda no GitHub Actions):

1. Espera o sitemap NO AR (https://ganica.com.br/sitemap.xml) refletir a versão recém-publicada
   e confere que todo endereço do sitemap gerado está no sitemap do ar. Se não estiver depois de
   ~6 minutos, falha (o GitHub avisa por e-mail).
2. Avisa os buscadores que usam IndexNow (Bing, que alimenta o ChatGPT Search e o Copilot, Yandex,
   Seznam, Naver) sobre os endereços novos ou alterados desde a publicação anterior.
   O Google não usa IndexNow: para ele, vale o sitemap no Search Console e no robots.txt.

Uso: python3 scripts/pos_publicacao.py <sitemap_anterior.xml> <sitemap_novo.xml>
"""
import json
import sys
import time
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
HOST = "ganica.com.br"
NS = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}


def ler(conteudo):
    try:
        raiz = ET.fromstring(conteudo)
    except ET.ParseError:
        return {}
    return {(u.findtext("s:loc", namespaces=NS) or "").strip(): (u.findtext("s:lastmod", namespaces=NS) or "").strip()
            for u in raiz.findall("s:url", NS)}


def baixar(url):
    req = urllib.request.Request(url + f"?v={int(time.time())}", headers={"User-Agent": "ganica-publicacao/1.0", "Cache-Control": "no-cache"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()


def main():
    anterior = ler(Path(sys.argv[1]).read_bytes()) if Path(sys.argv[1]).exists() and Path(sys.argv[1]).stat().st_size else {}
    novo = ler(Path(sys.argv[2]).read_bytes())
    if not novo:
        sys.exit("sitemap novo inválido")

    # 1. Conferir o sitemap no ar
    no_ar = {}
    for tentativa in range(80):  # até ~20 minutos (o deploy do GitHub Pages às vezes passa de 8 minutos)
        try:
            no_ar = ler(baixar(f"https://{HOST}/sitemap.xml"))
        except Exception as e:
            print(f"tentativa {tentativa + 1}: {e}")
        if no_ar and all(no_ar.get(loc) == lm for loc, lm in novo.items()):
            break
        time.sleep(15)
    faltando = [loc for loc, lm in novo.items() if no_ar.get(loc) != lm]
    if faltando:
        print("ERRO: sitemap no ar não reflete a publicação. Diferenças:")
        for loc in faltando:
            print("  -", loc, "| no ar:", no_ar.get(loc), "| esperado:", novo[loc])
        sys.exit(1)
    print(f"Sitemap no ar confere: {len(novo)} endereços.")

    # 2. IndexNow: só o que é novo ou mudou
    mudou = [loc for loc, lm in novo.items() if anterior.get(loc) != lm]
    if not mudou:
        print("Nada novo para avisar aos buscadores.")
        return
    chaves = [p for p in (RAIZ / "src").glob("*.txt") if len(p.stem) == 32]
    if not chaves:
        print("Sem chave IndexNow; aviso não enviado.")
        return
    chave = chaves[0].read_text().strip()
    corpo = json.dumps({"host": HOST, "key": chave, "keyLocation": f"https://{HOST}/{chave}.txt",
                        "urlList": mudou}).encode()
    req = urllib.request.Request("https://api.indexnow.org/indexnow", data=corpo,
                                 headers={"Content-Type": "application/json; charset=utf-8"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            print(f"IndexNow: HTTP {r.status} para {len(mudou)} endereço(s):")
    except urllib.error.HTTPError as e:
        # 202 = aceito, aguardando validação da chave; 4xx não deve derrubar a publicação
        print(f"IndexNow respondeu HTTP {e.code} para {len(mudou)} endereço(s):")
    for loc in mudou:
        print("  -", loc)


if __name__ == "__main__":
    main()
