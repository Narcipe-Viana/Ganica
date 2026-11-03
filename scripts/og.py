#!/usr/bin/env python3
"""Gera as imagens de compartilhamento (Open Graph, 1200x630) e o logo do site.

- Uma imagem por estudo em src/assets/og/<slug>.png (só cria as que faltam; use --todas para refazer).
- src/assets/og/ganica.png (home), src/assets/og/estudos.png (índice) e os ícones PNG (logo 512, favicon 48, Apple 180),
  gerados a partir de src/favicon.svg.

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
CSS_FONTES = "".join(
    _fonte("Lexend Deca", p, f"lexend-deca/files/lexend-deca-latin-{p}-normal.woff2") for p in (400, 500, 600)
)
LOGO_SVG = (RAIZ / "src" / "assets" / "img" / "logo-ganica.svg").read_text(encoding="utf-8")
FAVICON_SVG = (RAIZ / "src" / "favicon.svg").read_text(encoding="utf-8")
TRAMA = "data:image/svg+xml;base64," + base64.b64encode((RAIZ / "src" / "assets" / "img" / "trama.svg").read_bytes()).decode()


def cartao(kicker, titulo, destaque, rodape):
    e = html.escape
    tam = 62 if len(titulo) <= 70 else 52 if len(titulo) <= 95 else 44
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS_FONTES}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1200px;height:630px;background:#F5F9F9;color:#0B3842;font-family:'Lexend Deca';position:relative;overflow:hidden}}
.trama{{position:absolute;inset:0 0 0 40%;background:url('{TRAMA}') center/1200px 900px;opacity:.42;-webkit-mask-image:linear-gradient(to right,transparent,#000 62%)}}
.box{{position:absolute;left:72px;right:72px;top:60px;bottom:60px;display:flex;flex-direction:column}}
.topo{{display:flex;align-items:center;justify-content:space-between;gap:24px}}
.marca{{width:190px}}.marca svg{{display:block;width:100%;height:auto}}
.kicker{{font-size:20px;font-weight:500;color:#107088}}
h1{{font-weight:500;font-size:{tam}px;line-height:1.1;letter-spacing:-.015em;margin-top:auto;max-width:1020px}}
.base{{display:flex;align-items:center;justify-content:space-between;margin-top:36px;gap:24px}}
.dest{{font-size:22px;font-weight:600;color:#0B3842;background:#FAB32B;padding:10px 18px;border-radius:12px;max-width:760px}}
.rod{{font-size:20px;color:#466069;white-space:nowrap}}
</style></head><body><div class="trama"></div><div class="box">
<div class="topo"><span class="marca">{LOGO_SVG}</span><span class="kicker">{e(kicker)}</span></div>
<h1>{e(titulo)}</h1>
<div class="base">{f'<span class="dest">{e(destaque)}</span>' if destaque else '<span></span>'}<span class="rod">{e(rodape)}</span></div>
</div></body></html>"""


def icone(tam):
    """Símbolo da logo em PNG quadrado (schema Organization, favicon, ícone do iPhone)."""
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
*{{margin:0;padding:0}}body{{width:{tam}px;height:{tam}px;background:#fff}}svg{{display:block;width:100%;height:100%}}
</style></head><body>{FAVICON_SVG}</body></html>"""


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
            (OG / "estudos.png", cartao("Estudos exclusivos de CRO", "Biblioteca de estudos: dado de mercado, heatmap real e funil de conversão.", "", "ganica.com.br/estudos"), 1200, 630),
            (RAIZ / "src" / "assets" / "img" / "logo-ganica.png", icone(512), 512, 512),
            (RAIZ / "src" / "assets" / "img" / "favicon-48.png", icone(48), 48, 48),
            (RAIZ / "src" / "assets" / "img" / "apple-touch-icon.png", icone(180), 180, 180),
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
