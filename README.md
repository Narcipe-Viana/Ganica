# Site da Ganica (ganica.com.br)

Site estático gerado com [Eleventy](https://www.11ty.dev/) e publicado no GitHub Pages.

- **Editar conteúdo sem código:** entre em https://app.pagescms.org com sua conta do GitHub e abra este repositório.
- **Estudos (artigos):** `src/artigos/*.md` (um arquivo por estudo; o formulário do CMS edita esses arquivos).
- **Design:** `src/_includes/` (template único; mudar aqui muda todos os estudos).
- **Home:** `src/index.njk` · **Índice de estudos:** `src/estudos.njk` · **Sitemap:** gerado sozinho.
- **Publicação automática:** `editorial/` (manual editorial e fila de pautas) + tarefa agendada no Claude.
- **Checagens:** `npx @11ty/eleventy && python3 scripts/qa.py`.
- **Deploy:** todo push em `main` roda `.github/workflows/publicar.yml`, que gera o site e publica na branch `gh-pages`.
