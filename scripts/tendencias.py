#!/usr/bin/env python3
"""Coleta tendências do Google Trends (Brasil) para a pauta dos estudos da Ganica.

Roda no GitHub Actions (todo dia de manhã) e grava:
  editorial/tendencias.json  -> dados brutos para a automação editorial
  editorial/TENDENCIAS.md    -> resumo legível para humanos

Fontes (todas públicas, do próprio Google Trends):
  1. Pesquisas em alta do dia no Brasil (RSS oficial do Trends), com notícias relacionadas.
  2. Consultas relacionadas "em ascensão" e "principais" de termos-semente de e-commerce e
     marketplace, e da categoria Compras, nos últimos 90 dias (endpoints públicos do Explore).
  3. Calendário do varejo brasileiro (datas calculadas aqui), com as próximas datas.

Importante sobre os números do Trends: são índices relativos (0 a 100) e variações percentuais,
NUNCA volume de buscas. "Breakout" = alta acima de 5.000%.
Google às vezes recusa (HTTP 429); o script tenta de novo com espera e registra o que falhou,
sem quebrar. Uso: python3 scripts/tendencias.py
"""
import datetime as dt
import json
import random
import time
import urllib.parse
import xml.etree.ElementTree as ET
from pathlib import Path

import requests

RAIZ = Path(__file__).resolve().parent.parent
SAIDA_JSON = RAIZ / "editorial" / "tendencias.json"
SAIDA_MD = RAIZ / "editorial" / "TENDENCIAS.md"

GEO = "BR"
JANELA = "today 3-m"
HL = "pt-BR"
TZ = 180  # minutos de diferença para UTC (Brasília)

# Termos-semente: o que um decisor de e-commerce e marketplace pesquisa.
SEMENTES = [
    "e-commerce", "loja virtual", "marketplace", "mercado livre", "shopee", "amazon",
    "frete grátis", "pix", "cupom de desconto", "black friday", "checkout",
    "taxa de conversão", "tiktok shop", "vender online",
]
CATEGORIA_COMPRAS = 18  # categoria "Compras" do Google Trends

# Palavras que tornam uma pesquisa em alta do dia relevante para comércio online.
RELEVANTES = [
    "black friday", "cyber", "promo", "desconto", "cupom", "frete", "pix", "compra", "compras",
    "loja", "mercado livre", "shopee", "amazon", "magalu", "magazine luiza", "americanas",
    "casas bahia", "aliexpress", "shein", "temu", "tiktok shop", "kabum", "netshoes",
    "e-commerce", "ecommerce", "marketplace", "entrega", "correios", "taxa", "importação",
    "remessa", "procon", "reembolso", "golpe", "boleto", "cartão", "parcelamento", "natal",
    "dia das mães", "dia dos pais", "dia dos namorados", "dia das crianças", "consumidor",
    "preço", "oferta", "liquidação", "app", "varejo",
]

