---
title: "Auditoria de rastreamento no e-commerce: o checklist antes de confiar no GA4"
seo_title: "Auditoria GA4 no e-commerce: checklist de rastreamento"
og_title: "Auditoria de rastreamento: como saber se o GA4 da sua loja conta certo"
description: "Auditoria GA4 para e-commerce: como achar evento duplicado no GTM, conferir a compra pelo ID do pedido e separar erro de diferença normal antes de decidir."
twitter_description: "Evento contado em dobro, compra que some, número que não bate com a loja. O checklist para auditar o GA4 e o GTM antes de confiar em qualquer relatório."
slug: auditoria-rastreamento-ga4-gtm-ecommerce
date: '2026-11-10'
hora: "06:54"
updated: '2026-11-10'
rascunho: false
breadcrumb: Auditoria de rastreamento
secao: E-commerce
card_kicker: "Técnico · Rastreamento"
card_destaque: "Primeiro o dado, depois a conclusão"
card_titulo: "Auditoria de rastreamento no e-commerce: o checklist antes de confiar no GA4."
card_resumo: "Como achar evento duplicado no Tag Manager, conferir as compras do GA4 contra os pedidos da loja e separar erro de medição de diferença normal, com cada comportamento das ferramentas conferido na documentação oficial do Google."
tags_artigo:
  - GA4
  - Google Tag Manager
  - rastreamento
  - auditoria de dados
  - e-commerce
keywords:
  - auditoria GA4 e-commerce
  - evento duplicado GA4 GTM
  - compra duplicada GA4
  - transaction_id GA4
  - DebugView GA4
sobre:
  - Web analytics
  - Google Analytics 4
  - Google Tag Manager
  - Otimização de conversão (CRO)
imagem_og: ''
resposta_curta: "Uma auditoria de rastreamento confere se o GA4 conta o que de fato aconteceu na loja. O checklist tem três partes: achar disparos duplicados no Tag Assistant e no DebugView, cruzar cada compra do GA4 com os pedidos pagos pelo ID do pedido e separar erro de medição de diferença esperada, como consentimento recusado e dados atrasados. Só depois disso o número serve para decidir."
deck: "Antes de discutir por que a conversão caiu, vale perguntar se ela foi medida direito. Este guia mostra a ordem de auditoria que a Ganica recomenda para GA4 e Google Tag Manager num e-commerce, com cada comportamento das ferramentas conferido na documentação oficial do Google."
resumo:
  - "Evento contado em dobro costuma nascer de **tags sobrepostas** no Google Tag Manager. Num projeto de e-commerce em que atuamos, isso foi confirmado no DebugView e resolvido com consolidação de tags."
  - "Segundo o Google, o GA4 **deduplica compras com o mesmo ID de transação**. O efeito colateral: ID vazio ou repetido em pedidos diferentes faz o relatório **perder vendas**."
  - "A conferência mais confiável é cruzar o `transaction_id` das compras do GA4 com a **base de pedidos pagos** da loja, olhando falta e sobra."
  - "Parte da diferença é normal. O Google só modela quem recusou cookies com o modo de consentimento avançado e pelo menos **1.000 eventos por dia** com consentimento recusado por 7 dias, entre outros requisitos. Cumprir os requisitos não garante a modelagem, e a exportação para o BigQuery não traz esse dado modelado."
faq:
  - pergunta: "De quanto em quanto tempo devo auditar o GA4 da loja?"
    resposta: "A recomendação da Ganica é auditar sempre que o site muda de tema, de checkout, de plataforma ou de ferramenta de consentimento, e antes de qualquer data de pico. Fora disso, a recomendação é uma conferência mensal da compra contra os pedidos pagos."
  - pergunta: "O que fazer com os dados do período em que o evento estava duplicado?"
    resposta: "Anote o período e não o use em comparações sem tratamento. A recomendação da Ganica é registrar a data da correção e, se a exportação para o BigQuery já estava ligada naquele período, tratar as repetições na consulta antes de comparar meses."
  - pergunta: "Preciso do BigQuery para auditar o GA4?"
    resposta: "Não. O Tag Assistant e o DebugView mostram duplicidade sem BigQuery, e o relatório Transações do GA4 lista as compras pelo ID do pedido para comparar com a loja. O BigQuery ajuda quando o volume é grande ou quando é preciso tratar períodos antigos."
  - pergunta: "Quem deve fazer a auditoria de rastreamento, o time de marketing ou o de tecnologia?"
    resposta: "Os dois. O marketing sabe quais números orientam decisões e onde eles parecem estranhos; a tecnologia sabe onde as tags e o código foram instalados. A recomendação da Ganica é que uma pessoa só seja dona do contêiner do Tag Manager (o espaço onde ficam todas as tags da loja)."
