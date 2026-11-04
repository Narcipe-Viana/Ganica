// Configuração do Eleventy (gerador estático) do site da Ganica.
// O design vive em src/_includes; o conteúdo dos artigos vive em src/artigos/*.md
// e é editado pelo Pages CMS (ver .pages.yml).

import { readFileSync } from "node:fs";

// Largura e altura de uma imagem PNG, JPEG ou WebP do site (para width/height e evitar CLS).
export function dimensoesImagem(src) {
  try {
    const b = readFileSync(new URL(`./src${decodeURI(src)}`, import.meta.url));
    if (b.toString("ascii", 1, 4) === "PNG") return { w: b.readUInt32BE(16), h: b.readUInt32BE(20) };
    if (b.toString("ascii", 8, 12) === "WEBP") {
      const t = b.toString("ascii", 12, 16);
      if (t === "VP8X") return { w: 1 + b.readUIntLE(24, 3), h: 1 + b.readUIntLE(27, 3) };
      if (t === "VP8 ") return { w: b.readUInt16LE(26) & 0x3fff, h: b.readUInt16LE(28) & 0x3fff };
      if (t === "VP8L") { const v = b.readUInt32LE(21); return { w: (v & 0x3fff) + 1, h: ((v >> 14) & 0x3fff) + 1 }; }
    }
    if (b[0] === 0xff && b[1] === 0xd8) {
      let i = 2;
      while (i < b.length) {
        const m = b[i + 1], len = b.readUInt16BE(i + 2);
        if (m >= 0xc0 && m <= 0xc3) return { w: b.readUInt16BE(i + 7), h: b.readUInt16BE(i + 5) };
        i += 2 + len;
      }
    }
  } catch (e) {}
  return null;
}

const MESES = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho",
  "agosto", "setembro", "outubro", "novembro", "dezembro"];

function toDate(d) {
  // Datas do YAML sem aspas chegam como Date à meia-noite UTC; com aspas, como texto.
  // Normalizar as duas para meio-dia UTC do mesmo dia, para a ordenação não depender das aspas.
  if (d instanceof Date) return new Date(`${d.toISOString().slice(0, 10)}T12:00:00Z`);
  // datas "AAAA-MM-DD" sem hora: interpretar como meio-dia UTC para não virar o dia anterior no fuso -03
  return new Date(String(d).length === 10 ? `${d}T12:00:00Z` : d);
}

