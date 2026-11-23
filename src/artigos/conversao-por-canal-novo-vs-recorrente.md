---
title: "Taxa de conversão por canal: o ranking muda quando você separa novos de recorrentes"
seo_title: "Taxa de conversão por canal: separe novos de recorrentes"
og_title: "Taxa de conversão por canal: o ranking muda ao separar novos de recorrentes"
description: "A taxa de conversão por canal engana quando mistura quem chega pela primeira vez e quem já conhece a loja. Separe os dois no GA4 antes de decidir a verba."
twitter_description: "O canal campeão costuma ser o que tem mais cliente antigo. Como separar novos de recorrentes por canal no GA4 e o que isso muda na decisão de verba."
slug: conversao-por-canal-novo-vs-recorrente
date: '2026-11-23'
hora: "07:40"
updated: '2026-11-23'
rascunho: false
usa_dado_cliente: true
breadcrumb: Conversão por canal
secao: E-commerce
card_kicker: "CRO · Aquisição"
card_destaque: "O canal campeão costuma ter mais cliente antigo"
card_titulo: "A taxa de conversão por canal engana quem decide verba."
card_resumo: "A média de um canal soma quem nunca esteve na loja e quem já é cliente. Em análise da Ganica de um e-commerce brasileiro, o ranking de canais mudou ao separar os dois. Veja como fazer esse corte no GA4."
tags_artigo:
  - CRO
  - GA4
  - aquisição
  - taxa de conversão
keywords:
  - taxa de conversão por canal
  - conversão de usuário novo por canal
  - usuário recorrente GA4
  - conversão por canal e-commerce
  - decisão de verba de mídia
sobre:
  - Otimização de conversão (CRO)
  - Google Analytics 4
  - Mídia paga
imagem_og: ''
resposta_curta: "A taxa de conversão por canal engana porque a média de cada canal soma dois públicos opostos: quem chega ao site pela primeira vez e quem já esteve nele antes. Canais que falam com a base, como e-mail, costumam aparecer no topo pelo público que carregam, não pelo trabalho que fazem. Separe novos de recorrentes dentro de cada canal no GA4 antes de mover verba."
deck: "O ranking de canais que orienta a verba quase sempre mistura visitante novo e cliente antigo. Este estudo mostra como separar os dois no GA4, o que o corte revela e onde ele tem limite."
resumo:
  - "A taxa de conversão de um canal é uma média de dois públicos opostos. Segundo a Central de Ajuda do Google Analytics, o GA4 chama de recorrente quem **já iniciou ao menos uma sessão anterior**."
  - "Em análise da Ganica de um e-commerce brasileiro, em visitas de redes sociais pelo celular a conversão de quem já conhecia a loja foi **dezenas de vezes maior** que a de quem chegava pela primeira vez."
  - "O canal campeão do ranking muitas vezes só tem **público mais recorrente** que os outros: comparado entre públicos iguais, perde parte da vantagem. É um padrão que encontramos com frequência em diagnósticos."
  - "O corte sai do próprio GA4, com a dimensão de **novo e recorrente** e as dimensões de canal com escopo de sessão e de primeiro usuário."
  - "O limite é real: o GA4 identifica o visitante pelo navegador, e o Safari limita a **sete dias** a validade do cookie criado por script, segundo o blog da WebKit (Apple)."
faq:
  - pergunta: "Dá para ver novo e recorrente nos relatórios padrão do GA4, sem montar exploração?"
    resposta: "Dá, de forma parcial. Os relatórios padrão aceitam comparações, que mostram subconjuntos dos dados lado a lado, e isso já serve para uma primeira olhada no relatório de aquisição de tráfego. Para cruzar canal, público e compras com liberdade, a exploração livre é o caminho."
  - pergunta: "Usuário recorrente é a mesma coisa que cliente que já comprou?"
    resposta: "Não. Recorrente é quem já visitou o site antes, mesmo sem nunca ter comprado. Para separar quem já comprou, o GA4 tem as métricas de primeiros compradores e de total de compradores, que contam usuários com evento de compra. Em muitas lojas, vale olhar os dois cortes."
  - pergunta: "Devo cortar um canal com conversão baixa de visitante novo?"
    resposta: "Depende do papel do canal. Um canal de topo de funil costuma mesmo converter pouco na primeira visita e aparecer depois na conversão de outro canal. Antes de cortar, compare a conversão de novos entre canais semelhantes e veja quanto cada um alimenta a base que volta."
  - pergunta: "Esse corte vale para uma loja com pouco tráfego?"
    resposta: "Vale, com cuidado. Com pouco volume, cada canal fica com poucas compras por grupo e a comparação oscila muito de semana para semana. Nesses casos, use períodos mais longos e trate a diferença como indício, não como conclusão."
