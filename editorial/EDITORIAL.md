# Manual editorial da Ganica

Este manual é seguido em toda publicação automática de estudos no site ganica.com.br.
Ele existe porque nenhum humano revisa o artigo antes de ir ao ar: as regras abaixo e as
checagens automáticas (`scripts/qa.py`) fazem esse papel. **Na dúvida, não publique.**

## 1. Quem é a Ganica (e por que isso muda o texto)

A Ganica é uma consultoria de CRO para e-commerce que atende clientes premium. Não é uma agência
de volume. O objetivo de cada estudo é mostrar, para quem decide (dono, diretor de e-commerce,
gestor de mídia), uma forma de ler dados que ele ainda não estava usando, com honestidade sobre
o que a evidência sustenta e o que não sustenta.

Um estudo da Ganica nunca é:
- lista genérica de dicas ("10 dicas para aumentar a conversão");
- texto que poderia ter sido escrito sem olhar nenhum dado;
- promessa de resultado ("aumente suas vendas em X%");
- crítica ou provocação contra agências ou concorrentes.

## 2. Voz e estilo

- Português do Brasil, direto, frases curtas a médias. Tom de consultor sênior explicando para um
  decisor inteligente, não de professor nem de vendedor.
- **Proibido travessão (—)** em qualquer texto visível. Reescrever com ponto, vírgula, dois-pontos
  ou parênteses. O hífen de palavras compostas (e-commerce) é normal.
- Sem anglicismo desnecessário quando existe palavra comum em português. Termos técnicos do
  mercado (checkout, CRO, GA4, ticket médio, heatmap) são aceitos.
- Sem emoji, sem exclamação, sem caixa alta para ênfase.
- Toda afirmação forte vem acompanhada do que a sustenta. Hipótese é chamada de hipótese.
- Seção "O que ainda não sabemos" (ou equivalente) sempre que o estudo usar amostra pequena,
  um cliente só ou dado indireto.

## 3. Estrutura obrigatória de um estudo

Campos do front matter (os mesmos do formulário no Pages CMS): ver `src/artigos/` como modelo.

1. `title`: título do H1. Pode ser pergunta ou afirmação contraintuitiva. Até ~90 caracteres.
2. `seo_title`: até 65 caracteres, com a palavra-chave principal perto do início.
3. `description`: 120 a 160 caracteres, com a palavra-chave e o achado principal.
4. `deck`: linha fina de 1 a 2 frases que diz o que o leitor vai entender.
5. `resumo`: 4 ou 5 itens (o "Resumo rápido"), cada um com um fato ou conclusão concreta; números em **negrito**.
6. Corpo (Markdown) com **pelo menos 5 seções `##`**, entre **1.200 e 2.000 palavras**, contendo:
   - o problema como o mercado costuma enxergar;
   - a evidência (dado público verificado, levantamento próprio, ou caso anonimizado autorizado);
   - a leitura da Ganica (o que a evidência realmente mostra);
   - o que fazer na prática (passos concretos);
   - o que ainda não sabemos / limites da análise.
   - Pelo menos **1 link para `/#diagnostico`** e, quando houver, link para outro estudo relacionado.
   - Pelo menos uma tabela **ou** uma citação de destaque (`> frase`), quando fizer sentido.
   - Tabela em Markdown; uma linha em itálico logo abaixo da tabela vira a legenda (fonte da tabela).
7. `faq`: 3 a 5 perguntas reais que alguém digitaria no Google, com respostas de 2 a 4 frases.
8. `fontes`: todas as fontes, com nome do publicador e período; e a metodologia do que é análise própria.
9. Campos do card: `card_kicker` (ex. "CRO · Checkout"), `card_destaque` (o dado mais forte, curto),
   `card_resumo` (1 a 2 frases), `breadcrumb` (2 a 5 palavras).
10. `cta_titulo` e `cta_texto`: chamada final ligada ao tema do estudo, convidando ao diagnóstico.
11. `keywords`, `tags_artigo`, `sobre`: 3 a 6 itens cada.
12. `slug`: minúsculas, sem acento, palavras separadas por hífen, com a palavra-chave. **Nunca mudar depois de publicado.**

## 4. Regra de ouro dos números

**Todo número publicado precisa ter origem verificável.** Antes de publicar:
- Número de fonte pública: abrir a fonte (WebFetch) e confirmar que ela diz exatamente aquilo,
  no período citado. Fonte que não abre, que é agregador sem fonte primária, ou que diz outra
  coisa: o número sai do texto.
- Número de cliente: só se a pauta estiver autorizada e o número estiver em `dados_autorizados`.
  Publicar arredondado ou relativo ("cerca de 3 vezes", "perto de 20%").
- Número de exemplo: só em exemplo declarado como hipotético no próprio texto.
- Nunca inventar estatística, estudo, pesquisa, citação ou nome de especialista.
- Citações literais de fontes: no máximo uma por fonte, com menos de 15 palavras. O resto, paráfrase.

## 5. Anonimização de dado de cliente

- Nunca nomear cliente, marca, agência parceira, produto real do cliente, plataforma, cidade ou estado.
- Descrição máxima permitida: segmento amplo ("e-commerce de saúde", "e-commerce B2B técnico").
- Nunca valores absolutos de receita, sessões, pedidos, ticket ou taxa exata de conversão.
- Nunca mecânica de promoção, oferta, frete ou brinde reconhecível.
- Atenção ao efeito mosaico: não somar, ao longo de vários estudos, detalhes do mesmo cliente
  que juntos o identifiquem. Ao citar caso de cliente, reler os estudos já publicados.
- Nomes protegidos são bloqueados automaticamente pelo `scripts/qa.py` (lista em hash em `bloqueio.sha256`).

## 6. Design e mobile primeiro

O design é fixo no template (`src/_includes/layouts/artigo.njk`). O conteúdo nunca carrega CSS ou
HTML de layout próprio. Antes de publicar, o `scripts/qa.py` confere 390px (celular) e 1280px
(desktop): sem rolagem horizontal, imagens carregando, sem erro de JavaScript. Olhar as capturas
de `.qa/` do artigo em 390px antes de publicar: tabela legível, títulos sem quebra estranha.

## 7. SEO

- Uma intenção de busca por estudo; a palavra-chave da pauta aparece no `seo_title`, na
  `description`, no primeiro parágrafo e em pelo menos um `##`.
- Não repetir tema já publicado (ler `src/artigos/` antes).
- Schema (BlogPosting + BreadcrumbList) é gerado pelo template. FAQPage não é usado de propósito.