fontes: "Experiência da Ganica em projeto de e-commerce com evento duplicado por tags sobrepostas no Google Tag Manager (sem identificação da empresa). Documentação oficial do Google, consultada em novembro de 2026: Central de Ajuda do Google Analytics (Measure ecommerce; Transactions report; Monitor events in DebugView; Behavioral modeling for consent mode; BigQuery Export; BigQuery Export schema), Central de Ajuda do Google Tag Manager (Get started with Tag Manager; Tag firing options), guias para desenvolvedores do Google Analytics (Measure ecommerce; Measure single-page applications). Lei 13.709/2018 (LGPD), arts. 5º e 6º, no portal da Câmara dos Deputados. A lógica da consulta descrita é da Ganica, a partir do esquema oficial da exportação. Ferramentas mudam com frequência; confira as páginas oficiais antes de aplicar."
fontes_urls:
  - "Measure ecommerce, Central de Ajuda do Google Analytics | https://support.google.com/analytics/answer/12313109?hl=en"
  - "Transactions report, Central de Ajuda do Google Analytics | https://support.google.com/analytics/answer/15227167"
  - "Monitor events in DebugView, Central de Ajuda do Google Analytics | https://support.google.com/analytics/answer/7201382?hl=en"
  - "Behavioral modeling for consent mode, Central de Ajuda do Google Analytics | https://support.google.com/analytics/answer/11161109?hl=en"
  - "BigQuery Export, Central de Ajuda do Google Analytics | https://support.google.com/analytics/answer/9358801"
  - "BigQuery Export schema, Central de Ajuda do Google Analytics | https://support.google.com/analytics/answer/7029846"
  - "Get started with Tag Manager, Central de Ajuda do Google Tag Manager | https://support.google.com/tagmanager/answer/6107056"
  - "Tag firing options, Central de Ajuda do Google Tag Manager | https://support.google.com/tagmanager/answer/6279951"
  - "Measure ecommerce, guia para desenvolvedores do Google Analytics | https://developers.google.com/analytics/devguides/collection/ga4/ecommerce"
  - "Measure single-page applications, guia para desenvolvedores do Google Analytics | https://developers.google.com/analytics/devguides/collection/ga4/single-page-applications"
  - "Lei nº 13.709/2018, Lei Geral de Proteção de Dados (Câmara dos Deputados) | https://www2.camara.leg.br/legin/fed/lei/2018/lei-13709-14-agosto-2018-787077-publicacaooriginal-156212-pl.html"
cta_titulo: "Os números da sua loja contam a mesma história que os seus pedidos?"
cta_texto: "Um diagnóstico de CRO começa conferindo o rastreamento: se a compra é medida uma vez, se nada se perde no caminho e onde a conversão de fato quebra."
autor_texto: "Sou consultor de CRO focado em e-commerce, com trabalho direto em estrutura de analytics (GTM, GA4, PostHog, BigQuery, Looker Studio) e auditoria comportamental. Minha regra é simples: antes de analisar, garantir que o dado conta a verdade."
---

## O que é uma auditoria de rastreamento e por que ela vem antes da análise?

Uma auditoria de rastreamento, ou auditoria do GA4 no e-commerce, é a conferência de que cada evento importante da loja (ver produto, adicionar ao carrinho, iniciar o checkout, comprar) é registrado uma vez, com os dados certos, no momento certo. Ela vem antes de qualquer análise de conversão porque um relatório errado não avisa que está errado: ele só mostra um número, e a equipe decide em cima dele.

No GA4, o Google Analytics 4, tudo é evento. O Google Tag Manager (GTM) é a ferramenta que decide quando cada evento é enviado, por meio de tags (o código que manda o dado) e acionadores (a regra que diz quando a tag dispara). Uma auditoria GA4 de e-commerce olha os dois lados: o que o GTM dispara e o que o GA4 recebe.

A recomendação da Ganica é abrir qualquer diagnóstico com uma pergunta simples: o número de compras que o GA4 mostra conversa com o número de pedidos pagos da loja? Se a resposta for "não sei", a auditoria vem primeiro, e o teste A/B, o redesenho e a troca de verba esperam.

