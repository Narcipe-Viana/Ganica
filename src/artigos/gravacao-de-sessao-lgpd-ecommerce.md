---
title: "Gravação de sessão e LGPD: o que mascarar, o que não gravar e como provar que fez"
seo_title: "Gravação de sessão e LGPD: o guia para e-commerce"
og_title: "Gravação de sessão e LGPD: mascarar, não gravar e provar que fez"
description: "Gravação de sessão e LGPD no e-commerce: o que cada ferramenta mascara por padrão, quais páginas não gravar e que registros mostram que a loja fez a sua parte."
twitter_description: "Clarity, Hotjar, PostHog e LogRocket mascaram coisas diferentes por padrão. O guia para gravar sessões na loja sem guardar dado pessoal que não devia, conferido na documentação oficial em novembro de 2026."
slug: gravacao-de-sessao-lgpd-ecommerce
date: '2026-11-24'
hora: "07:06"
updated: '2026-11-24'
rascunho: false
breadcrumb: Gravação de sessão e LGPD
secao: E-commerce
card_kicker: "Técnico · Privacidade de dados"
card_destaque: "Máscara depois do envio não existe"
card_titulo: "Gravação de sessão e LGPD: o que mascarar, o que não gravar e como provar que fez."
card_resumo: "O que Clarity, Hotjar, PostHog e LogRocket escondem por padrão, quais áreas da loja ficam fora da gravação e quais registros mostram que a configuração foi feita, conferidos na documentação oficial em novembro de 2026."
tags_artigo:
  - LGPD
  - gravação de sessão
  - Microsoft Clarity
  - Hotjar
  - PostHog
  - LogRocket
keywords:
  - gravação de sessão LGPD
  - session replay LGPD
  - mascaramento de dados gravação de sessão
  - Clarity LGPD
  - Hotjar LGPD
sobre:
  - Proteção de dados pessoais
  - Gravação de sessão
  - Lei Geral de Proteção de Dados (LGPD)
  - Otimização de conversão (CRO)
imagem_og: ''
resposta_curta: "A LGPD não proíbe a gravação de sessão, mas exige finalidade clara, só o dado necessário, segurança e prova do que foi feito. Na prática, a loja mascara no navegador tudo o que é digitado e o texto com dado pessoal, deixa fora da gravação as áreas de conta, pagamento e confirmação, e guarda o registro da configuração, dos testes e de quem acessa as gravações."
deck: "Gravar a sessão do visitante ajuda a achar onde a loja perde venda, mas também pode guardar nome, endereço e o que a pessoa comprou. Este guia mostra o que cada ferramenta esconde por padrão, o que a loja precisa esconder por conta própria e como documentar isso, com base na documentação oficial e no texto da LGPD conferidos em novembro de 2026."
resumo:
  - "A LGPD não fala em gravação de sessão, mas os princípios de **finalidade, necessidade, segurança e prestação de contas** (art. 6º) se aplicam a ela sempre que a gravação registra dado pessoal."
  - "As ferramentas não mascaram as mesmas coisas por padrão: no **PostHog** e no **LogRocket**, o texto comum da página é gravado; no **Clarity**, o modo padrão mascara números e e-mails; no **Hotjar**, o que é digitado e, por padrão, números e e-mails da página ficam escondidos."
  - "Nas quatro ferramentas, a máscara é aplicada **no navegador, antes do envio**. Clarity e Hotjar avisam que mudar a máscara não esconde o que já foi gravado."
  - "Em loja de saúde, o item comprado pode revelar algo sobre a saúde do cliente, e a LGPD trata **dado referente à saúde** como sensível, sem a base do legítimo interesse (art. 11)."
  - "A recomendação da Ganica é deixar **conta e confirmação do pedido** fora da gravação, gravar o **pagamento só com máscara total** e guardar **cinco registros** que provam a configuração."
