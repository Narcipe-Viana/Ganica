---
title: "PostHog, GA4 e BigQuery no e-commerce: o que integrar e como evitar número errado"
seo_title: "Integrar PostHog e BigQuery: guia para e-commerce"
og_title: "PostHog, GA4 e BigQuery: como integrar os dados de um e-commerce"
description: "Como integrar PostHog e BigQuery num e-commerce com GA4: os caminhos, os cuidados que evitam número errado e onde a IA entra de verdade na análise."
twitter_description: "PostHog para o BigQuery, BigQuery para o PostHog, GA4 no meio. O que cada integração resolve, o que ela quebra e onde a IA ajuda."
slug: integrar-posthog-bigquery-ecommerce
date: '2026-11-03'
updated: '2026-11-03'
rascunho: false
breadcrumb: Integrar PostHog e BigQuery
secao: E-commerce
card_kicker: "Técnico · Dados"
card_destaque: "5 caminhos de integração, 1 chave em comum"
card_titulo: "PostHog, GA4 e BigQuery no e-commerce: o que integrar e como evitar número errado."
card_resumo: "Um guia técnico, conferido na documentação oficial, sobre como juntar comportamento, analytics e pedidos num só lugar sem gerar número errado, e como colocar IA em cima disso com segurança."
tags_artigo:
  - analytics
  - PostHog
  - BigQuery
  - GA4
  - dados de e-commerce
keywords:
  - integrar PostHog e BigQuery
  - PostHog BigQuery
  - GA4 BigQuery export
  - analytics para e-commerce
  - IA para análise de dados de e-commerce
sobre:
  - Analytics de produto
  - Data warehouse
  - Otimização de conversão (CRO)
  - Inteligência artificial
imagem_og: ''
resposta_curta: "As integrações úteis num e-commerce são cinco: PostHog para o BigQuery, BigQuery para o PostHog, GA4 para o BigQuery, painéis sobre o BigQuery e assistentes de IA por MCP. As que valem a pena primeiro são as duas exportações para o BigQuery. O que decide se o número presta é deduplicar eventos, tratar dados atrasados e usar o ID do pedido como chave comum."
deck: "Juntar o comportamento do visitante, o analytics e os pedidos num só lugar é o que transforma dado em diagnóstico. Este guia mostra os caminhos possíveis e os cuidados técnicos, conferidos na documentação oficial, que evitam conclusões erradas."
resumo:
  - "Existem **cinco caminhos** práticos para integrar PostHog, GA4 e BigQuery, e cada um resolve um problema diferente. Escolher pela direção do dado evita retrabalho."
  - "Num projeto de e-commerce em que atuamos, **integramos o PostHog ao BigQuery** porque o GA4 apresentava falhas de rastreamento e era preciso uma fonte complementar mais confiável."
  - "A exportação do PostHog pode gerar **eventos duplicados** e organiza os dados por momento de chegada, não do acontecimento. Sem tratar isso, o relatório mente."
  - "PostHog e GA4 **não compartilham identificador** por padrão. A chave mais segura para cruzar comportamento e venda é o **ID do pedido**, com os pedidos também no warehouse."
  - "A IA entra **depois** do modelo de dados: assistentes conectados por MCP aceleram a leitura, mas os controles são diferentes no BigQuery e no PostHog."