fontes: "Caso: análise da Ganica de um e-commerce brasileiro, ao longo de alguns meses de 2026, apresentada só com números relativos e arredondados. Central de Ajuda do Google Analytics: páginas de dimensões e métricas, de grupo de canais padrão, de criação de segmentos, de comparações nos relatórios, de User-ID e de identidade dos relatórios, e referência da API de dados do GA4, consultadas em novembro de 2026. Documentação do Google para tags sobre configuração de cookies, consultada em novembro de 2026. Blog da WebKit (Apple) sobre prevenção inteligente de rastreamento, publicado em 2020. Central de Ajuda do Google Ads sobre metas de ciclo de vida do cliente, consultada em novembro de 2026. Lei 13.709/2018 (LGPD); este estudo não é orientação jurídica. Pesquisa da CNDL e do SPC Brasil com a Offerwise Pesquisas, quantitativa pela web, pós-ponderada por sexo, idade, estado e renda, com compradores digitais das capitais de 18 anos ou mais (campo entre 25 de maio e 4 de junho de 2026; 939 contatos na primeira etapa e 800 respondentes no questionário completo; margens de erro de 3,2 e 3,5 pontos percentuais, a 95% de confiança), divulgada pela CNDL e noticiada pelo E-Commerce Brasil em setembro de 2026, consultadas em novembro de 2026. Não conferimos o relatório completo com as tabelas da pesquisa."
fontes_urls:
  - "Dimensões e métricas do Analytics (Central de Ajuda do Google Analytics) | https://support.google.com/analytics/answer/9143382"
  - "Grupo de canais padrão e escopo das dimensões de origem (Central de Ajuda do Google Analytics) | https://support.google.com/analytics/answer/9756891?hl=en"
  - "Criador de segmentos das explorações (Central de Ajuda do Google Analytics) | https://support.google.com/analytics/answer/9304353?hl=en"
  - "Aplicar comparações aos relatórios (Central de Ajuda do Google Analytics) | https://support.google.com/analytics/answer/9269518?hl=en"
  - "User-ID no GA4 (Central de Ajuda do Google Analytics) | https://support.google.com/analytics/answer/9355972"
  - "Identidade dos relatórios (Central de Ajuda do Google Analytics) | https://support.google.com/analytics/answer/10976610"
  - "Esquema da API de dados do GA4 (Google for Developers) | https://developers.google.com/analytics/devguides/reporting/data/v1/api-schema"
  - "Configurar e personalizar cookies (Google for Developers) | https://developers.google.com/tag-platform/security/guides/customize-cookies"
  - "Full Third-Party Cookie Blocking and More (WebKit, Apple) | https://webkit.org/blog/10218/full-third-party-cookie-blocking-and-more/"
  - "Metas de ciclo de vida do cliente (Central de Ajuda do Google Ads) | https://support.google.com/google-ads/answer/12080169"
  - "Lei Geral de Proteção de Dados Pessoais, Lei 13.709/2018 (Planalto) | https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm"
  - "Consumo online levou 139 milhões de consumidores às compras, pesquisa CNDL/SPC Brasil (CNDL) | https://cndl.org.br/varejosa/com-recorde-historico-consumo-online-levou-139-milhoes-de-consumidores-as-compras-na-internet-no-ultimo-ano-aponta-pesquisa-cndl-spc-brasil/"
  - "Brasil ganha 20 milhões de consumidores digitais em um ano, diz SPC (E-Commerce Brasil) | https://www.ecommercebrasil.com.br/noticias/brasil-ganha-20-milhoes-de-consumidores-digitais-em-um-ano-diz-spc"
cta_titulo: "O seu relatório de canais está medindo o canal ou o público dele?"
cta_texto: "Um diagnóstico de CRO separa visitante novo de cliente antigo dentro de cada canal e mostra onde a verba está sendo decidida pelo número errado."
autor_texto: "Sou consultor de CRO focado em e-commerce, com trabalho direto em estrutura de analytics (GTM, GA4, Looker Studio) e auditoria comportamental. O corte entre novo e recorrente é um dos primeiros que faço num diagnóstico de canais."
---

