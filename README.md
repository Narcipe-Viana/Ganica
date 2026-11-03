# Site da Ganica (ganica.com.br)

Site estático gerado com [Eleventy](https://www.11ty.dev/) e publicado no GitHub Pages.

- **Editar conteúdo sem código:** entre em https://app.pagescms.org com sua conta do GitHub e abra este repositório.
- **Estudos (artigos):** `src/artigos/*.md` (um arquivo por estudo; o formulário do CMS edita esses arquivos).
- **Design:** `src/_includes/` (template único; mudar aqui muda todos os estudos). Marca e componentes comuns em `css/base.css`; cards da biblioteca em `css/estudos.css`.
- **Logo:** `src/assets/img/logo-ganica.svg` e `src/favicon.svg`. Os ícones PNG e as imagens de compartilhamento saem de `python3 scripts/og.py --todas`.
- **Home:** `src/index.njk` · **Índice de estudos:** `src/estudos.njk` · **Sitemap:** gerado sozinho.
- **Publicação automática:** `editorial/` (manual editorial e fila de pautas) + tarefa agendada no Claude.
- **Checagens:** `npx @11ty/eleventy && python3 scripts/qa.py`.
- **Deploy:** todo push em `main` roda `.github/workflows/publicar.yml`, que gera o site e publica na branch `gh-pages`.
- **SEO após publicar:** `scripts/pos_publicacao.py` confere o sitemap no ar e avisa os buscadores via IndexNow (Bing/ChatGPT Search, Yandex). O Google lê o sitemap pelo Search Console e pelo `robots.txt`.