faq:
  - pergunta: "PostHog substitui o GA4 num e-commerce?"
    resposta: "Na leitura da Ganica, na maioria dos casos não precisa substituir. O GA4 segue útil para aquisição e para a integração com o Google Ads, e o PostHog acrescenta gravação de sessão, heatmap e análise de funil por pessoa. Juntos no BigQuery, um ajuda a conferir o outro."
  - pergunta: "Quanto custa exportar o GA4 para o BigQuery?"
    resposta: "Depende do volume. Segundo a Central de Ajuda do Google Analytics, o BigQuery cobra armazenamento e processamento de consultas conforme o uso, e a exportação em streaming adiciona 0,05 dólar por GB. Segundo a documentação do BigQuery, o sandbox gratuito tem cota vitalícia de 10 GiB de armazenamento, não devolvida ao apagar dados, e 1 TiB de consultas por mês, com tabelas que expiram em 60 dias e sem streaming. Na leitura da Ganica, ele serve para teste, não para histórico."
  - pergunta: "Por que os números do PostHog, do GA4 e da plataforma da loja nunca batem?"
    resposta: "Porque cada um conta de um jeito. Segundo o Google, o export do GA4 pode diferir da interface, que aplica processamento próprio; GA4 e PostHog instalados por script dependem do navegador do visitante, e a plataforma registra o pedido no servidor. Na leitura da Ganica, diferença pequena e estável é esperada, e diferença que muda de um dia para o outro pede investigação antes de qualquer conclusão."
  - pergunta: "É seguro conectar uma IA aos dados de analytics da loja?"
    resposta: "Pode ser, com os controles certos em cada ferramenta. Segundo o Google Cloud, o assistente deve ter identidade separada, e uma política de negação pode restringir `execute_sql`, a única ferramenta MCP do BigQuery que não é somente leitura. Segundo a documentação do PostHog, o modo só leitura é opcional e as chamadas devem ser revisadas antes de executar, por causa do risco de injeção de prompt. A recomendação da Ganica é manter dado pessoal fora do alcance do assistente."
fontes: "Experiência da Ganica em projeto de e-commerce com PostHog e BigQuery (sem identificação da empresa). Documentação oficial do PostHog: Batch exports, BigQuery destination, Linking BigQuery as a source, Session replay privacy controls, Controlling data collection, Data storage, Events, Identifying users, Model Context Protocol (MCP), MCP FAQ, Data warehouse MCP e Pricing. Documentação oficial do Google: BigQuery Export, Set up BigQuery Export e BigQuery Export schema (Central de Ajuda do Google Analytics); Estimate and control costs, Query partitioned tables, sandbox, Use the BigQuery MCP server e release notes (Google Cloud). Lei 13.709/2018 (LGPD), arts. 5º, 7º e 33, e página da ANPD para titulares. Tudo consultado em novembro de 2026; recursos e preços dessas ferramentas mudam com frequência."
fontes_urls:
  - https://posthog.com/docs/data-pipelines/batch-exports
  - https://posthog.com/docs/data-pipelines/batch-exports/bigquery
  - https://posthog.com/docs/data-pipelines/sources/bigquery
  - https://posthog.com/docs/session-replay/privacy
  - https://posthog.com/docs/privacy/data-collection
  - https://posthog.com/docs/privacy/data-storage
  - https://posthog.com/docs/data/events
  - https://posthog.com/docs/product-analytics/identify
  - https://posthog.com/docs/model-context-protocol
  - https://posthog.com/docs/model-context-protocol/faq
  - https://posthog.com/docs/data-warehouse/surfaces/mcp
  - https://posthog.com/pricing
  - https://support.google.com/analytics/answer/9358801
  - https://support.google.com/analytics/answer/9823238
  - https://support.google.com/analytics/answer/7029846
  - https://docs.cloud.google.com/bigquery/docs/best-practices-costs
  - https://docs.cloud.google.com/bigquery/docs/querying-partitioned-tables
  - https://docs.cloud.google.com/bigquery/docs/sandbox
  - https://docs.cloud.google.com/bigquery/docs/use-bigquery-mcp
  - https://docs.cloud.google.com/bigquery/docs/release-notes
  - https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm
  - https://www.gov.br/anpd/pt-br/assuntos/titular-de-dados-1
cta_titulo: "Seus números de analytics estão contando a mesma história?"
cta_texto: "Antes de qualquer teste, um diagnóstico de CRO confere se o rastreamento da sua loja é confiável e mapeia onde a conversão está sendo perdida."
autor_texto: "Sou consultor de CRO focado em e-commerce, com trabalho direto em estrutura de analytics (GTM, GA4, PostHog, BigQuery, Looker Studio) e auditoria comportamental. Meu princípio é simples: antes de analisar, garantir que o dado conta a verdade."
---

## Por que levar o comportamento do visitante para um data warehouse?

