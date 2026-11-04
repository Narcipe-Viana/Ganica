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

## 1.1 Ordem de prioridades

1. **Conteúdo rico, que gera valor real para o leitor.** Nada passa na frente disso.
2. **SEO**, logo abaixo: todo estudo publicado precisa estar indexável, no sitemap com a data certa,
   com título, descrição, dados estruturados e links internos corretos. Um estudo bom que o Google
   não encontra não cumpre seu papel. O `scripts/qa.py` bloqueia a publicação se o sitemap estiver
   incompleto ou inválido, e o workflow confere o sitemap no ar depois de cada publicação.
3. Todo o resto (formato, ritmo, distribuição).

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
5. `resposta_curta`: 40 a 70 palavras que respondem o título por inteiro (ver seção 8).
   `resumo`: 4 ou 5 itens (o "Resumo rápido"), cada um com um fato ou conclusão concreta; números em **negrito**.
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

Objetivo: **nenhum leitor consegue descobrir qual é o cliente**, nem juntando vários estudos.

Pautas com `usa_dado_cliente: true` só podem usar os números já anonimizados em `dados_anonimizados`
do `pautas.yml`. E sempre:

- **Segmento no nível mais amplo possível**: "um e-commerce brasileiro de saúde e bem-estar" ou
  "um e-commerce de consumo recorrente". Nunca o tipo exato de produto, porte, faturamento, número de
  produtos, tempo de mercado, região, plataforma, meios de pagamento contratados ou ferramentas usadas.
- **Nunca nomear** cliente, marca, agência parceira, produto real, categoria real do catálogo,
  gateway, antifraude, cidade ou estado.
- **Números só relativos ou arredondados** ("quase 3 vezes", "perto de metade", "cerca de 1 em 5").
  Proibido: valor com casas decimais, valor em reais, volume de sessões, pedidos ou faturamento,
  taxa de conversão exata.
- **Período vago**: "ao longo de alguns meses de 2026". Nunca mês, semana ou data comemorativa
  ligada ao dado (ex.: não dizer que o dado veio da preparação de uma Black Friday específica).
- **Sem mecânica reconhecível**: nenhuma oferta, cupom, frete, brinde, política de desconto ou
  sequência de checkout descrita de forma que alguém reconheça o site.
- **Contra o efeito mosaico**: cada estudo cita "um e-commerce" como caso isolado. Nunca dizer que
  é o mesmo cliente de outro estudo, nunca somar no mesmo texto vários achados do mesmo cliente,
  e nunca repetir num estudo o detalhe de contexto usado em outro. Antes de escrever, ler os
  estudos já publicados e conferir o que já foi dito sobre casos de cliente.
- **Formato**: o caso entra como ilustração de um método que o leitor pode aplicar na própria loja,
  nunca como relato de bastidor do cliente.
- Nomes protegidos são bloqueados automaticamente pelo `scripts/qa.py` (lista em hash em
  `bloqueio.sha256`), que também reprova número com casas decimais e valor em reais em estudos
  marcados com `usa_dado_cliente: true` no front matter.

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

## 8. GEO: escrever para ser citado por IA (ChatGPT, Gemini, AI Overviews/AI Mode, Perplexity, Claude)

Motores de resposta não leem o artigo inteiro: eles recortam **trechos** que respondem bem a uma
pergunta e citam quem parece a fonte mais confiável. Cada estudo é escrito para ser recortado.

**Resposta primeiro**
- `resposta_curta` (obrigatória): 40 a 70 palavras que respondem a pergunta do título de forma
  completa, sem depender do resto do texto. Começa pela resposta, não pelo contexto. Aparece no topo
  do artigo ("Resposta direta") e vai para o schema como `abstract`.
- Em cada seção `##`, a **primeira frase responde** o que o título da seção promete. Detalhe e
  nuance vêm depois.

**Títulos que são perguntas reais**
- Pelo menos metade dos `##` em forma de pergunta que alguém digitaria ou falaria para uma IA
  ("Por que o mobile converte menos no checkout?", "Como montar o funil por dispositivo no GA4?").