SESSAO = requests.Session()
SESSAO.headers.update({
    "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                   "(KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"),
    "Accept-Language": "pt-BR,pt;q=0.9,en;q=0.8",
})
erros = []


def pegar(url, tentativas=4, **kw):
    for i in range(tentativas):
        try:
            r = SESSAO.get(url, timeout=30, **kw)
            if r.status_code == 200:
                return r
            if r.status_code in (429, 500, 502, 503):
                espera = 8 * (i + 1) + random.uniform(0, 5)
                time.sleep(espera)
                continue
            erros.append(f"{r.status_code} em {url[:90]}")
            return None
        except requests.RequestException as e:
            time.sleep(5)
            ultimo = str(e)
    erros.append(f"falhou após {tentativas} tentativas: {url[:90]}")
    return None


def json_google(texto):
    # As respostas do Trends começam com um prefixo anti-JSON-hijacking: )]}' ou )]}',
    return json.loads(texto[texto.index("{"):])


# ---------------------------------------------------------------- 1. em alta hoje
def em_alta_hoje():
    r = pegar(f"https://trends.google.com/trending/rss?geo={GEO}")
    if not r:
        return []
    ns = {"ht": "https://trends.google.com/trending/rss"}
    itens = []
    for item in ET.fromstring(r.content).iter("item"):
        titulo = (item.findtext("title") or "").strip()
        noticias = [{
            "titulo": (n.findtext("ht:news_item_title", namespaces=ns) or "").strip(),
            "url": (n.findtext("ht:news_item_url", namespaces=ns) or "").strip(),
            "fonte": (n.findtext("ht:news_item_source", namespaces=ns) or "").strip(),
        } for n in item.findall("ht:news_item", ns)]
        texto = (titulo + " " + " ".join(n["titulo"] for n in noticias)).lower()
        itens.append({
            "pesquisa": titulo,
            "trafego_aprox": (item.findtext("ht:approx_traffic", namespaces=ns) or "").strip(),
            "publicado": (item.findtext("pubDate") or "").strip(),
            "relevante_ecommerce": any(p in texto for p in RELEVANTES),
            "noticias": noticias[:3],
        })
    return itens


# ---------------------------------------------------------------- 2. explore
def aquecer():
    # O Google define o cookie de sessão mesmo quando responde 429.
    try:
        SESSAO.get(f"https://trends.google.com/trends/explore?geo={GEO}&hl={HL}", timeout=30)
    except requests.RequestException:
        pass
    time.sleep(2)


def relacionadas(termo=None, categoria=0):
    item = {"keyword": termo or "", "geo": GEO, "time": JANELA}
    req = {"comparisonItem": [item], "category": categoria, "property": ""}
    url = ("https://trends.google.com/trends/api/explore?hl=%s&tz=%d&req=%s"
           % (HL, TZ, urllib.parse.quote(json.dumps(req, separators=(",", ":")))))
    r = pegar(url)
    if not r:
        return None
    try:
        widgets = json_google(r.text)["widgets"]
    except (ValueError, KeyError):
        erros.append(f"resposta inesperada do explore para {termo or categoria}")
        return None
    resultado = {}
    for w in widgets:
        if w.get("id") not in ("RELATED_QUERIES", "TIMESERIES"):
            continue
        tipo = "relatedsearches" if w["id"] == "RELATED_QUERIES" else "multiline"
        u = ("https://trends.google.com/trends/api/widgetdata/%s?hl=%s&tz=%d&req=%s&token=%s"
             % (tipo, HL, TZ, urllib.parse.quote(json.dumps(w["request"], separators=(",", ":"))),
                w["token"]))
        time.sleep(1.5 + random.uniform(0, 1.5))
        rr = pegar(u)
        if not rr:
            continue
        try:
            dados = json_google(rr.text)["default"]
        except (ValueError, KeyError):
            continue
        if tipo == "relatedsearches":
            listas = dados.get("rankedList", [])

            def conv(lst):
                return [{"consulta": k["query"], "valor": k.get("formattedValue", "")}
                        for k in lst.get("rankedKeyword", [])][:15]
            resultado["principais"] = conv(listas[0]) if len(listas) > 0 else []
            resultado["em_ascensao"] = conv(listas[1]) if len(listas) > 1 else []
        else:
            pontos = [p["value"][0] for p in dados.get("timelineData", []) if p.get("value")]
            if len(pontos) >= 8:
                ini = sum(pontos[:4]) / 4 or 1
                fim = sum(pontos[-4:]) / 4
                resultado["variacao_90d_pct"] = round(100 * (fim - ini) / ini)
                resultado["indice_atual"] = pontos[-1]
    resultado["link"] = ("https://trends.google.com/trends/explore?" + urllib.parse.urlencode(
        {k: v for k, v in {"date": JANELA, "geo": GEO, "q": termo or None,
                           "cat": categoria or None, "hl": HL}.items() if v}))
    return resultado


# ---------------------------------------------------------------- 3. calendário
def nesimo_dia(ano, mes, dia_semana, n):
    d = dt.date(ano, mes, 1)
    while d.weekday() != dia_semana:
        d += dt.timedelta(days=1)
    return d + dt.timedelta(weeks=n - 1)


def calendario(hoje):
    datas = []
    for ano in (hoje.year, hoje.year + 1):
        bf = nesimo_dia(ano, 11, 3, 4) + dt.timedelta(days=1)  # dia seguinte à 4ª quinta de novembro
        datas += [
            ("Dia do Consumidor", dt.date(ano, 3, 15)),
            ("Dia das Mães", nesimo_dia(ano, 5, 6, 2)),
            ("Dia dos Namorados", dt.date(ano, 6, 12)),
            ("Dia dos Pais", nesimo_dia(ano, 8, 6, 2)),
            ("Dia do Cliente", dt.date(ano, 9, 15)),
            ("Dia das Crianças", dt.date(ano, 10, 12)),
            ("11.11", dt.date(ano, 11, 11)),
            ("Black Friday", bf),
            ("Cyber Monday", bf + dt.timedelta(days=3)),
            ("Natal", dt.date(ano, 12, 25)),
        ]
    prox = sorted((d, n) for n, d in datas if 0 <= (d - hoje).days <= 75)
    return [{"data": d.isoformat(), "evento": n, "dias_ate": (d - hoje).days} for d, n in prox]


def main():
    hoje = dt.datetime.now(dt.timezone(dt.timedelta(hours=-3))).date()
    saida = {
        "gerado_em": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
        "geo": GEO, "janela_explore": "últimos 90 dias",
        "aviso": "Índices do Google Trends são relativos (0 a 100) e variações percentuais; não são volume de buscas.",
        "calendario_proximo": calendario(hoje),
        "em_alta_hoje": em_alta_hoje(),
        "categoria_compras": None,
        "sementes": {},
        "erros": erros,
    }
    aquecer()
    saida["categoria_compras"] = relacionadas(categoria=CATEGORIA_COMPRAS)
    for termo in SEMENTES:
        time.sleep(4 + random.uniform(0, 4))
        saida["sementes"][termo] = relacionadas(termo)

    SAIDA_JSON.write_text(json.dumps(saida, ensure_ascii=False, indent=1), encoding="utf-8")
    SAIDA_MD.write_text(resumo_md(saida), encoding="utf-8")
    ok = sum(1 for v in saida["sementes"].values() if v)
    print(f"em alta hoje: {len(saida['em_alta_hoje'])} itens "
          f"({sum(i['relevante_ecommerce'] for i in saida['em_alta_hoje'])} relevantes); "
          f"sementes com dados: {ok}/{len(SEMENTES)}; categoria Compras: {'ok' if saida['categoria_compras'] else 'falhou'}; "
          f"erros: {len(erros)}")


def resumo_md(s):
    l = [f"# Tendências (Google Trends, Brasil)", "",
         f"Gerado em {s['gerado_em']} pelo GitHub Actions. {s['aviso']}", ""]
    l += ["## Próximas datas do varejo", ""]
    l += [f"- {c['data']}: {c['evento']} (em {c['dias_ate']} dias)" for c in s["calendario_proximo"]] or ["- nenhuma nos próximos 75 dias"]
    rel = [i for i in s["em_alta_hoje"] if i["relevante_ecommerce"]]
    l += ["", "## Em alta hoje com ligação a comércio online", ""]
    l += [f"- {i['pesquisa']} ({i['trafego_aprox']}): " + "; ".join(n["titulo"] for n in i["noticias"][:2]) for i in rel] or ["- nenhuma hoje"]
    cc = s.get("categoria_compras") or {}
    l += ["", "## Categoria Compras: consultas em ascensão (90 dias)", ""]
    l += [f"- {q['consulta']} ({q['valor']})" for q in cc.get("em_ascensao", [])] or ["- sem dados"]
    l += ["", "## Termos de e-commerce e marketplace", ""]
    for termo, d in s["sementes"].items():
        if not d:
            l.append(f"- **{termo}**: sem dados nesta coleta")
            continue
        var = d.get("variacao_90d_pct")
        asc = ", ".join(f"{q['consulta']} ({q['valor']})" for q in d.get("em_ascensao", [])[:6]) or "nenhuma"
        l.append(f"- **{termo}**" + (f" (variação 90 dias: {var:+d}%)" if var is not None else "") + f": em ascensão: {asc}")
    if s["erros"]:
        l += ["", "## Falhas desta coleta", ""] + [f"- {e}" for e in s["erros"][:15]]
    return "\n".join(l) + "\n"


if __name__ == "__main__":
    main()