Na leitura da Ganica, integrar PostHog e BigQuery faz sentido porque nenhuma ferramenta sozinha conta a história inteira de uma venda. O GA4 é bom em aquisição, o PostHog é bom em comportamento (gravação de sessão, heatmap, funil por pessoa) e a plataforma da loja é a fonte do pedido. Um data warehouse é um banco de dados feito para análise, onde essas fontes podem ser cruzadas com SQL.

O BigQuery, do Google Cloud, é um destino natural nesse cenário porque o GA4 exporta para ele nativamente. Com o PostHog e os pedidos da loja no mesmo lugar, surge uma pergunta que nenhuma ferramenta responde sozinha: dos pedidos pagos, quantos o GA4 deixou de registrar, e o PostHog viu essas compras?

## Quais são os caminhos para integrar PostHog, GA4 e BigQuery?

São cinco caminhos práticos: PostHog para o BigQuery, BigQuery para o PostHog, GA4 para o BigQuery, BigQuery para o Looker Studio e IA conectada por MCP. A recomendação da Ganica é começar pelas duas exportações para o BigQuery, porque painéis e IA dependem delas.

| Caminho | Para que serve |
|---|---|
| **1. PostHog para o BigQuery (exportação em lote)** | Cruzar eventos, pessoas e sessões com pedidos e GA4 usando SQL. |
| **2. BigQuery para o PostHog (fonte do data warehouse)** | Analisar tabelas como pedidos dentro do PostHog, junto com o comportamento. |
| **3. GA4 para o BigQuery (exportação nativa)** | Ter o dado bruto do GA4, por evento, sem a amostragem e o processamento dos relatórios. |
| **4. BigQuery para o Looker Studio** | Painéis para o time e a diretoria, a partir de tabelas tratadas. |
| **5. IA conectada por MCP ao BigQuery e ao PostHog** | Fazer perguntas em linguagem natural, com o assistente consultando os dados. |

**Exportação em lote do PostHog.** Segundo a documentação do PostHog, as exportações em lote enviam dados com frequências que vão de 5 minutos até semanal, para destinos como BigQuery, Snowflake, Redshift, Postgres e S3. Os modelos principais são eventos, que são imutáveis, pessoas, que mudam com o tempo, e sessões. No BigQuery, a tabela de eventos é criada particionada por dia na coluna `timestamp`.

**BigQuery como fonte do PostHog.** O caminho inverso usa uma conta de serviço do Google Cloud com permissão de leitura e escrita num conjunto de dados. A documentação do PostHog alerta que o teste de conexão só valida a leitura, de modo que uma permissão de escrita faltando passa no teste e falha na primeira sincronização. A mesma documentação informa que o modo sandbox do BigQuery não é suportado nesse caminho.

**GA4 para o BigQuery.** Segundo a Central de Ajuda do Google Analytics, a exportação diária traz o dado bruto do dia anterior, sem horário garantido, e propriedades padrão têm limite de 1 milhão de eventos por dia. Se a propriedade passa desse limite de forma consistente, o Google avisa que a exportação diária é pausada e que os dias anteriores não são reprocessados. Segundo o Google, a exportação em streaming entrega o dia corrente em minutos, sem garantia de completude, por 0,05 dólar adicional por GB.

## O que fizemos num projeto real com PostHog e BigQuery?

Num projeto de e-commerce em que atuamos, integramos o PostHog ao BigQuery porque o GA4 apresentava falhas de rastreamento e a busca era por uma fonte complementar mais confiável. A leitura da Ganica é que ligar a integração é a parte fácil. O que decide se o número presta vem depois: entender onde as ferramentas divergem e qual campo junta as duas pontas.

## Quais cuidados técnicos evitam números errados?

Seis cuidados, reunidos pela Ganica a partir da documentação do PostHog e do Google, evitam números errados: deduplicar eventos, contar com dados atrasados, partir da tabela de eventos, planejar colunas novas, filtrar pela partição e fechar números na tabela diária do GA4.