- Variações naturais da palavra-chave e perguntas relacionadas (o que, por que, como, quanto,
  quando, vale a pena) espalhadas entre títulos e FAQ.

**Trechos autossuficientes**
- Cada parágrafo se sustenta sozinho: retome o sujeito ("o checkout mobile", e não "ele"),
  evite "como vimos acima". Parágrafos de 2 a 4 frases.
- Defina o termo técnico na primeira vez que aparece, numa frase do tipo "X é Y que Z".
- Ao menos uma **lista numerada de passos** (o método) e uma **tabela** comparativa quando houver
  dado, porque são os formatos mais extraídos por IA.

**Fatos com atribuição explícita**
- Número sempre colado à fonte na mesma frase ("segundo o Banco Central, ...", "em análise da
  Ganica de um e-commerce de saúde, ..."). IA cita frase com fonte; frase sem fonte é descartada.
- `fontes_urls`: lista com o link de cada fonte primária citada, no formato `"Título legível (Instituição) | https://..."`. Aparece no fim do artigo como "Links das fontes" (link clicável, com o domínio) e vai para o schema como `citation`.
- Links externos no texto (obrigatório): o dado de terceiro leva o link da fonte primária no próprio trecho em que aparece, em markdown `[texto descritivo](https://...)`, no nome da fonte ou do estudo, nunca em "clique aqui". Mínimo de 2 links externos no corpo quando houver 2 ou mais fontes; todo link do corpo também entra em `fontes_urls`. Linkar a fonte primária (a pesquisa, a documentação oficial, a lei), não um agregador, quando ela existir. Sem `nofollow`: citar fonte confiável é sinal de qualidade para o Google e dá ao leitor e aos motores de IA como conferir o número.
- Datas e períodos explícitos para dado público ("em 2025", "entre 2020 e 2025").

**Autoridade e entidade**
- Escrever como quem fez a análise: "na Ganica, quando analisamos...", "o método que usamos nos
  diagnósticos é...". Experiência de primeira mão é o principal diferencial frente a conteúdo genérico.
- Nome da Ganica e do autor de forma consistente. Não inventar credenciais, clientes ou resultados.
- Seção "O que ainda não sabemos": honestidade sobre limites aumenta a confiança de quem cita.

**FAQ**
- 3 a 5 perguntas que **não** repetem os títulos `##`; respostas de 2 a 4 frases, começando pela
  resposta ("Sim.", "Não.", "Depende de X: ...").

**Técnico (já automático no template)**
- BlogPosting com `abstract`, `citation`, `image`, `wordCount`, datas com fuso, autor e organização
  ligados por `@id`; BreadcrumbList; índice `/estudos/` com ItemList; `/feed.xml`; `/llms.txt`;
  imagem de compartilhamento gerada por `scripts/og.py`.

## 9. Estudos de tendência (Google Trends)

Fonte: `editorial/tendencias.json` (e o resumo `TENDENCIAS.md`), atualizado todo dia às 5h10 pelo
GitHub Actions com: pesquisas em alta no Brasil, consultas em ascensão da categoria Compras e de
termos-semente de e-commerce e marketplace (90 dias), e as próximas datas do varejo.

**Como escolher o tema (quartas-feiras)**
1. Ler o arquivo e conferir `gerado_em`. Se tiver mais de 3 dias, buscar o sinal por WebSearch e
   tratar o arquivo só como pista.
2. Candidatos, em ordem de preferência:
   a) consulta em ascensão ligada a uma data próxima do calendário (ex.: dúvidas sobre Black Friday);
   b) consulta em ascensão de um termo-semente que um decisor de e-commerce faria (meios de pagamento,
      marketplaces, frete, regras novas, ferramentas de venda);
   c) pesquisa "em alta hoje" com `relevante_ecommerce: true` e ligação real com comércio online.