export default function (eleventyConfig) {
  eleventyConfig.addPassthroughCopy({ "src/assets": "assets" });
  eleventyConfig.addPassthroughCopy({ "src/favicon.svg": "favicon.svg" });
  eleventyConfig.addPassthroughCopy({ "src/assets/img/favicon-48.png": "favicon-48.png" });
  eleventyConfig.addPassthroughCopy({ "src/assets/img/apple-touch-icon.png": "apple-touch-icon.png" });
  eleventyConfig.addPassthroughCopy({ "CNAME": "CNAME" });
  eleventyConfig.addPassthroughCopy({ "robots.txt": "robots.txt" });
  // Chave do IndexNow (arquivo de 32 caracteres hexadecimais na raiz do site)
  eleventyConfig.addPassthroughCopy({ "src/*.txt": "/" });
  eleventyConfig.addPassthroughCopy({ "src/assets/img/logo-ganica.png": "logo-ganica.png" });

  // Datas
  eleventyConfig.addFilter("dataBR", (d) => {
    const x = toDate(d);
    return `${x.getUTCDate()} de ${MESES[x.getUTCMonth()]} de ${x.getUTCFullYear()}`;
  });
  const MESES_CURTOS = ["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"];
  eleventyConfig.addFilter("dataCurta", (d) => {
    const x = toDate(d);
    return `${String(x.getUTCDate()).padStart(2, "0")} ${MESES_CURTOS[x.getUTCMonth()]} ${x.getUTCFullYear()}`;
  });
  eleventyConfig.addGlobalData("anoAtual", () => new Date().getUTCFullYear());
  eleventyConfig.addFilter("dataISO", (d) => toDate(d).toISOString().slice(0, 10));

  // Tempo de leitura (~200 palavras por minuto, mínimo 2)
  eleventyConfig.addFilter("leitura", (html) => {
    const palavras = String(html || "").replace(/<[^>]+>/g, " ").split(/\s+/).filter(Boolean).length;
    return Math.max(2, Math.round(palavras / 200));
  });

  // Markdown em linha para campos curtos do front matter (resumo, FAQ, fontes)
  let md;
  eleventyConfig.amendLibrary("md", (lib) => { md = lib; });
  eleventyConfig.addFilter("mdInline", (s) => (md ? md.renderInline(String(s || "")) : s));
  eleventyConfig.addFilter("md", (s) => (md ? md.render(String(s || "")) : s));
  eleventyConfig.addFilter("json", (v) => JSON.stringify(v));
  // Títulos: impede quebra de linha no hífen ("e-" numa linha e "commerce" na outra)
  eleventyConfig.addFilter("semQuebraHifen", (s) =>
    String(s || "")
      .replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;")
      .replace(/([\p{L}\d]+(?:-[\p{L}\d]+)+)/gu, '<span class="nw">$1</span>'));
  // Etiqueta "Novo": estudo publicado há até 7 dias (o site é regerado todo dia pelo workflow)
  const AGORA = Date.now();
  eleventyConfig.addFilter("ehNovo", (d) => (AGORA - toDate(d).getTime()) <= 7 * 24 * 3600 * 1000);
  eleventyConfig.addFilter("palavras", (html) =>
    String(html || "").replace(/<[^>]+>/g, " ").split(/\s+/).filter(Boolean).length);
  eleventyConfig.addFilter("dataRFC3339", (d) => toDate(d).toISOString());
  eleventyConfig.addFilter("textoPuro", (s) => String(s || "").replace(/<[^>]+>/g, "").replace(/\*\*/g, ""));
  // "CRO · Checkout mobile" -> "Checkout mobile"
  eleventyConfig.addFilter("kickerFim", (s) => String(s || "").split("·").pop().trim());
  eleventyConfig.addFilter("comPonto", (s) => {
    const t = String(s || "").trim();
    return /[.!?]$/.test(t) ? t : `${t}.`;
  });
  // Fonte: "Título | https://..." ou só a URL. Devolve { titulo, url, dominio }.
  const fonte = (s) => {
    const txt = String(s || "").trim();
    const i = txt.lastIndexOf(" | ");
    const url = i >= 0 ? txt.slice(i + 3).trim() : txt;
    let dominio = url;
    try { dominio = new URL(url).hostname.replace(/^www\d?\./, ""); } catch (e) {}
    return { titulo: i >= 0 ? txt.slice(0, i).trim() : dominio, url, dominio };
  };
  eleventyConfig.addFilter("fonte", fonte);
  eleventyConfig.addFilter("fonteUrl", (s) => fonte(s).url);
  eleventyConfig.addFilter("dimensoes", (src) => dimensoesImagem(src));
  eleventyConfig.addFilter("pad2", (n) => String(n).padStart(2, "0"));

  // Coleção de estudos publicados, do mais recente para o mais antigo
  eleventyConfig.addCollection("estudos", (api) =>
    api.getFilteredByGlob("src/artigos/*.md")
      .filter((p) => !p.data.rascunho)
      // Mesmo dia: o publicado por último (campo "hora", HH:MM de Brasília) fica no topo
      .sort((a, b) => (toDate(b.data.date) - toDate(a.data.date)) ||
        String(b.data.hora || "00:00").localeCompare(String(a.data.hora || "00:00")))
  );

  // Componentes do design aplicados ao HTML gerado pelo Markdown do corpo:
  // tabela -> .data-table dentro de .data-table-wrap; parágrafo em itálico logo após
  // a tabela -> legenda (.table-caption); citação (>) -> .pull-quote.
  eleventyConfig.addTransform("componentes-prose", function (content) {
    if (!(this.page.outputPath || "").endsWith(".html")) return content;
    return content
      .replace(/<table>/g, '<div class="data-table-wrap"><table class="data-table">')
      .replace(/<\/table>\s*<p><em>([\s\S]*?)<\/em><\/p>/g, '</table></div>\n<p class="table-caption">$1</p>')
      .replace(/<\/table>(?!\s*<\/div>)/g, "</table></div>")
      // Imagem do corpo em Markdown, ![alt](/assets/... "legenda"), vira figura com legenda,
      // dimensões reais (sem CLS) e carregamento preguiçoso.
      .replace(/<p>\s*<img src="([^"]+)" alt="([^"]*)"(?: title="([^"]*)")?\s*\/?>\s*<\/p>/g, (m, src, alt, legenda) => {
        const d = dimensoesImagem(src);
        const dim = d ? ` width="${d.w}" height="${d.h}"` : "";
        const cap = legenda ? `<figcaption>${legenda}</figcaption>` : "";
        return `<figure class="figura"><a href="${src}" class="figura-link" aria-label="Abrir imagem em tamanho real"><img src="${src}" alt="${alt}"${dim} loading="lazy" decoding="async"></a>${cap}</figure>`;
      })
      .replace(/<blockquote>\s*<p>([\s\S]*?)<\/p>\s*<\/blockquote>/g, '<p class="pull-quote">$1</p>');
  });

  return {
    dir: { input: "src", includes: "_includes", data: "_data", output: "_site" },
    markdownTemplateEngine: false,
    htmlTemplateEngine: "njk",
  };
}