faq:
  - pergunta: "Preciso pedir consentimento para gravar a sessão do visitante?"
    resposta: "Depende da base legal escolhida pela loja e do tipo de dado. A LGPD admite outras bases além do consentimento, como o legítimo interesse (art. 7º, IX), mas ele só permite tratar o dado estritamente necessário, exige transparência (art. 10) e não serve para dado sensível. A decisão precisa ser registrada e combinada com o aviso de cookies e a política de privacidade da loja, de preferência com apoio jurídico."
  - pergunta: "O aviso de cookies resolve a LGPD da gravação de sessão?"
    resposta: "Não sozinho. O aviso cuida da transparência e, quando a base é o consentimento, da escolha do visitante, mas não impede que a ferramenta grave um nome ou um endereço que aparece na tela. A máscara e a exclusão de páginas são o que de fato limita o dado coletado."
  - pergunta: "Mapa de calor também tem dado pessoal?"
    resposta: "Em geral, bem menos que a gravação. Segundo a documentação do Microsoft Clarity, o mapa de calor é montado a partir dos atributos dos elementos da página, e não do conteúdo deles. Mesmo assim, ele vem do mesmo código da ferramenta instalado no site, então as regras de máscara e de páginas excluídas valem para os dois."
  - pergunta: "Dá para apagar a gravação de um cliente específico que pediu exclusão?"
    resposta: "Depende da ferramenta, e vale conferir antes de contratar. O FAQ do Clarity, por exemplo, informa que, para excluir os dados de um usuário, é preciso apagar o projeto inteiro. Por isso a máscara no navegador pesa tanto: dado que nunca foi enviado não precisa ser apagado depois."
fontes: "Documentação oficial consultada em novembro de 2026: Microsoft Learn (Clarity: Masking content, Consent API v2, Cookie consent, FAQ); Central de Ajuda do Hotjar (supressão de dados, liberação de campos, Privacy FAQs); documentação do PostHog (Session replay privacy controls); documentação do LogRocket (Privacy e referência de configuração do DOM). Lei 13.709/2018 (LGPD), texto compilado no Planalto, arts. 5º, 6º, 7º, 10, 11, 33, 37 e 46. Página da ANPD sobre transferência internacional de dados (Resolução CD/ANPD nº 19/2024 e Resolução nº 32/2026, adequação da União Europeia). A organização em três camadas, a lista de áreas da loja e os registros recomendados são leitura da Ganica. Este estudo não é orientação jurídica; configurações e padrões das ferramentas mudam com frequência e devem ser conferidos antes de qualquer decisão."
fontes_urls:
  - "Lei nº 13.709/2018, Lei Geral de Proteção de Dados, texto compilado (Planalto) | https://planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709compilado.htm"
  - "Masking content, Microsoft Clarity (Microsoft Learn) | https://learn.microsoft.com/en-us/clarity/setup-and-installation/clarity-masking"
  - "Clarity Consent API v2 (Microsoft Learn) | https://learn.microsoft.com/en-us/clarity/clarity-consent-api-v2"
  - "Cookie consent, Microsoft Clarity (Microsoft Learn) | https://learn.microsoft.com/en-us/clarity/cookie-consent"
  - "About Clarity (FAQ), Microsoft Learn | https://learn.microsoft.com/clarity/faq"
  - "How to suppress text, images, videos and user input, Central de Ajuda do Hotjar | https://help.hotjar.com/hc/en-us/articles/36819956605329-How-to-Suppress-Text-Images-Videos-and-User-Input-from-Collected-Data"
  - "How to show elements and keystrokes in data collection, Central de Ajuda do Hotjar | https://help.hotjar.com/hc/en-us/articles/36820034730641-How-to-Show-Elements-and-Keystrokes-in-Data-Collection"
  - "Privacy FAQs, Central de Ajuda do Hotjar | https://help.hotjar.com/hc/en-us/articles/36820004397713-Privacy-FAQs"
  - "Session replay privacy controls (PostHog Docs) | https://posthog.com/docs/session-replay/privacy"
  - "Privacy, LogRocket Docs (LogRocket) | https://docs.logrocket.com/docs/privacy"
  - "Control how LogRocket records the DOM (LogRocket Docs) | https://docs.logrocket.com/reference/dom"
  - "Transferência internacional de dados (ANPD) | https://www.gov.br/anpd/pt-br/assuntos/assuntos-internacionais/transferencia-internacional-de-dados/international-affairs"