## Por que o GA4 conta o mesmo evento duas vezes?

O GA4 conta o mesmo evento duas vezes quando duas estruturas diferentes mandam o mesmo dado. É um padrão que encontramos com frequência em diagnósticos: tags sobrepostas no gerenciador de tags.

Há três origens possíveis de duplicidade. A primeira é o código do Google instalado direto no tema da loja e, de novo, dentro do contêiner do GTM (o pacote onde ficam todas as tags da loja). A segunda são duas tags no GTM que enviam o mesmo evento, cada uma com um acionador diferente que dispara na mesma página. A terceira aparece em lojas feitas como aplicação de página única, em que a página muda sem recarregar: o [guia do Google para esse tipo de site](https://developers.google.com/analytics/devguides/collection/ga4/single-page-applications) avisa que, quando as tags são configuradas no Tag Manager, a medição automática por histórico do navegador no GA4 não deve ficar ligada, porque isso pode contar visualizações de página em dobro.

O GTM tem uma opção que ajuda a entender o problema, mas não o resolve sozinha. Segundo a [Central de Ajuda do Tag Manager](https://support.google.com/tagmanager/answer/6279951), cada tag pode disparar uma vez por evento, uma vez por página ou sem limite. Essa opção controla a repetição de uma mesma tag. Ela não impede que duas tags diferentes mandem o mesmo evento, que é justamente o caso das estruturas sobrepostas.

Num projeto de e-commerce em que atuamos, foi exatamente isso: um evento contado em dobro por estruturas de tags sobrepostas no Google Tag Manager. O diagnóstico foi confirmado no DebugView, a tela do GA4 que mostra os eventos em tempo real, e a correção foi a consolidação das tags.

## Como achar evento duplicado no Tag Assistant e no DebugView?

O caminho para achar evento duplicado é fazer a jornada de compra com o modo de visualização do GTM ligado e conferir, ao mesmo tempo, o que o GTM disparou e o que o GA4 recebeu. Segundo a [Central de Ajuda do Tag Manager](https://support.google.com/tagmanager/answer/6107056), o botão Preview abre o Tag Assistant, que mostra quais tags dispararam e em que ordem, e também o que acionou ou deixou de acionar cada uma.

O DebugView é a tela do GA4 que mostra, em tempo real, os eventos que chegam de um aparelho em modo de depuração. Segundo a [Central de Ajuda do Google Analytics](https://support.google.com/analytics/answer/7201382?hl=en), o modo de depuração pode ser ligado pelo Tag Assistant, pelo parâmetro `debug_mode` na tag ou no evento, e a tela mostra por padrão os eventos dos últimos 60 segundos, com um seletor para escolher o aparelho. A mesma página avisa que colocar `debug_mode` como falso não desliga o modo: é preciso retirar o parâmetro.

A ordem que a Ganica recomenda para essa conferência é esta:

1. **Abra o modo de visualização do GTM** e conecte a loja. Faça uma jornada completa: página de produto, carrinho, checkout e uma compra de teste.
2. **Em cada passo, conte as tags que dispararam** no Tag Assistant. Duas tags do GA4 com o mesmo nome de evento no mesmo momento são o sinal clássico de sobreposição.
3. **Confira no DebugView** se o evento aparece uma vez ou duas, com os mesmos parâmetros. O Tag Assistant mostra a intenção; o DebugView mostra o que chegou.
4. **Procure código fora do GTM.** Se o DebugView mostra um evento que nenhuma tag do contêiner disparou, existe outra instalação no tema, num aplicativo da plataforma ou em outra ferramenta.
5. **Consolide antes de criar.** Escolha uma estrutura dona de cada evento, pause as outras e repita a jornada. Só remova de vez depois de confirmar que nada parou de ser medido.

## Como conferir as compras do GA4 contra os pedidos da loja?

A conferência mais confiável das compras é cruzar o `transaction_id`, o identificador do pedido que vai junto do evento `purchase`, com a lista de pedidos pagos da loja. Assim a pergunta deixa de ser "o total bate?" e passa a ser "quais pedidos o GA4 viu, quais ele perdeu e quais ele contou a mais?".

Não é preciso BigQuery para começar. Segundo a [Central de Ajuda do Google Analytics](https://support.google.com/analytics/answer/15227167), o relatório Transações, no tópico Monetização, mostra cada transação com a dimensão ID da transação e a receita de compra. Exporte essa lista e compare com os pedidos pagos do mesmo período.

O `transaction_id` tem um papel que pouca gente conhece. Segundo a [página de e-commerce da Central de Ajuda do Google Analytics](https://support.google.com/analytics/answer/12313109?hl=en), o GA4 deduplica compras registradas com o mesmo ID de transação. A mesma página traz três regras que mudam a leitura de qualquer relatório:

- **O ID precisa ser único por pedido.** Se a tag manda o mesmo ID para compras diferentes, o Google avisa que a conta de conversões pode ficar muito abaixo do real.
- **O ID não pode ir vazio.** O GA4 deduplica todas as compras enviadas com ID vazio, o que faz várias vendas virarem uma só.
- **O ID não pode identificar o cliente.** O Google pede que ele não carregue informação capaz de identificar a pessoa. Na prática, nada de e-mail ou CPF dentro do ID.

A leitura da Ganica é que essa deduplicação protege o relatório de compras, mas não substitui a auditoria. A página do Google descreve a deduplicação para compras. Ela pede o ID em todos os eventos de e-commerce, mas não diz que eventos como adicionar ao carrinho ou iniciar o checkout são deduplicados. Por isso uma duplicidade nessas etapas pode inflar o começo do funil sem aparecer na receita.

Quem já exporta o GA4 para o BigQuery, o banco de dados de análise do Google Cloud, pode procurar IDs repetidos direto nos dados brutos. Segundo o [esquema oficial da exportação](https://support.google.com/analytics/answer/7029846), o identificador fica no campo `ecommerce.transaction_id` e cada dia ganha uma tabela `events_AAAAMMDD`, quando a exportação diária está ativada. Uma consulta curta resolve: filtrar os eventos com `event_name` igual a `purchase`, agrupar por `ecommerce.transaction_id` e listar os IDs que aparecem mais de uma vez. Cada ID repetido é um de dois erros: o mesmo pedido enviado mais de uma vez ao GA4 ou o mesmo ID usado em pedidos diferentes. A base de pedidos da loja mostra qual dos dois. Separe também as compras com ID vazio, que o GA4 trata como uma compra só, e as compras sem ID, que não têm como ser cruzadas com a loja.

O método de cruzar compra e pedido pelo ID também aparece no estudo sobre [conversão do checkout por dispositivo](/conversao-checkout-mobile-funil-por-dispositivo.html), e o guia de [integração entre PostHog, GA4 e BigQuery](/integrar-posthog-bigquery-ecommerce.html) mostra como levar a base de pedidos para o mesmo lugar.

## Que diferença entre o GA4 e a plataforma da loja é normal?

Alguma diferença entre o GA4 e a plataforma da loja é normal, porque o GA4 mede no navegador e a loja registra o pedido no servidor. O que separa diferença normal de erro é o comportamento: diferença pequena, estável e parecida entre meios de pagamento é esperada; diferença que salta de um dia para o outro, ou que só aparece num aparelho ou num meio de pagamento, é sinal de problema.

A primeira fonte de diferença é o consentimento. Segundo a [Central de Ajuda do Google Analytics](https://support.google.com/analytics/answer/11161109?hl=en), o GA4 pode estimar o comportamento de quem recusou cookies por modelagem. Para isso, o modo de consentimento precisa estar ativo em todas as páginas, com as tags do Google carregando antes do aviso de cookies e em todos os casos (a implementação avançada). A propriedade também precisa coletar pelo menos 1.000 eventos por dia com consentimento recusado, por pelo menos 7 dias, e ter pelo menos 1.000 usuários diários com consentimento aceito em 7 dos 28 dias anteriores. O dado modelado só aparece nos relatórios com a identidade de relatório Combinada. O Google diz ainda que atingir esses números não garante a modelagem, e que o dado modelado não vai para a exportação ao BigQuery.

A segunda fonte é o tempo. Segundo o [esquema da exportação](https://support.google.com/analytics/answer/7029846), o GA4 atualiza as tabelas diárias do BigQuery com eventos que chegam atrasados por até três dias, e o evento que chega depois dessa janela não entra. A [página da exportação para o BigQuery](https://support.google.com/analytics/answer/9358801) descreve a mesma janela como dois dias corridos mais o dia atual. Ela também avisa que o Google pode refazer tabelas antigas quando reprocessa dados e que os dados exportados podem diferir dos que aparecem na interface do GA4.

| Sinal na auditoria | Leitura provável |
|---|---|
| GA4 com mais compras que a loja | Disparo repetido da compra ou pedidos não pagos contados como venda |
| GA4 com menos compras, diferença estável | Consentimento recusado, bloqueio do navegador ou compra concluída fora da página de confirmação |
| Diferença que muda de um dia para o outro | Mudança recente no site, no tema ou na ferramenta de consentimento |
| Falta concentrada num meio de pagamento | Retorno de aplicativo de banco ou de página externa que não volta à confirmação |
| Etapa posterior maior que a anterior no funil | Evento repetido na etapa posterior, etapa anterior sem disparo ou relatório de funil aberto (que conta quem entrou direto numa etapa do meio) |
| Fechamento do dia muda nos dias seguintes | Eventos atrasados, ainda dentro da janela de atualização |

*Tabela: leitura da Ganica, com base na documentação oficial do Google citada no texto.*

## Qual é o checklist completo de auditoria do GA4 no e-commerce?

O checklist que a Ganica recomenda segue a ordem do barato para o caro: primeiro a configuração, depois o código.

1. **Liste o que mede o quê.** Anote cada ferramenta instalada (GA4, GTM, pixels de mídia, ferramentas de comportamento) e onde ela foi instalada: tema, contêiner ou aplicativo da plataforma.
2. **Escolha um dono para cada evento.** Para cada evento de e-commerce, uma única tag deve ser responsável. Dois donos para o mesmo evento são a receita da duplicidade.
3. **Faça a jornada em modo de visualização.** Repita em computador e celular e com todos os meios de pagamento. Inclua o caso em que o cliente paga e não volta à loja.
4. **Confira os parâmetros da compra.** O [guia de e-commerce para desenvolvedores](https://developers.google.com/analytics/devguides/collection/ga4/ecommerce) pede que cada item tenha ao menos `item_id` ou `item_name` e recomenda enviar `currency` sempre que houver `value`. Confira também se o `transaction_id` muda a cada pedido e nunca vai vazio.
5. **Cruze compra e pedido pelo ID** por uma ou duas semanas, separando por aparelho e por meio de pagamento.
6. **Teste com o consentimento aceito e recusado.** Veja o que deixa de ser enviado quando o visitante recusa, e confira se é isso que a política da loja promete.
7. **Feche o número do dia com atraso.** Não compare o dia de ontem antes de a janela de eventos atrasados terminar.
8. **Registre cada correção com data.** Uma anotação simples evita que a equipe compare um mês medido errado com um mês medido certo.

Na conferência de pedidos entra dado pessoal. A Lei Geral de Proteção de Dados define dado pessoal como informação relacionada a pessoa natural identificada ou identificável e pede que o tratamento se limite ao mínimo necessário para a finalidade (arts. 5º e 6º da [Lei 13.709/2018](https://www2.camara.leg.br/legin/fed/lei/2018/lei-13709-14-agosto-2018-787077-publicacaooriginal-156212-pl.html)). A recomendação da Ganica é cruzar só o ID do pedido, a data, o valor e o meio de pagamento, sem nome, e-mail ou documento. Mesmo assim, esses dados podem continuar sendo dado pessoal, porque a loja consegue ligar o ID ao cliente. Por isso, deixe o arquivo com acesso restrito e apague-o ao fim da conferência. Este guia não é orientação jurídica.

A auditoria é o primeiro passo de um [diagnóstico de CRO](/#diagnostico) (otimização da taxa de conversão), e o guia sobre [taxa de conversão do e-commerce](/taxa-de-conversao-ecommerce.html) mostra o que fazer depois que o dado está confiável.

## O que ainda não sabemos

Não encontramos, na documentação do Google, um número oficial de quanto o GA4 e a plataforma da loja podem divergir. A diferença aceitável depende da parcela de visitantes que recusa cookies, do uso de bloqueadores, do peso de cada meio de pagamento e de como a loja confirma o pedido. Por isso este guia fala em diferença estável, e não em uma porcentagem.

Também não há, na documentação consultada, uma descrição de deduplicação para eventos além da compra. A leitura da Ganica é tratar qualquer repetição nas etapas do funil como erro a corrigir na origem, e não como algo que o GA4 resolve sozinho.

Este guia reúne um caso e a documentação oficial do Google, consultada em novembro de 2026. Ele não mede ganho de conversão: mede se o número que orienta a decisão é confiável.
