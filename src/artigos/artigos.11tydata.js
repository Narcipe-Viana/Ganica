// Dados comuns a todos os artigos: layout, URL na raiz (/slug.html, mesmo padrão
// das URLs já indexadas) e rascunhos fora do site publicado.
export default {
  layout: "layouts/artigo.njk",
  eleventyComputed: {
    permalink: (data) => (data.rascunho ? false : `/${data.slug}.html`),
    eleventyExcludeFromCollections: (data) => !!data.rascunho,
  },
};