1. **Deduplique os eventos.** A documentação do PostHog avisa que a exportação pode gerar duplicatas e recomenda deduplicar no destino. Cada evento tem um `uuid` único: use-o numa visão ou tabela tratada antes de qualquer contagem.
2. **Conte com dados atrasados.** Segundo o PostHog, os dados entram em cada lote pelo momento em que chegaram ao PostHog, não pelo momento em que aconteceram. Relatórios que fecham o dia cedo demais subcontam.
3. **Não espere o visitante anônimo na tabela de pessoas.** Segundo o PostHog, a exportação de pessoas só inclui quem tem perfil de pessoa. As análises de funil precisam partir da tabela de eventos.
4. **Planeje colunas novas.** O PostHog avisa que campos novos dos modelos de exportação não são adicionados sozinhos às tabelas de destino: é preciso criar a coluna manualmente. As propriedades de evento ficam na coluna `properties`, em JSON ou texto, conforme a opção da exportação.
5. **Filtre pela partição.** No modelo sob demanda, o BigQuery cobra pelo volume lido, e a documentação do Google Cloud diz que filtrar pela coluna de partição reduz esse volume.
6. **Use a tabela diária do GA4 para fechar números.** O Google orienta consultar `events_YYYYMMDD`, e não a tabela provisória `events_intraday_YYYYMMDD`, avisa que os números do export podem diferir da interface e informa que tabelas diárias ainda recebem eventos atrasados por até 2 dias corridos, além de hoje.

A recomendação da Ganica é transformar esses pontos numa camada de tabelas tratadas antes de qualquer análise.

## Como ligar o comportamento do PostHog ao pedido e ao GA4?

A recomendação da Ganica é ligar comportamento e venda pelo ID do pedido, usado como chave comum, com a base de pedidos da loja também no BigQuery. Por padrão, as duas ferramentas não compartilham identificador: segundo a documentação de cada uma, o GA4 usa `user_pseudo_id` e o PostHog usa `distinct_id`. Na leitura da Ganica, um visitante anônimo vira dois registros sem ligação.

Há três formas de ligar as pontas, da mais confiável à mais frágil, na avaliação da Ganica:

1. **ID do pedido nos dois.** Envie o mesmo `transaction_id` no evento de compra do GA4 e numa propriedade do evento de compra no PostHog. A chave liga as ferramentas à base de pedidos, mas só existe para quem comprou.
2. **ID do cliente após o login.** Quando o cliente se identifica, o mesmo identificador interno pode ser enviado como `user_id` no GA4 e na identificação do PostHog. Não alcança quem compra como visitante.
3. **ID do navegador de uma ferramenta guardado na outra.** É frágil: depende de cookies e exige cuidado redobrado com consentimento.

Com a chave definida e os pedidos no warehouse, dá para responder quantos pedidos o PostHog e o GA4 registraram e onde cada um perdeu. O método é o mesmo cruzamento por `transaction_id` descrito no [estudo sobre funil por dispositivo](/conversao-checkout-mobile-funil-por-dispositivo.html), aqui com três fontes.

## Onde a IA entra de verdade na análise?

Na leitura da Ganica, a IA entra depois do modelo de dados, nunca antes. Com as tabelas tratadas e a chave comum definida, um assistente conectado por MCP consulta os dados e responde em linguagem natural. MCP (Model Context Protocol) é um padrão aberto que permite a um assistente de IA usar ferramentas externas, como um banco de dados, com permissões controladas.

BigQuery e PostHog oferecem servidor MCP oficial, cada um sobre os próprios dados:

- **BigQuery.** Segundo o Google Cloud, o servidor MCP lista tabelas e executa SQL, com a ferramenta `execute_sql_readonly` só de leitura, limite padrão de três minutos por consulta e máximo de 3.000 linhas por resultado.
- **PostHog.** Segundo a documentação do PostHog, o servidor MCP consulta dados com SQL, gerencia flags e experimentos e investiga erros. Conectar é gratuito, mas ferramentas que usam IA internamente podem ser cobradas.

A recomendação da Ganica é usar assistentes conectados por MCP na primeira leitura dos dados: perguntar em que etapa o funil caiu esta semana, por dispositivo e por meio de pagamento, e receber a consulta pronta junto com o resultado. O ganho é de velocidade. A interpretação continua humana.

A recomendação da Ganica são três regras de segurança, com controles diferentes em cada ferramenta:

