---
title: "A taxa de conversão só caía, e o problema não era o site: era o tráfego"
seo_title: "Taxa de conversão não sobe? Às vezes o problema é a mídia"
og_title: "Taxa de conversão não sobe? Um caso em que o problema era a mídia, não o site"
description: "Taxa de conversão não sobe mesmo mudando o site? Veja um caso em que campanhas de engajamento e leads diluíram a conversão, e como separar o tráfego no GA4."
twitter_description: "O site mudou várias vezes e a conversão só caía. O problema era o tráfego de campanhas de engajamento e leads. Como enxergar isso no GA4 antes de mexer na página."
slug: taxa-de-conversao-nao-sobe-trafego-desqualificado
date: '2026-11-16'
hora: "06:45"
updated: '2026-11-16'
rascunho: false
usa_dado_cliente: true
breadcrumb: Taxa de conversão e mídia paga
secao: E-commerce
card_kicker: "Case · Mídia e CRO"
card_destaque: "Mais visitas sem intenção de compra derrubam a taxa média"
card_titulo: "A taxa de conversão só caía, e o problema não era o site."
card_resumo: "Num diagnóstico da Ganica em um e-commerce brasileiro, as mudanças no site não seguravam a conversão. A causa estava nas campanhas de engajamento e de leads. Mostramos como separar o tráfego no GA4 antes de mexer na página."
tags_artigo:
  - CRO
  - mídia paga
  - taxa de conversão
  - GA4
keywords:
  - taxa de conversão não sobe
  - tráfego desqualificado
  - mídia paga e CRO
  - objetivo de campanha
  - taxa de conversão por campanha
sobre:
  - Otimização de conversão (CRO)
  - Mídia paga
  - Google Analytics 4
imagem_og: ''
resposta_curta: "Se a taxa de conversão não sobe mesmo depois de mudar o site, olhe primeiro para o tráfego. Campanhas de engajamento e de captação de leads são otimizadas para curtidas, cliques ou cadastros, não para compras, e tendem a levar ao site muitos visitantes sem intenção de comprar. A taxa média cai sem o site piorar. Separe a conversão por campanha no GA4 antes de mexer na página."
deck: "Num diagnóstico da Ganica em um e-commerce brasileiro, a conversão continuava caindo apesar das mudanças no site. O problema estava na mídia: campanhas com outro objetivo levavam ao site gente que não vinha para comprar. Este estudo mostra como enxergar isso e como alinhar mídia e CRO."
resumo:
  - "Num diagnóstico da Ganica em um e-commerce brasileiro, a taxa de conversão **continuou caindo** depois de várias mudanças no site. A causa não estava na página: estava no **tráfego** que chegava."
  - "A mídia paga tinha ativado campanhas de **engajamento** e de **captação de leads**. Na documentação da Meta, cada meta de otimização busca pessoas mais propensas à ação pedida: engajar com o post, preencher um formulário ou converter no site."
  - "Em exemplo hipotético, somar **50 mil** visitas que quase não compram a uma loja com **50 mil** visitas convertendo **2%** derruba a taxa média para cerca de **1%**, mesmo com **mais pedidos**."
  - "No GA4, a taxa de conversão por campanha sai das dimensões de sessão (campanha, origem e mídia) cruzadas com compras e com a taxa de engajamento."
  - "A correção não é desligar campanhas de marca ou de leads: é **nomear campanhas por objetivo**, separar o relatório de CRO por tráfego com intenção de compra e combinar metas entre mídia e CRO."
faq:
  - pergunta: "Campanha de engajamento é dinheiro jogado fora?"
    resposta: "Não necessariamente. Engajamento e captação de leads têm papel em construir público e lista de contatos. O problema é medir essas campanhas pela taxa de conversão do site, que não é o que elas foram feitas para entregar, e misturar esse tráfego no mesmo número que avalia o site."
  - pergunta: "Qual objetivo de campanha usar para vender no e-commerce?"
    resposta: "Para venda direta, o objetivo deve ser o de vendas ou conversões no site, com o evento de compra configurado como meta. Na Meta, a otimização para conversões no site busca pessoas mais propensas a converter; no Google Ads, a Central de Ajuda indica os Lances inteligentes (como Maximizar conversões, CPA desejado e ROAS desejado) quando o objetivo é uma ação no site. Confira com a equipe de mídia qual evento cada campanha está otimizando."
  - pergunta: "O lead de uma campanha de captação compra depois?"
    resposta: "Pode comprar, mas em outro tempo. Por isso o lead deve ser medido numa janela própria, por exemplo quantos compram em 30 ou 60 dias depois do cadastro, e não pela compra na primeira visita. Essa medição exige cruzar a lista de leads com os pedidos da loja, usando só os dados necessários, como manda a LGPD."
  - pergunta: "Como saber se a queda de conversão é do site ou do tráfego?"
    resposta: "Compare a taxa de conversão de um grupo de tráfego estável, como busca orgânica ou campanhas de venda, antes e depois da queda. Se esse grupo se manteve e a média caiu, o problema é a mistura do tráfego. Se o grupo estável também caiu, aí vale investigar o site."