3. Descartar: celebridades, esporte, política partidária, marcas de terceiros como protagonistas,
   consultas de navegação ("logo shopee png", "login"), termos em outro idioma, variações de série
   esparsa (`base_baixa: true`, pouca busca real), e qualquer coisa em que a Ganica não tenha leitura de CRO a dar.
4. Confirmar **por que** está subindo com WebSearch (notícia, regra nova, data). Sem causa
   confirmada, não vira estudo.
5. O ângulo é sempre "o que isso muda na conversão de uma loja", não a notícia. O estudo precisa
   continuar útil depois que a tendência passar (evergreen com gancho atual).
6. Registrar a pauta no `pautas.yml` com `tipo: tendencia` e um campo `sinal` (termo, valor,
   janela, link do Explore) antes de escrever.

**Como citar o Trends no texto**
- Sempre como índice relativo ou variação: "as buscas por X no Google cresceram cerca de N% nos
  últimos 90 dias, segundo o Google Trends". Nunca como volume ("milhões de buscas").
- "Aumento repentino" (Breakout) = alta acima de 5.000%; descrever como "salto repentino".
- Colocar o link do Explore em `fontes_urls` e a data da coleta em `fontes`.
- Se não houver tema que passe no critério, a quarta usa a próxima pauta `base`.

## 10. Estudos Marketing 3.0 + conhecimento de campo (sextas-feiras)

Fontes: `editorial/referencias/marketing-3-0.md` (paráfrase das ideias do livro de Kotler,
Kartajaya e Setiawan, 2010) e `editorial/conhecimento-campo.md` (padrões C1 a C15 observados em
diagnósticos reais, já generalizados).

**Fórmula do estudo: conceito, campo, dado, ação**
1. **Conceito**: a ideia do livro em linguagem simples, com atribuição (autores, título, 2010), em
   paráfrase. Nenhuma frase entre aspas atribuída ao livro.
2. **Campo**: o padrão de diagnóstico que mostra o conceito acontecendo (ou falhando) no e-commerce
   brasileiro. É a experiência de primeira mão: "é um padrão que encontramos com frequência".
3. **Dado**: pelo menos uma evidência verificável e atual (pesquisa pública primária, Google Trends,
   documentação oficial). O conceito nunca prova nada sozinho.
4. **Ação**: o que a loja faz na segunda-feira, em passos numerados, e como medir se funcionou.

**O que torna o estudo valioso (e não resumo de livro)**
- Dizer onde o livro **acertou** e onde **envelheceu** (o livro é anterior a Pix, marketplaces
  dominantes, TikTok Shop e busca por IA). Essa leitura crítica é o diferencial.
- Uma "tese própria da Ganica" explícita: a frase que a Ganica defende e que o livro sozinho não diz.
- Nada de "propósito" ou "valores" soltos: todo conceito termina numa decisão de página, oferta,
  checkout, mídia ou recompra.
- Respeitar as regras de uso de `conhecimento-campo.md` (no máximo um padrão como caso central,
  nada de detalhe novo) e a seção 5 (anonimização).

## 11. Estudos a partir da CXL (sextas-feiras)

Toda sexta, um estudo próprio da Ganica parte de um artigo do blog da CXL, de preferência sobre IA,
(https://cxl.com/blog/), confronta o que ele diz com dados do Brasil e chega a uma conclusão da
Ganica. Modelo de referência: `src/artigos/ia-pesquisa-cro-ecommerce-brasil.md`.

**Por que não é reescrita.** Reescrever ou traduzir o texto da CXL com outro título é conteúdo
derivado de terceiros: viola direito autoral e cai na política de spam do Google para conteúdo
reaproveitado (*scraped content*). E não seria citado por IA, porque não acrescenta nada. O valor
está no que o artigo original não tem: dado brasileiro, contexto brasileiro (LGPD, Pix, WhatsApp,
marketplaces locais, porte das lojas) e leitura de CRO da Ganica.

**Como escolher o artigo**
1. Abrir https://cxl.com/blog/ e listar os artigos sobre IA (IA em CRO, experimentação, analytics,
   busca por IA/GEO/AEO, agentes, IA em marketing). Para abrir um artigo, achar a URL dele pelo
   WebSearch e então usar WebFetch nela.
