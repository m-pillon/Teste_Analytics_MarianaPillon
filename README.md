# Teste de Analytics - Mariana Pillon

## Rodando o projeto
### Instalando dependências
As dependências estão em *requirements.txt*. Os requirements incluem _apenas_ bibliotecas necessárias para o projeto. Para instala-las, digite no terminal:
> $ `pip install -r requirements.txt`

Muitas delas são para rodar um arquivo do tipo Jupyter Notebook (.ipynb).

### Rodando o projeto
Rodar o projeto com este comando deveria ser o suficiente para gerar todos os arquivos e [TODO] imagens.
> $ `python main.py`

No entanto, é mais interessante ver o que eu fiz passo a passo. Para isso, [TODO] incluirei arquivos do tipo .ipynb e seus respectivos .pdf's para visualização.

## Parte 1: Criação e análise de dados
**Sobre os dados**: 
* Foi simulado o controle de vendas de uma padaria
* Cada entrada se refere a apenas um produto, identificado por seu nome;
* Há 8 produtos possíveis, com preços de R$1,00 a R$4,50 (fixos)
* O número de unidades do produto compradas (quantidade) vai de 1 a 10

**Limpeza de dados**:
* Não há dados faltantes no CSV original, porém, criei o arquivo *fake_missing_data.csv* e retirei alguns dados manualmente. Aqui estão minhas estratégias para dados faltantes:
  * Para o preço: copiar o preço da venda anterior ao dado faltante daquele produto;
  * Para a categoria: basta olhar o produto, já que sempre depende dele;
  * Para a quantidade: média, moda ou mediana, dependendo de outras métricas;
  * Para o nome do produto: predição com base na categoria e preço;
  * Para a data: se for importante para a análise, tirar aquela linha; se não, ignorar a coluna data;

## Parte 2: SQL
TODO