fontes: "Caso: diagnóstico da Ganica num e-commerce brasileiro, apresentado só de forma qualitativa e sem números do cliente. Meta for Developers, referência da API de marketing (campo de objetivo de otimização do conjunto de anúncios e página do objeto promovido), consultada em novembro de 2026. Central de Ajuda do Google Ads, página sobre como escolher a estratégia de lances pelo objetivo, consultada em novembro de 2026. Central de Ajuda do Google Analytics, páginas sobre dimensões e métricas e sobre dimensões de origem de tráfego, e referência da API de dados do GA4, consultadas em novembro de 2026. O exemplo de diluição da taxa é hipotético, com números ilustrativos."
fontes_urls:
  - "Data API schema, Google Analytics Data API (Google) | https://developers.google.com/analytics/devguides/reporting/data/v1/api-schema"
  - "Ad Set, referência da API de marketing (Meta for Developers) | https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign"
  - "Determine a bid strategy based on your goals, Central de Ajuda do Google Ads (Google) | https://support.google.com/google-ads/answer/2472725?hl=en"
  - "Dimensões e métricas do Analytics, Central de Ajuda do Google Analytics (Google) | https://support.google.com/analytics/answer/9143382"
  - "Ad Set, Promoted Object, referência da API de marketing (Meta for Developers) | https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-promoted-object"
  - "Lei Geral de Proteção de Dados Pessoais, Lei 13.709/2018 (Planalto) | https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm"
  - "Escopos das dimensões de origem de tráfego, Central de Ajuda do Google Analytics (Google) | https://support.google.com/analytics/answer/11080067"
cta_titulo: "A sua taxa de conversão está medindo o site ou a mistura da mídia?"
cta_texto: "Um diagnóstico de CRO separa o tráfego por objetivo de campanha, mostra a conversão de quem veio para comprar e diz se o problema está na página ou na mídia."
autor_texto: "Sou consultor de CRO focado em e-commerce, com trabalho direto em estrutura de analytics (GTM, GA4, Looker Studio) e auditoria comportamental. Aprendi neste caso que, antes de mexer no site, é preciso perguntar à mídia o que mudou no tráfego."
---

## Por que a taxa de conversão não sobe mesmo depois de mudar o site?

A taxa de conversão não sobe, e às vezes até cai, depois de mudanças no site porque o problema pode não estar na página, e sim em quem chega até ela. A taxa de conversão é a parte das visitas que termina em compra. Se a loja passa a receber muitas visitas de pessoas que não vieram para comprar, a taxa média cai, mesmo que o site esteja igual ou melhor.

Esse é um erro comum no e-commerce: mídia paga e CRO trabalham separados. CRO (otimização da taxa de conversão) é o trabalho de descobrir por que os visitantes não compram e corrigir isso. Quando a equipe de CRO não sabe o que a mídia mudou, ela investiga a página, testa mudanças e mede o resultado num número que está sendo puxado para baixo por outra causa.

## O que aconteceu neste caso?

Num diagnóstico da Ganica em um e-commerce brasileiro, a taxa de conversão era um desafio, e o trabalho começou pelas páginas. Foram feitas diversas mudanças no site, e a taxa, em vez de subir, continuava caindo.

Quando paramos para analisar o tráfego que chegava, a resposta apareceu. A equipe de mídia paga tinha ativado campanhas de engajamento e campanhas de captação de leads (cadastros de contato) que levavam tráfego para o site. Esse tráfego quase não comprava, e o volume dele era grande o bastante para puxar para baixo a taxa média da loja.

O problema não estava no site. A mistura do tráfego estava mudando, e era isso que puxava a taxa para baixo. É um padrão que encontramos com frequência em diagnósticos: campanhas com objetivo de engajamento ou de leads levam ao site muita gente sem intenção de comprar, e o trabalho de CRO parece não funcionar, mesmo quando a conversão do público que veio para comprar está estável ou melhorando.

## Por que campanhas de engajamento e de leads derrubam a taxa de conversão?