2. Descartar os já listados em `editorial/cxl-usados.yml` (seção `usados`).
3. Preferir, nesta ordem: o mais recente; o mais ligado a conversão de e-commerce; o que tem um
   ângulo brasileiro claro. A seção `candidatos` do mesmo arquivo traz os já mapeados.
4. Se nenhum artigo de IA da CXL ainda não usado **agregar** para um decisor de e-commerce, analisar
   os outros conteúdos da CXL (CRO e testes A/B, analytics, UX e design, psicologia do consumidor,
   copy, precificação), inclusive os mais antigos das categorias do blog, com o mesmo método e a
   mesma exigência de dado brasileiro. Preferir os que conversam com conversão de e-commerce e que
   ainda não foram usados (`editorial/cxl-usados.yml`, candidatos de IA e de outros temas).
5. Só se nada da CXL agregar, a sexta usa a próxima pauta `m30` (Marketing 3.0 + campo).
6. "Agregar" significa: o tema importa para quem vende online no Brasil, existe dado brasileiro
   verificável para confrontar e a Ganica tem uma leitura própria a acrescentar. Artigo que só daria
   um resumo não agrega.

**Estrutura obrigatória (além das seções 3 e 8)**
- O que o artigo da CXL propõe: resumo em paráfrase, com autor, data e link, em no máximo
  2 parágrafos. Nenhuma frase traduzida ou copiada; nenhuma citação entre aspas maior que 10 palavras.
- As lacunas do artigo original (dados ausentes, contexto só dos EUA, falta de resultado, temas não
  tratados), dito com respeito e sem provocação.
- Como é no Brasil: **pelo menos 2 fontes brasileiras primárias** e verificadas (ex.: Cetic.br,
  IBGE, Banco Central, ANPD, legislação, entidades do varejo com metodologia divulgada), de
  preferência numa tabela de 2 colunas.
- O que a Ganica conclui: a tese própria, que não está no artigo da CXL.
- O que fazer: passos numerados aplicáveis a uma loja brasileira.
- O que ainda não sabemos.
- Título, slug, estrutura e exemplos próprios: nunca o título da CXL traduzido.
- `card_kicker`: "IA · <tema>" quando o artigo de partida for sobre IA; senão "CRO · <tema>". Em `fontes`, o artigo da CXL vem primeiro como "artigo de partida".
- Depois de publicar, mover o artigo de `candidatos` para `usados` em `editorial/cxl-usados.yml`.

## 12. Estudos técnicos (terças-feiras)

Conteúdo técnico sobre captação e uso de dados num e-commerce: rastreamento correto (GA4, GTM,
eventos de e-commerce), ferramentas (PostHog, Hotjar, Clarity, LogRocket e outras), integrações
(BigQuery, Looker Studio) e IA aplicada sobre esses dados. Objetivo: demonstrar credibilidade
técnica da Ganica para quem decide e para quem executa. Modelo:
`src/artigos/integrar-posthog-bigquery-ecommerce.md`.

**Regras**
- Todo passo técnico, limite, preço ou comportamento de ferramenta conferido na documentação oficial
  no dia (WebFetch), com o link em `fontes_urls`. Ferramentas mudam rápido: registrar em `fontes`
  o mês da consulta.
- Prova social só a partir de `editorial/casos-tecnicos.md`, com a redação e os limites definidos
  lá. Nunca inventar caso, resultado ou prática da Ganica. Recomendação é escrita como recomendação
  ("a recomendação da Ganica é..."), não como prática comprovada.
- Neutro em relação a fornecedores: nada de tom de propaganda, comparação pela pergunta de negócio.
- LGPD sempre que houver dado pessoal (gravação de sessão, IP, identificadores).
- Trechos de código só curtos e conferidos na documentação; nomes de evento e parâmetro em `código`.
- `card_kicker`: "Técnico · <tema>".
