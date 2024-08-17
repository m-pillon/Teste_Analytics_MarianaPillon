# Teste de Analytics - Mariana Pillon

## Parte 1: Criação e análise de dados
**Sobre os dados**: 
* Foi simulado o controle de vendas de uma padaria
* Cada entrada se refere a apenas um produto, identificado por seu nome;
* Há 8 produtos possíveis, com preços de R$1,00 a R$4,50 (fixos)
* O número de unidades do produto compradas (quantidade) vai de 1 a 10

**Limpeza de dados**:
* Não há dados faltantes, porém, se tivesse, aqui estão algumas estratégias:
  * Para o preço: copiar o preço da venda anterior ao dado faltante daquele produto
  * Para a quantidade: média, moda ou mediana, dependendo de outras métricas
  * Para o nome do produto: predição com base na categoria e preço
  * Para a data: se for importante para a análise, tirar aquela linha; se não, ignorar a coluna data

## Parte 2: SQL
TODO