Campanhas de engajamento e de leads derrubam a taxa de conversão porque as plataformas de anúncio procuram o público mais propenso à ação pedida, e essa ação não é a compra. Quando esses anúncios levam ao site, chegam visitas de quem engaja ou se cadastra, não de quem veio comprar. Na [referência da API de marketing da Meta](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign), cada meta de otimização do conjunto de anúncios diz para quem o anúncio será entregue.

Com engajamento, o alvo é quem tende a interagir com o post. Com geração de leads, quem tende a preencher um formulário (em geral, dentro da própria Meta; quando o cadastro é no site, a campanha usa a conversão no site com um evento de cadastro). Com cliques no link, quem tende a clicar. Com conversões no site, o alvo é quem tende a fazer no site o evento escolhido pelo anunciante, e esse evento, definido no [objeto promovido do conjunto de anúncios](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-promoted-object), pode ser a compra (Purchase) ou um cadastro (Lead ou CompleteRegistration).

Por isso, uma campanha de leads otimizada para o evento de cadastro também traz quem se cadastra, não quem compra. Para vender, a meta precisa ser o evento de compra (ou o valor da compra).

No Google Ads, a lógica é a mesma. A [Central de Ajuda do Google Ads](https://support.google.com/google-ads/answer/2472725?hl=en) orienta escolher a estratégia de lance pelo objetivo: lance por cliques para gerar tráfego, por impressões para reconhecimento de marca e estratégias de conversão quando o objetivo é uma ação direta no site.

Ou seja, a campanha de engajamento cumpre o que promete: encontra quem curte, comenta e clica. Só que essa pessoa, ao chegar ao site, não está no momento de comprar. A plataforma não errou; o erro é avaliar o site com um número que mistura esse público com o público de compra. Para saber o que cada campanha está otimizando, peça à equipe de mídia a meta de desempenho e o evento de conversão de cada conjunto ou grupo de anúncios, e não só o nome da campanha.

## Como o tráfego desqualificado esconde o problema na média?

O tráfego desqualificado esconde o problema porque a média soma grupos de tráfego com intenções muito diferentes num número só. Veja um exemplo hipotético, com números ilustrativos. Uma loja recebe 50 mil visitas por mês, de busca orgânica, campanhas de venda e acesso direto, e converte 2%, ou 1.000 pedidos. A mídia passa a rodar campanhas de engajamento e leads que trazem mais 50 mil visitas, das quais saem só 50 pedidos (1 a cada 1.000 visitas).

| Cenário hipotético | Taxa de conversão da loja |
|---|---|
| Antes: 50 mil visitas e 1.000 pedidos | 2% |
| Depois: 100 mil visitas e 1.050 pedidos | cerca de 1% |
| Só o tráfego com intenção de compra, depois: 50 mil visitas e 1.000 pedidos | 2% |

*Exemplo hipotético da Ganica, com números ilustrativos. Não representa os números do caso nem de nenhuma loja real.*

A loja vendeu mais, e a taxa caiu quase pela metade. Quem olha só a média conclui que o site piorou e começa a mexer em páginas que estão funcionando. Pior: se uma mudança no site entra no ar na mesma semana em que as campanhas começam, ela leva a culpa pela queda.

> Antes de perguntar o que mudou no site, pergunte o que mudou no tráfego.

## Como enxergar a conversão por campanha no GA4?

Para enxergar a conversão por campanha no GA4 (Google Analytics 4, a ferramenta de medição do Google), cruze as dimensões de sessão de origem do tráfego com compras e com sinais de engajamento. As [dimensões de origem de tráfego do GA4](https://support.google.com/analytics/answer/11080067) com escopo de sessão (em inglês, as que começam com "Session"; no GA4 em português, as que terminam em "da sessão", como Origem da sessão) mostram de onde veio cada visita, e aparecem no relatório de aquisição de tráfego.

Numa exploração livre, coloque a campanha da sessão e a origem/mídia da sessão nas linhas e acrescente as métricas abaixo (no relatório Aquisição de tráfego, use uma como dimensão principal e a outra como secundária, e personalize o relatório para incluir as métricas de compra e carrinho). As definições estão na [página de dimensões e métricas do GA4](https://support.google.com/analytics/answer/9143382) e na [referência de métricas da API de dados do GA4](https://developers.google.com/analytics/devguides/reporting/data/v1/api-schema):

- **Sessões**, para ver o peso de cada campanha no total.
- **Compras de e-commerce** (Ecommerce purchases) e a taxa de eventos principais da sessão (Session key event rate, na documentação do Google: a parte das sessões em que aconteceu algum evento principal). Essa taxa conta qualquer evento principal: se o cadastro de lead também estiver marcado como evento principal, as campanhas de leads vão parecer converter bem. Para ver só a compra, divida as Compras de e-commerce pelas Sessões de cada campanha: é uma taxa aproximada de compra por sessão, boa para comparar campanhas entre si.
- **Taxa de engajamento** (Engagement rate), que é a parte das sessões engajadas: as que duraram 10 segundos ou mais, tiveram um evento principal ou duas ou mais visualizações de página.
- **Adições ao carrinho** (Add to carts), para ver se o visitante ao menos começou a comprar.

O sinal de tráfego desqualificado (visitas sem intenção de compra) é claro: muitas sessões, poucas adições ao carrinho, quase nenhuma compra e engajamento baixo. Para esse corte funcionar, as campanhas precisam chegar com parâmetros de campanha (UTMs) bem preenchidos. Antes de comparar campanhas, confira também se o GA4 conta cada compra uma vez só, como mostra o estudo de [auditoria de rastreamento no GA4](/auditoria-rastreamento-ga4-gtm-ecommerce.html).

O teste que separa site de mídia é simples: compare, antes e depois da queda, a conversão de um grupo de tráfego estável, como busca orgânica ou campanhas de venda. Se esse grupo se manteve e a média caiu, a queda vem da mistura do tráfego, não do site.

## O que fazer para mídia e CRO trabalharem juntos?

Para mídia e CRO trabalharem juntos, a loja precisa de um combinado simples sobre objetivos, nomes e números. O caminho que a Ganica recomenda:

1. **Nomeie cada campanha pelo objetivo.** Inclua o objetivo no nome e nas UTMs (por exemplo, "venda", "engajamento", "leads"), para que qualquer pessoa separe o tráfego no GA4 sem perguntar.
2. **Separe o relatório de CRO.** Acompanhe à parte a taxa de conversão do tráfego com intenção de compra, em geral busca orgânica, acesso direto e campanhas de venda. Confira na sua loja: o orgânico de blog, por exemplo, também costuma ter pouca intenção de compra. Assim, a meta de conversão do CRO não sobe e desce junto com a verba de mídia.
3. **Avise antes de mudar.** Toda campanha nova ou mudança grande de verba entra numa agenda compartilhada, com data. Assim, ninguém atribui ao site uma queda que veio da mídia, nem o contrário.
4. **Meça cada campanha pelo que ela promete.** Engajamento se mede por alcance e interação; lead, por custo do cadastro e por quantos compram depois; venda, por pedidos e receita.
5. **Leve o lead para uma régua de nutrição e dê a ele uma janela própria.** Cruze a lista de leads com os pedidos e veja quantos compram em 30 ou 60 dias, em vez de cobrar compra na primeira visita. Esse cruzamento usa dado pessoal: pelo princípio da necessidade da [LGPD (art. 6º, III, da Lei 13.709/2018)](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm), limite-o ao necessário (por exemplo, um identificador do contato e a data do pedido) e restrinja o acesso ao arquivo.
6. **Teste o site só com o tráfego certo.** Num teste A/B (mostrar duas versões da página, ao mesmo tempo, a grupos sorteados de visitantes), as duas versões recebem a mesma mistura de tráfego, e a comparação continua justa. Mas um grande volume de visitas sem intenção de compra dilui a diferença e exige mais tempo de teste, e a comparação de antes e depois, sem grupo de controle, fica contaminada pela mudança na mídia. Leia o resultado também só com o tráfego com intenção de compra e prefira o teste com sorteio a comparar períodos.

Para entender como essa leitura se encaixa na análise geral da loja, o estudo sobre [taxa de conversão do e-commerce](/taxa-de-conversao-ecommerce.html) mostra como abrir a taxa por etapa, canal e tipo de cliente, e o estudo sobre [investir em CRO](/investir-em-cro-ecommerce.html) mostra por que a conversão muda o custo de cada pedido de mídia.

## O que ainda não sabemos

Não sabemos quanto do público de engajamento e de leads compra depois, em outra visita ou outro aparelho. Parte dessa venda pode aparecer mais tarde, atribuída a outro canal, e a atribuição (a regra que decide qual canal recebe o crédito da venda) nunca é perfeita. Por isso este estudo não diz que essas campanhas não vendem: diz que elas não devem entrar na mesma conta que avalia o site.

O caso é de uma loja, e os números da tabela são hipotéticos. A proporção entre os grupos de tráfego muda de loja para loja, e o efeito na taxa média depende dela. O que vale para qualquer loja é a ordem: separar o tráfego antes de concluir que o site piorou. Se a sua taxa de conversão está caindo e as mudanças no site não resolvem, esse é um dos pontos que um [diagnóstico de CRO](/#diagnostico) confere primeiro.
