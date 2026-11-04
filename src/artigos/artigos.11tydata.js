// Dados comuns a todos os artigos: layout, URL na raiz (/slug.html, mesmo padrão
// das URLs já indexadas) e rascunhos fora do site publicado.
export default {
  layout: "layouts/artigo.njk",
  eleventyComputed: {
    permalink: (data) => (data.rascunho ? false : `/${data.slug}.html`),
    // Imagens do corpo (Markdown) para o schema do artigo
    imagens_corpo: (data) =>
      [...String(data.page?.rawInput || "").matchAll(/!\[([^\]]*)\]\((\/[^\s)]+)/g)].map((m) => m[2]),
    eleventyExcludeFromCollections: (data) => !!data.rascunho,
  },
};