## Por que a taxa de conversão por canal engana?

A taxa de conversão por canal engana porque cada canal entrega ao site uma mistura diferente de dois públicos opostos: quem nunca esteve na loja e quem já esteve. Esses grupos parecem com a divisão entre quem nunca comprou e quem já comprou, mas não são a mesma coisa: o GA4 (Google Analytics 4, a ferramenta de medição do Google) conta a visita, não a compra. E a taxa de conversão, que é a parte das visitas que termina em compra, sobe quando o canal traz gente que já conhece a loja, sem que ele tenha feito nada de especial.

É o caso do e-mail e das mensagens para a base, que falam na maior parte com quem já esteve na loja. O ranking premia esse canal e castiga o que traz gente nova, que é o trabalho que costuma custar mais caro por venda.

Voltar à mesma loja é comum no Brasil. Segundo pesquisa da [CNDL e do SPC Brasil com a Offerwise Pesquisas](https://cndl.org.br/varejosa/com-recorde-historico-consumo-online-levou-139-milhoes-de-consumidores-as-compras-na-internet-no-ultimo-ano-aponta-pesquisa-cndl-spc-brasil/), 95% dos compradores ouvidos já compraram de novo no mesmo site ou aplicativo. O campo foi feito entre 25 de maio e 4 de junho de 2026, com 800 compradores digitais das capitais e margem de erro de 3,5 pontos percentuais; o resultado também foi [noticiado pelo E-Commerce Brasil](https://www.ecommercebrasil.com.br/noticias/brasil-ganha-20-milhoes-de-consumidores-digitais-em-um-ano-diz-spc). Se a recompra é comum, é grande a chance de a sua loja ter os dois públicos em quase todo canal, e eles não se comportam igual.

## O que o GA4 chama de usuário novo e de recorrente?

No GA4, os rótulos falam de visita anterior, não de compra anterior. Segundo a [Central de Ajuda do Google Analytics](https://support.google.com/analytics/answer/9143382), a métrica de usuários recorrentes conta quem já iniciou ao menos uma sessão anterior, engajada ou não, e a de novos usuários conta os identificadores que registraram o primeiro acesso, pelo evento `first_visit` no site ou `first_open` no aplicativo. A dimensão que separa os dois aparece no [esquema da API de dados do GA4](https://developers.google.com/analytics/devguides/reporting/data/v1/api-schema) como `newVsReturning`, pelo mesmo critério: a contagem de sessões anteriores.

Na prática, "recorrente" no GA4 inclui o curioso que voltou três vezes e nunca comprou. Para olhar cliente de verdade, a mesma página traz as métricas de compra: primeiros compradores, os usuários que fizeram a primeira compra no período, e total de compradores, os usuários únicos com ao menos uma compra.

Cada corte responde a uma pergunta:

| O que você quer saber | O corte do GA4 que responde |
|---|---|
| O canal traz gente que nunca esteve no site? | Novo e recorrente (sessões anteriores) |
| O canal traz gente que nunca comprou? | Primeiros compradores e total de compradores |
| O canal foi a porta de entrada da pessoa? | Grupo de canais padrão do primeiro usuário |
| O canal trouxe esta visita? | Grupo de canais padrão da sessão |

*Definições das dimensões e métricas na Central de Ajuda do Google Analytics, consultada em novembro de 2026.*

A diferença entre os dois últimos está no escopo, ou seja, no que a dimensão descreve. Na [página de grupo de canais padrão](https://support.google.com/analytics/answer/9756891?hl=en), o grupo de canais da sessão é aquele pelo qual o usuário chegou ao iniciar uma nova sessão, e o do primeiro usuário, aquele pelo qual ele chegou ao site pela primeira vez. Um conta a visita, o outro a origem da pessoa, e confundir os dois é o erro mais comum nessa análise.

## Como separar novos de recorrentes por canal no GA4?

Para separar novos de recorrentes por canal no GA4, use uma exploração no formato livre, que é a tela de Explorar em que você monta a sua própria tabela, com a dimensão de novo e recorrente e as dimensões de canal com o escopo certo. Segundo a [página do criador de segmentos](https://support.google.com/analytics/answer/9304353?hl=en), segmento de usuário é um subconjunto de usuários e segmento de sessão, um subconjunto das sessões; dá para criar até dez segmentos por exploração e aplicar até quatro de cada vez numa mesma técnica.

A recomendação da Ganica para separar novo de recorrente por canal:

1. **Confira o rastreamento.** Compra contada duas vezes derruba qualquer comparação; o estudo de [auditoria de rastreamento no GA4](/auditoria-rastreamento-ga4-gtm-ecommerce.html) traz o checklist.
2. **Separe os dois grupos pela dimensão de novo e recorrente.** Segundo o esquema da API de dados do GA4, o usuário novo tem zero sessões anteriores e o recorrente tem uma ou mais. Como a mesma pessoa é nova na primeira visita e recorrente depois, use a dimensão para detalhar as linhas da tabela, ou monte segmentos de sessão: segmento de usuário, que pela Central de Ajuda é um subconjunto de usuários, colocaria a mesma pessoa nos dois grupos.
3. **Coloque o canal nas linhas**, com o grupo de canais padrão da sessão, que diz qual canal trouxe aquela visita.
4. **Escolha as métricas.** Sessões e compras de e-commerce. Para a taxa, marque a compra como evento principal (o nome que o GA4 dá ao evento contado como resultado) e use a taxa de eventos principais **daquele evento**: segundo o esquema da API de dados do GA4, a métrica geral mede a parte das sessões com algum evento principal, e por isso mistura compra com carrinho e cadastro.
5. **Compare dentro de cada canal e, entre canais, grupo contra grupo**: novo contra novo, recorrente contra recorrente. O que não serve é comparar a média de um canal com a média de outro.
6. **Repita com o grupo de canais do primeiro usuário**, para ver quais canais trazem gente nova, mesmo quando a compra aparece depois em outro canal.
7. **Use um período longo**: com poucas compras por grupo, a diferença de uma semana é ruído.

Quem não quer montar exploração tem um atalho: segundo a [Central de Ajuda do Google Analytics](https://support.google.com/analytics/answer/9269518?hl=en), os relatórios aceitam comparações, que mostram subconjuntos dos dados lado a lado.

## O que muda no ranking de canais quando você isola os recorrentes?

O que muda é a ordem, e às vezes o canal campeão. Em análise da Ganica de um e-commerce brasileiro, em 2026, nas visitas de redes sociais pelo celular a conversão de quem já conhecia a loja foi dezenas de vezes maior que a de quem chegava pela primeira vez. É o tipo de distância que a média de um canal apaga.

O cookie contamina essa medida nos dois sentidos. Quem volta e perdeu o cookie entra no grupo dos novos e puxa a conversão desse grupo para cima, encurtando a distância; no mesmo movimento, sai da conta dos recorrentes, que ficam só com quem voltou dentro da validade do cookie, o que alarga a distância. Como não dá para separar os dois efeitos, a leitura honesta é a ordem de grandeza, não o múltiplo exato.

O mesmo corte explica por que o canal que fala com a base, em geral o e-mail, costuma aparecer no topo. É um padrão que encontramos com frequência em diagnósticos: o canal campeão muitas vezes só tem público mais recorrente que os outros, e comparado entre públicos iguais perde parte da vantagem. O que o destacava era o público, não o trabalho do canal.

> O canal não converte. As pessoas que ele traz convertem. Se o relatório não separa as pessoas, ele não está medindo o canal.

Nos diagnósticos, a conta que mais surpreende quem decide verba é esta: dentro do mesmo canal, a distância entre quem chega pela primeira vez e quem já conhece a loja costuma ser maior que a distância entre um canal e outro. O risco é direto: a loja vê redes sociais ou prospecção com conversão baixa na média e corta a verba, cortando junto a entrada de gente nova. Se ninguém alimenta a base, o canal que vive dela tende a cair depois, o que é hipótese, não medição deste caso.

## Por que esse corte não é perfeito, e o que fazer a respeito?

O corte não é perfeito porque o GA4 reconhece o navegador, não a pessoa. A [documentação do Google para tags](https://developers.google.com/tag-platform/security/guides/customize-cookies) explica que o prazo do cookie é renovado a cada carregamento de página e que, se ele expirar entre dois acessos, a primeira e a segunda visita aparecem como visitantes distintos. Trocar de aparelho, usar aba privada ou limpar os dados do navegador dá no mesmo.

Em Safari, o prazo é curto por decisão do navegador. No blog da [WebKit](https://webkit.org/blog/10218/full-third-party-cookie-blocking-and-more/), a Apple lembra que anunciou em fevereiro de 2019 que a prevenção inteligente de rastreamento passaria a limitar a sete dias a validade dos cookies criados pelo próprio site via script, e descreve a regra que apaga o armazenamento criado por script depois de sete dias de uso do navegador sem interação com o site. O limite vale para o cookie criado por script, que é como a tag do Google escreve o cookie quando a medição roda só no navegador. Numa loja com muito tráfego de iPhone, onde todo navegador usa o WebKit, parte do público recorrente reaparece como novo.

Dá para melhorar a medição dentro do que a loja controla:

1. **Ligue o User-ID se você tem área logada.** Segundo a [Central de Ajuda do Google Analytics](https://support.google.com/analytics/answer/9355972), ele permite associar identificadores próprios a usuários e conectar o comportamento deles entre sessões, aparelhos e plataformas. Pela [LGPD (art. 5º, I, da Lei 13.709/2018)](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm), dado pessoal é a informação ligada a pessoa identificada ou identificável, e um código que a loja liga ao cliente entra nessa conta: base legal, aviso de privacidade e o que vai para cada ferramenta precisam estar resolvidos antes. A recomendação da Ganica é enviar um código interno, nunca e-mail, CPF ou telefone.
2. **Confira a identidade dos relatórios.** Na [página sobre identidade dos relatórios](https://support.google.com/analytics/answer/10976610), as opções são mesclada, observada e baseada em dispositivo; nas duas primeiras o User-ID vem antes do identificador do aparelho, que nos sites vem do identificador do cliente.
3. **Olhe também quem comprou.** Primeiros compradores e total de compradores dependem do evento de compra, que a loja controla, não de quanto o cookie durou.
4. **Trate o número como faixa**, porque cravar um múltiplo exato exige uma medição que o cookie não garante.

## O que isso muda na decisão de verba?

Muda o que você cobra de cada canal. Com o público separado, o canal de prospecção deixa de ser julgado pela taxa que a base inflaciona e passa a responder por duas perguntas: quanta gente nova traz e quanto ela converte perto de canais semelhantes.

Na plataforma de mídia existe um controle para isso. A [Central de Ajuda do Google Ads](https://support.google.com/google-ads/answer/12080169) descreve as metas de ciclo de vida do cliente em três modos: dar lance mais alto para cliente novo que para cliente existente, dar lance mais alto para cliente novo de alto valor e dar lance só para cliente novo. A mesma página orienta definir os clientes existentes com dados próprios da loja e, no modo que só dá lance para cliente novo, recomenda campanha separada para a base. Cada modo tem exigências próprias de meta de conversão, que vale conferir antes de ligar.

Três combinados valem mais que o ajuste na plataforma de mídia:

1. **Dois números no relatório, não um.** Conversão do tráfego novo e do recorrente, por canal, sempre juntas, pelo princípio do estudo sobre [tráfego desqualificado](/taxa-de-conversao-nao-sobe-trafego-desqualificado.html): média que mistura públicos não serve para decidir.
2. **Meta por papel do canal.** Canal de entrada responde por gente nova; canal de base, por recompra.
3. **Página certa para cada público.** O visitante novo precisa de prova; o cliente antigo, de caminho curto. O estudo sobre [persona comportamental](/persona-ecommerce-cro-comportamental.html) mostra como virar prioridade de página, e o de [taxa de conversão do e-commerce](/taxa-de-conversao-ecommerce.html), onde isso entra na análise geral.

## O que ainda não sabemos

Não sabemos qual seria o ranking de canais da loja analisada com uma identificação perfeita das pessoas. Também não sabemos quanto do mérito de cada canal vem de visitas anteriores: o modelo de atribuição, que é a regra que decide qual canal recebe o crédito da venda, não enxerga todas elas. O caso é de um e-commerce, com os limites de cookie descritos acima, e a ordem de grandeza muda de loja para loja. Por isso o estudo não diz qual canal merece mais verba: diz que a decisão não pode sair de uma média que soma quem nunca esteve na loja e quem já é cliente. O número de recompra citado aqui vem da divulgação da própria entidade que fez a pesquisa, mas sem o relatório completo com as tabelas: ele serve de contexto de mercado, não de medida da sua loja.

Se o seu relatório ainda mostra uma linha por canal, com um número só, esse é um dos primeiros cortes que um [diagnóstico de CRO](/#diagnostico), o trabalho de aumentar a parte das visitas que termina em compra, refaz.