- **Uma identidade separada para o assistente**, como recomenda a documentação do Google Cloud.
- **Somente leitura.** No BigQuery, segundo o Google Cloud, `execute_sql` é a única ferramenta MCP que não é somente leitura e pode ser restringida por política de negação; os papéis pedidos são MCP Tool User, BigQuery Job User e BigQuery Data Viewer. No PostHog, segundo a documentação do MCP, o modo só leitura é opcional e se ativa pelo cabeçalho `x-posthog-read-only` ou pelo parâmetro `readonly`.
- **Dado pessoal fora do alcance.** No BigQuery, exponha ao assistente só as tabelas tratadas, sem nome, e-mail, telefone ou IP. No PostHog, a documentação informa que o MCP alcança tabelas vinculadas do warehouse, então sincronize só tabelas tratadas e não capture o que não é necessário.

A documentação do PostHog também alerta para o risco de injeção de prompt e orienta revisar as chamadas antes de executar.

## O que a LGPD exige numa integração como essa?

A LGPD trata como dado pessoal toda informação relacionada a pessoa natural identificada ou identificável (art. 5º, I, da Lei 13.709/2018), e cada integração leva esse dado para mais um lugar. O tratamento precisa de hipótese legal (art. 7º), e a transferência internacional só é permitida nos casos previstos (art. 33). Na prática, quatro pontos merecem atenção:

1. **Gravação de sessão.** Segundo a documentação do PostHog, os campos de formulário são mascarados por padrão, mas o texto da página não. Em áreas como "minha conta" e confirmação de pedido, mascare o texto ou use a classe `ph-no-capture`, que substitui o elemento por um bloco na gravação.
2. **IP e propriedades exportadas.** A tabela de eventos exportada para o BigQuery tem uma coluna `ip`, e o PostHog permite configurar o projeto para descartar o IP. Na leitura da Ganica, remover só a coluna pode não bastar: a propriedade `$ip` e `person_properties` também merecem revisão.
3. **Identificadores.** `transaction_id`, `user_id` e `distinct_id` não mostram um nome, mas podem ser religados à base de pedidos. A Ganica recomenda tratá-los como dado pessoal.
4. **Acesso.** No BigQuery, quem acessa o quê é controlado por permissões. Separe a tabela bruta, de acesso restrito, das tabelas tratadas.

Este guia não é orientação jurídica. Em operações com dados sensíveis, como saúde, vale ouvir um especialista em proteção de dados antes de começar.

## Por onde começar a integrar PostHog e BigQuery?

A recomendação da Ganica é começar pela pergunta de negócio, não pela ferramenta, nesta ordem:

1. **Escreva as três perguntas** que hoje ninguém consegue responder. Por exemplo: quanto o GA4 está deixando de registrar.
2. **Audite o rastreamento** antes de exportar qualquer coisa.
3. **Ative a exportação do GA4 para o BigQuery**, que é nativa e, segundo o Google, começa a enviar dados em até 24 horas depois do vínculo. Confira antes se a propriedade cabe no limite diário.
4. **Configure a exportação do PostHog** com as colunas de propriedades em JSON e frequência compatível com o uso.
5. **Leve os pedidos da loja para o BigQuery** e garanta o ID do pedido nos eventos de compra das duas ferramentas.
6. **Monte a camada tratada**, com deduplicação, janela para dados atrasados e sem dados pessoais diretos.
7. **Só então conecte painéis e IA**, com acesso só de leitura às tabelas tratadas.

A auditoria do passo 2 é parte do que um [diagnóstico de CRO](/#diagnostico) entrega.

## O que ainda não sabemos

Custos e recursos dessas ferramentas mudam com frequência. Em novembro de 2026, a tabela de preços do PostHog trazia 1 milhão de linhas gratuitas por mês nas exportações em lote e cobrança por linha acima disso. As notas de versão do BigQuery registram o servidor MCP como disponibilidade geral desde abril de 2026.

Também não encontramos um padrão de mercado para quanto o PostHog e o GA4 devem divergir. A diferença aceitável depende da loja, do consentimento e de bloqueadores de anúncios. Na leitura da Ganica, uma diferença que muda muito de um dia para o outro pede investigação antes de qualquer conclusão.

Este guia reúne um caso e a documentação oficial. Ele não mede ganho de conversão.
