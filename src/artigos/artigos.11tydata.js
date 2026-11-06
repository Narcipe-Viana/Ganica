// Dados comuns a todos os artigos: layout, URL na raiz (/slug.html, mesmo padrão
// das URLs já indexadas) e rascunhos fora do site publicado.
// Data de hoje em Brasília (AAAA-MM-DD), no momento do build.
const HOJE_BR = new Date(Date.now() - 3 * 3600 * 1000).toISOString().slice(0, 10);
const diaISO = (d) => (d instanceof Date ? d.toISOString().slice(0, 10) : String(d || "").slice(0, 10));
// Estudo agendado: pronto (rascunho: false), mas com publicar_em no futuro. Fica fora do site
// até o build do dia (o workflow roda todo dia às 00:05 de Brasília e publica sozinho).
const fora = (data) => !!data.rascunho || (!!data.publicar_em && diaISO(data.publicar_em) > HOJE_BR);

export default {
  layout: "layouts/artigo.njk",
  eleventyComputed: {
    permalink: (data) => (fora(data) ? false : `/${data.slug}.html`),
    // Imagens do corpo (Markdown) para o schema do artigo
    imagens_corpo: (data) =>
      [...String(data.page?.rawInput || "").matchAll(/!\[([^\]]*)\]\((\/[^\s)]+)/g)].map((m) => m[2]),
    eleventyExcludeFromCollections: (data) => fora(data),
  },
};
