#!/usr/bin/env python3
"""Gera as imagens de compartilhamento (Open Graph, 1200x630) e o logo do site.

- Uma imagem por estudo em src/assets/og/<slug>.png (só cria as que faltam; use --todas para refazer).
- src/assets/og/ganica.png (home), src/assets/og/estudos.png (índice) e src/assets/img/logo-ganica.png (512x512).

Usa as fontes do próprio site (pacotes @fontsource em node_modules) e o Chromium do Playwright.
Uso: python3 scripts/og.py [--todas]
"""
import asyncio
import base64
import html
import sys
from pathlib import Path

import yaml
from playwright.async_api import async_playwright

RAIZ = Path(__file__).resolve().parent.parent
OG = RAIZ / "src" / "assets" / "og"
FONTES = RAIZ / "node_modules" / "@fontsource"

def _fonte(familia, peso, arquivo):
    dados = base64.b64encode((FONTES / arquivo).read_bytes()).decode()
    return f"@font-face{{font-family:'{familia}';font-weight:{peso};src:url(data:font/woff2;base64,{dados}) format('woff2')}}"


# Fontes embutidas em base64 (página em about:blank não carrega file://)
CSS_FONTES = "".join([
    _fonte("Frank Ruhl Libre", 500, "frank-ruhl-libre/files/frank-ruhl-libre-latin-500-normal.woff2"),
    _fonte("Frank Ruhl Libre", 700, "frank-ruhl-libre/files/frank-ruhl-libre-latin-700-normal.woff2"),
    _fonte("Work Sans", 400, "work-sans/files/work-sans-latin-400-normal.woff2"),
    _fonte("Work Sans", 600, "work-sans/files/work-sans-latin-600-normal.woff2"),
])


def cartao(kicker, titulo, destaque, rodape):
    e = html.escape
    tam = 64 if len(titulo) <= 70 else 54 if len(titulo) <= 95 else 46
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS_FONTES}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1200px;height:630px;background:#161B2C;color:#F5F3EC;font-family:'Work Sans';position:relative;overflow:hidden}}
.borda{{position:absolute;inset:28px;border:1px solid rgba(245,243,236,.14)}}
.faixa{{position:absolute;left:0;top:0;bottom:0;width:10px;background:#C99A44}}
.box{{position:absolute;left:84px;right:84px;top:72px;bottom:72px;display:flex;flex-direction:column}}
.topo{{display:flex;align-items:center;gap:18px}}
.marca{{font-family:'Frank Ruhl Libre';font-weight:700;font-size:34px;color:#F5F3EC}}
.sep{{width:1px;height:26px;background:rgba(245,243,236,.25)}}
.kicker{{font-size:17px;letter-spacing:.16em;text-transform:uppercase;color:#C99A44;font-weight:600}}
h1{{font-family:'Frank Ruhl Libre';font-weight:500;font-size:{tam}px;line-height:1.08;letter-spacing:-.01em;margin-top:auto;max-width:980px}}
.base{{display:flex;align-items:center;justify-content:space-between;margin-top:40px;gap:24px}}
.dest{{font-size:21px;font-weight:600;color:#161B2C;background:#C99A44;padding:10px 16px;border-radius:2px;max-width:720px}}
.rod{{font-size:19px;color:#C7CBD6;white-space:nowrap}}
</style></head><body><div class="faixa"></div><div class="borda"></div><div class="box">
<div class="topo"><span class="marca">Ganica</span><span class="sep"></span><span class="kicker">{e(kicker)}</span></div>
<h1>{e(titulo)}</h1>
<div class="base">{f'<span class="dest">{e(destaque)}</span>' if destaque else '<span></span>'}<span class="rod">{e(rodape)}</span></div>
</div></body></html>"""


LOGO = f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS_FONTES}
*{{margin:0;padding:0}}body{{width:512px;height:512px;background:#161B2C;display:flex;align-items:center;justify-content:center}}
span{{font-family:'Frank Ruhl Libre';font-weight:700;font-size:300px;color:#C99A44;line-height:1;margin-top:-20px}}
</style></head><body><span>G</span></body></html>"""


async def render(pg, conteudo, destino, w, h):
    await pg.set_viewport_size({"width": w, "height": h})
    await pg.set_content(conteudo, wait_until="load")
    await pg.evaluate("document.fonts.ready")
    destino.parent.mkdir(parents=True, exist_ok=True)
    await pg.screenshot(path=str(destino), type="png")


async def main(todas):
    OG.mkdir(parents=True, exist_ok=True)
    async with async_playwright() as p:
        nav = await p.chromium.launch()
        pg = await nav.new_page()
        fixos = [
            (OG / "ganica.png", cartao("Consultoria de CRO para e-commerce", "Seu tráfego já foi conquistado. O problema é o que acontece depois do clique.", "", "ganica.com.br"), 1200, 630),
            (OG / "estudos.png", cartao("Estudos exclusivos de CRO", "Dado de mercado, heatmap real e funil de conversão, lidos com rigor.", "", "ganica.com.br/estudos"), 1200, 630),
            (RAIZ / "src" / "assets" / "img" / "logo-ganica.png", LOGO, 512, 512),
        ]
        for destino, conteudo, w, h in fixos:
            if todas or not destino.exists():
                await render(pg, conteudo, destino, w, h)
                print("gerado", destino.relative_to(RAIZ))
        for md in sorted((RAIZ / "src" / "artigos").glob("*.md")):
            fm = yaml.safe_load(md.read_text(encoding="utf-8").split("---", 2)[1]) or {}
            destino = OG / f"{fm['slug']}.png"
            if destino.exists() and not todas:
                continue
            await render(pg, cartao(fm.get("card_kicker") or "Estudo", fm["title"], fm.get("card_destaque") or "", "Por Narcipe Viana · ganica.com.br"), destino, 1200, 630)
            print("gerado", destino.relative_to(RAIZ))
        await nav.close()


if __name__ == "__main__":
    asyncio.run(main("--todas" in sys.argv))
