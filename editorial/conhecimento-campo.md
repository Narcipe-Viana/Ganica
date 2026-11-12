# Conhecimento de campo da Ganica (padrões observados em diagnósticos reais)

Padrões que aparecem no trabalho de CRO da Ganica com e-commerces brasileiros. É o que diferencia
um estudo da Ganica de um texto genérico: experiência de primeira mão.

**Este repositório é público.** Por isso, aqui só existem padrões já generalizados: sem nome, sem
número, sem segmento estreito, sem período. Regras de uso nos estudos:

- Apresentar como padrão de diagnóstico ("é um padrão que encontramos com frequência em
  diagnósticos", "em lojas que analisamos"), nunca como relato de um cliente.
- No máximo **um** padrão de campo como caso central por estudo; os outros, se aparecerem, entram
  como menção curta e sem detalhe.
- Não acrescentar detalhe que não está escrito aqui (porte, região, ferramenta, número, data).
- Número de cliente só via `dados_anonimizados` de uma pauta aprovada no `pautas.yml`.
- Seguir a seção 5 do EDITORIAL.md (anonimização) em tudo.

## Padrões

**C1. A quebra mobile fica numa etapa só.** Em funis segmentados por dispositivo, é comum o celular
acompanhar o computador nas etapas de descoberta e carrinho e perder quase tudo no pagamento.
Redesenhar o site mobile inteiro ataca o lugar errado; o ganho costuma estar na mecânica de
pagamento no celular (preenchimento, verificação, confirmação).

**C2. Quem converte é o recorrente, não o canal.** Quando se separa novo de recorrente dentro de
cada canal, a diferença dentro do canal costuma ser maior que a diferença entre canais. Canais
"campeões" muitas vezes só têm público mais recorrente.

**C3. Segurança que vira fricção.** Etapas de verificação no pagamento com cartão (desafios,
confirmações extras) geram dúvida sobre se a compra foi concluída. Cancelamentos e abandonos
tendem a se concentrar no cartão; meios instantâneos sofrem menos. Tratar sempre como hipótese
a testar, não como causa comprovada.

**C4. O mais buscado não é o que mais vende.** Na busca interna, a categoria que concentra as
buscas pode converter bem menos que sua fatia de interesse. Causa provável: excesso de variações
parecidas sem orientação para o leigo (paradoxo da escolha).

**C5. Confiança mora no rodapé.** Em nichos sensíveis (saúde, bem-estar, produto ingerido), o
visitante desconfiado procura selos, meios de pagamento, políticas, dados da empresa e atendimento
no rodapé. Rodapé incompleto, ou atendimento que leva para fora do site, custa venda.

**C6. Benefícios empilhados sem hierarquia.** Lojas acumulam desconto de primeira compra, frete
grátis por faixa, brindes e promoções gerais ao mesmo tempo. O cliente não entende qual vale, o
"exclusivo" deixa de ser exclusivo e a margem some sem ganho de conversão.

**C7. A loja oficial como vitrine.** Marcas que também vendem por revendedores ou outros canais
veem a loja própria receber tráfego e converter pouco: o visitante pesquisa ali e compra em outro
lugar, muitas vezes por preço ou conveniência. O papel da loja oficial precisa ser decidido
(vender, informar, gerar confiança) antes de otimizar a conversão.

**C8. Lojas próprias que competem entre si.** Operações com mais de uma loja própria com catálogo
quase igual dividem autoridade de busca, investimento e atenção. Segmentar catálogo e papel de cada
loja costuma valer mais que otimizar cada uma isoladamente.

**C9. O dado mente antes do cliente.** É comum o GA4 contar eventos em dobro por tags sobrepostas no
gerenciador de tags, ou mostrar etapas posteriores maiores que as anteriores por causa de cookies e
funil aberto. Antes de qualquer conclusão: auditar a instrumentação (modo de depuração, consolidação
de tags, conferência de filtros de data).

**C10. Tráfego pago antes da casa arrumada.** Marcas que cresceram por orgânico e direto e decidem
comprar mídia costumam pagar para levar visitantes a páginas que ainda não convertem bem. A ordem
certa é corrigir fricções óbvias e só então escalar a verba.

**C11. Pouca hora de tecnologia exige priorização em reais.** Com capacidade técnica limitada, a
lista de melhorias só anda quando cada item vira impacto financeiro estimado, esforço e confiança.
O item mais caro (checkout) às vezes ainda é o primeiro.

**C12. Kits por objetivo, não por produto.** Agrupar produtos pelo objetivo do cliente (por exemplo,
rotina de quem treina) comunica melhor que listar itens soltos e ajuda quem não sabe o que escolher.

**C13. Na listagem, o clique vai para a próxima decisão pendente.** Em páginas de categoria e busca,
o clique se concentra em resolver o que falta decidir (achar o item, escolher a variante), não no
botão de compra. (Já publicado no estudo do botão de comprar na listagem.)

**C14. Marca nova em canal novo.** Empresas que abrem um canal direto ao consumidor com marca nova
precisam construir no site a confiança que o nome ainda não tem: prova social, políticas claras,
informação da empresa, atendimento visível.

**C15. Revendedor contra fabricante na mesma busca.** Quando a loja revende um produto que o
fabricante também vende, a página de produto precisa responder melhor que a do fabricante (dúvidas
de uso, comparativos, garantia, entrega). Isso pesa também em respostas de IA.

**C16. Mídia de engajamento e de leads dilui a conversão.** Campanhas pagas com objetivo de
engajamento ou de captura de leads levam ao site muita gente sem intenção de comprar. A taxa de
conversão média cai ou não sobe, e o trabalho de CRO parece não funcionar, mesmo quando a conversão do
público qualificado está estável ou melhorando. Antes de qualquer conclusão sobre o site, separar o
tráfego por objetivo de campanha. (Confirmado pelo Narcipe.)