cta_titulo: "A sua ferramenta de gravação está registrando mais do que a loja precisa?"
cta_texto: "Um diagnóstico de CRO revisa o que está sendo gravado, em quais páginas e com quais máscaras, junto com a pergunta de negócio que justifica cada gravação."
autor_texto: "Sou consultor de CRO focado em e-commerce, com trabalho direto em estrutura de analytics (GTM, GA4, PostHog, BigQuery, Looker Studio) e auditoria comportamental. Antes de ligar qualquer gravação, a pergunta que faço é qual decisão ela vai ajudar a tomar."
---

## O que a LGPD exige de quem usa gravação de sessão no e-commerce?

A LGPD (Lei Geral de Proteção de Dados) exige que a gravação de sessão tenha finalidade clara, colete só o necessário, seja protegida e possa ser comprovada. Gravação de sessão (em inglês, session replay) é o registro da visita de uma pessoa ao site, que a loja assiste depois como se fosse um vídeo da tela: a ferramenta reconstrói a página a partir das mudanças no código, e por isso registra tudo o que aparece na tela, a menos que alguém mande esconder.

A lei não cita gravação de sessão, mas o [texto da LGPD no Planalto](https://planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709compilado.htm) define dado pessoal como informação relacionada a pessoa natural identificada ou identificável (art. 5º, I). Um nome no cabeçalho da conta, um endereço na tela de entrega ou um e-mail digitado no cadastro entram nessa definição. A partir daí valem os princípios do art. 6º: finalidade (um propósito específico e informado), necessidade (o mínimo necessário), transparência, segurança e prestação de contas, que pede que a loja consiga demonstrar as medidas que adotou.

Por isso este guia organiza o trabalho em três camadas: o que mascarar, o que não gravar e como provar que fez. Ele complementa o comparativo de [ferramentas de analytics para e-commerce](/ga4-posthog-hotjar-clarity-logrocket-ecommerce.html), que mostra qual pergunta de negócio cada ferramenta responde. Este guia não é orientação jurídica: a base legal e o texto da política de privacidade são decisões que pedem apoio de quem cuida da conformidade da loja.

## O que cada ferramenta mascara por padrão?

As ferramentas de gravação de sessão não escondem as mesmas coisas quando são instaladas sem ajuste. Mascarar é trocar o conteúdo por asteriscos, blocos ou caracteres neutros antes que ele seja enviado ao servidor da ferramenta. A diferença mais importante está no texto comum da página, como o nome do cliente impresso na tela.

| Ferramenta | O que vem escondido sem nenhum ajuste |
|---|---|
| Microsoft Clarity | Campos de digitação e listas de seleção em qualquer modo; no modo padrão (Equilibrado), também números e e-mails da página |
| Hotjar | Tudo o que é digitado; números e e-mails no texto da página (opções ligadas por padrão); sequências de 9 ou mais dígitos e e-mails digitados nunca são gravados, nem em campos liberados |
| PostHog | Campos de digitação; o texto comum da página é gravado |
| LogRocket | Campos de senha; os demais elementos, inclusive texto e campos, são gravados |

*Tabela: leitura da Ganica a partir da documentação oficial de cada ferramenta, consultada em novembro de 2026.*

No Clarity, a página de [mascaramento do Microsoft Clarity](https://learn.microsoft.com/en-us/clarity/setup-and-installation/clarity-masking) descreve três modos: Estrito (todo o conteúdo mascarado), Equilibrado (só números e e-mails, o padrão) e Relaxado (nada além de campos e listas). No Hotjar, a [central de ajuda sobre supressão](https://help.hotjar.com/hc/en-us/articles/36819956605329-How-to-Suppress-Text-Images-Videos-and-User-Input-from-Collected-Data) informa que o que é digitado é suprimido por padrão e que a supressão acontece antes de a sessão sair da página para o Hotjar. A mesma página informa que números e e-mails no texto da página também são suprimidos por padrão.

No PostHog, a [documentação de privacidade da gravação](https://posthog.com/docs/session-replay/privacy) diz que os campos são mascarados por padrão, mas o texto geral não. No LogRocket, a [referência de configuração do DOM](https://docs.logrocket.com/reference/dom) diz que só os campos de senha ficam de fora e que todos os outros elementos são capturados por padrão. Na prática, uma loja que instala PostHog ou LogRocket sem ajuste grava o nome e o endereço que aparecem impressos na tela de entrega.

## Por que a máscara precisa ser configurada antes de ligar a gravação?

A máscara precisa vir antes porque ela age no navegador, antes do envio. A documentação do Clarity afirma que mudanças de máscara não valem para trás, e a do Hotjar diz que, depois que a sessão é enviada, não há como suprimir o dado. A documentação do PostHog diz que o conteúdo mascarado é retirado no navegador e nunca segue pela rede, e a [página de privacidade do LogRocket](https://docs.logrocket.com/docs/privacy) diz que o dado excluído nunca é enviado aos servidores dele. A consequência é a mesma nas quatro ferramentas: o que foi enviado antes da máscara já está lá.

Esse detalhe muda a ordem do trabalho. Ligar a gravação primeiro e ajustar as máscaras quando alguém notar um problema significa guardar dado pessoal por semanas. Segundo o [FAQ do Clarity](https://learn.microsoft.com/clarity/faq), as gravações ficam guardadas por 30 dias, mas as marcadas como favoritas e uma amostra aleatória ficam até 9 meses; o mesmo FAQ informa que, para excluir os dados de um usuário específico, é preciso apagar o projeto inteiro. No Hotjar, segundo as [perguntas frequentes de privacidade](https://help.hotjar.com/hc/en-us/articles/36820004397713-Privacy-FAQs), gravações e mapas de calor ficam 365 dias a partir da captura; quem migrou para o Contentsquare Free tem prazo menor, como mostra o [comparativo de ferramentas](/ga4-posthog-hotjar-clarity-logrocket-ecommerce.html).

Cada ferramenta tem o próprio comando para esconder um trecho da página. Um atributo é uma marcação colocada no código do elemento, e um seletor é a regra que aponta qual elemento da página deve ser afetado:

| Ferramenta | Como esconder um elemento ou todo o texto |
|---|---|
| Microsoft Clarity | Atributo `data-clarity-mask="True"` (vale para o elemento e o que está dentro dele) ou seletor no painel; modo Estrito para todo o texto |
| Hotjar | Atributo ou classe `data-hj-suppress`; opção de suprimir todo o texto nas configurações do site |
| PostHog | Classe `ph-no-capture` (troca o elemento por um bloco do mesmo tamanho); opção `maskTextSelector: "*"` para todo o texto |
| LogRocket | Atributo `data-private`; opções `textSanitizer` e `inputSanitizer`, desligadas por padrão |

*Tabela: atributos e opções descritos na documentação oficial de cada ferramenta, consultada em novembro de 2026.*

Dois detalhes evitam surpresa. O Clarity avisa que não mascara o conteúdo de folhas de estilo, e no Hotjar o atributo `data-hj-allow` ([central de ajuda sobre liberação de campos](https://help.hotjar.com/hc/en-us/articles/36820034730641-How-to-Show-Elements-and-Keystrokes-in-Data-Collection)), que libera a gravação do que é digitado num campo, não vale para os campos que estão dentro do elemento marcado: precisa ir em cada campo.

## Quais páginas da loja não deveriam ser gravadas?

Algumas áreas da loja concentram dado pessoal e raramente precisam do conteúdo visível para responder uma pergunta de conversão. A recomendação da Ganica é deixar fora da gravação a área do cliente (pedidos, endereços, dados cadastrais) e a página de confirmação do pedido, onde aparecem nome, endereço e itens comprados juntos, e gravar as telas de pagamento só com máscara total, porque, num padrão que encontramos com frequência em diagnósticos, é nelas que o celular perde a venda, e o clique continua visível sem o conteúdo.

Cada ferramenta resolve isso de um jeito. A documentação do PostHog aponta controles para iniciar e parar a gravação por código, indicados para componentes de terceiros que não podem ser mascarados, como formulários de pagamento e telas de login. No Hotjar, a supressão de todo o conteúdo pode valer para o site inteiro ou só para páginas escolhidas, nas configurações do site. No Clarity, a máscara pode ser aplicada por seletor no painel ou pelo atributo `data-clarity-mask` no código; para não gravar uma página, o FAQ do Clarity orienta tirar o código da ferramenta dessa página.

O caso que mais pede cuidado é a loja de saúde, de suplementos ou de qualquer produto que revele algo sobre o corpo de quem compra. A LGPD lista o dado referente à saúde entre os dados pessoais sensíveis (art. 5º, II), e o art. 11 não inclui o legítimo interesse entre as bases para tratar dado sensível. Um carrinho com o nome de um medicamento, ligado a uma pessoa identificável, pode ser lido como dado de saúde. Para dado sensível, a base do consentimento precisa ser específica e destacada, para finalidades específicas (art. 11, I). Na dúvida, o caminho mais seguro é mascarar nomes de produto nas telas de carrinho, checkout e confirmação, ou não gravar essas telas. O estudo sobre o [rodapé de confiança em lojas de saúde](/rodape-ecommerce-confianca-saude.html) mostra por que esse visitante já chega desconfiado.

Duas áreas costumam passar despercebidas. A busca interna grava o que a pessoa digitou na barra de busca e pode revelar a mesma coisa que o carrinho. E endereços de página com e-mail ou número de pedido no próprio link aparecem no reprodutor da gravação: o PostHog oferece a função `maskCapturedNetworkRequestFn`, que edita o endereço no navegador antes do envio, e no LogRocket a limpeza de dados da rede é configurada à parte da limpeza da tela.

## Como configurar a gravação de sessão com LGPD, passo a passo?

A forma mais segura é configurar, testar e registrar antes de liberar a gravação para todo o tráfego, nesta ordem recomendada pela Ganica:

1. **Escreva a finalidade em uma frase.** Por exemplo: "entender por que o visitante do celular abandona o carrinho". Gravação sem pergunta coleta dado sem necessidade, e o art. 6º pede propósito específico.
2. **Escolha e registre a base legal com quem cuida da conformidade.** Base legal é a justificativa, prevista na lei, que autoriza usar o dado. Legítimo interesse exige que só o dado estritamente necessário seja tratado e que haja transparência (art. 10); consentimento exige que o aviso de cookies realmente controle a ferramenta.
3. **Mapeie as páginas da loja em três grupos:** gravar com máscara padrão, gravar com máscara total e não gravar. Conta, pagamento e confirmação começam no segundo ou no terceiro grupo.
4. **Ajuste a máscara antes de instalar em produção.** No PostHog, ligue a máscara de texto (`maskTextSelector`) ou marque os blocos com dado pessoal; no LogRocket, que grava também o que é digitado, ligue `inputSanitizer` e marque com `data-private` os blocos com nome e endereço; no Clarity, o modo de máscara vale para o projeto inteiro, então use o Estrito no projeto ou mascare os blocos dessas páginas com `data-clarity-mask="True"` ou com um seletor no painel; no Hotjar, aplique a supressão nos elementos com nome e endereço.
5. **Ligue o aviso de cookies à ferramenta.** No Clarity, a [Consent API v2](https://learn.microsoft.com/en-us/clarity/clarity-consent-api-v2) é o comando que avisa a ferramenta se o visitante aceitou. Atenção a dois pontos da documentação. O modo de consentimento do Clarity só vem ligado por padrão para visitantes do Espaço Econômico Europeu, do Reino Unido e da Suíça; para que o Clarity não grave cookies antes do aceite em nenhum lugar, a [página de cookies do Clarity](https://learn.microsoft.com/en-us/clarity/cookie-consent) orienta desligar a opção de cookies nas configurações de instalação do projeto. E, quando o consentimento é negado, o Clarity continua coletando, só que sem cookies e com um identificador por página vista. Por isso, se a base legal escolhida for o consentimento, a recomendação da Ganica é carregar o código da ferramenta só depois do aceite.
6. **Teste com um pedido de mentira.** Faça uma compra de teste com nome e endereço fictícios e assista à própria gravação procurando qualquer dado que deveria estar escondido.
7. **Restrinja o acesso e repita o teste a cada mudança no checkout.** Uma tela nova pode criar um elemento que a regra antiga não cobre. O art. 46 da LGPD pede medidas técnicas e administrativas de segurança, e o § 2º diz que elas valem desde a concepção do serviço.

## Como provar que a loja fez a sua parte?

A loja prova que fez a sua parte guardando registros simples, com data, do que configurou e testou. A LGPD pede que controlador e operador mantenham registro das operações de tratamento, especialmente quando a base é o legítimo interesse (art. 37), e permite que a ANPD (Autoridade Nacional de Proteção de Dados) peça um relatório de impacto quando o tratamento se apoia nessa base (art. 10, § 3º).

A recomendação da Ganica é manter cinco registros, num documento que qualquer pessoa da equipe consiga encontrar:

- **A finalidade e a base legal**, com a data da decisão e quem decidiu.
- **O mapa de páginas**: o que é gravado, com qual máscara e o que fica fora.
- **A configuração da ferramenta**: modo de máscara, seletores e atributos usados, prazo de guarda das gravações.
- **O teste com pedido fictício**, repetido a cada mudança relevante no site, com a conclusão anotada.
- **A lista de quem acessa as gravações** e por quê.

Há ainda a questão de onde o dado fica guardado. Segundo o FAQ de privacidade do Hotjar, os dados ficam na Amazon Web Services na Irlanda; segundo o FAQ do Clarity, na nuvem Microsoft Azure. Enviar dado pessoal para fora do Brasil é transferência internacional, que a LGPD só admite nas hipóteses do art. 33. Uma delas é o país considerado adequado pela ANPD: segundo a [página da ANPD sobre transferência internacional](https://www.gov.br/anpd/pt-br/assuntos/assuntos-internacionais/transferencia-internacional-de-dados/international-affairs), a União Europeia foi reconhecida como adequada pela Resolução nº 32/2026, o que, na leitura da Ganica, tende a cobrir o envio para servidores na Irlanda. Se o fornecedor repassar dados a empresas fora da União Europeia, vale conferir no contrato como esse repasse é tratado. Para outros destinos, um caminho são as cláusulas-padrão da Resolução CD/ANPD nº 19/2024. O FAQ do Clarity não cita a região de armazenamento, então vale confirmar com o fornecedor e com o jurídico onde o dado fica e como o contrato trata esse ponto.

## O que ainda não sabemos

A ANPD não publicou, até onde este estudo conseguiu verificar, uma orientação específica sobre gravação de sessão em sites. As recomendações deste guia partem dos princípios gerais da LGPD e da documentação das ferramentas, e não de uma decisão da autoridade sobre o tema.

Também não há resposta fechada sobre quando o nome de um produto passa a ser dado de saúde. Este estudo trata a dúvida com cautela, mas a resposta depende do produto, do contexto e da interpretação jurídica.

Por fim, os padrões de máscara mudam com as versões das ferramentas, e as páginas oficiais nem sempre mostram a data da mudança. A documentação da Microsoft não é uniforme: o FAQ do Clarity diz que todo o conteúdo é escondido por padrão, enquanto a página de mascaramento indica o modo Equilibrado; vale conferir o modo no próprio painel. O mesmo acontece no Hotjar: a página de supressão diz que números e e-mails no texto vêm escondidos por padrão, enquanto as perguntas frequentes de privacidade citam só as sequências de números; confira as opções de supressão nas configurações do site. Os comportamentos citados foram conferidos em novembro de 2026. Se a loja quer saber o que as gravações registram hoje e se elas respondem alguma pergunta de conversão, esse é um bom ponto de partida para um [diagnóstico de CRO](/#diagnostico) (otimização da taxa de conversão).
