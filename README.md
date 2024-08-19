# Teste de Analytics - Mariana Pillon

## **Índice**
- [Como rodar o projeto](#como-rodar)
  - [Instalando Dependências](#instalando-dependências)
  - [Rodando o projeto](#rodando-o-projeto)
- [Parte 1: Análise de dados](#parte-1-criação-e-análise-de-dados)
  - [Sobre os dados](#sobre-os-dados)
  - [Limpeza de dados](#limpeza-de-dados)
  - [Análise de dados](#análise-de-dados)
- [Parte 2: SQL](#parte-2-sql)

## Como rodar
### Instalando dependências
As dependências estão em *requirements.txt*. Os requirements incluem _apenas_ bibliotecas necessárias para o projeto. Para instala-las, digite no terminal:
> $ `pip install -r requirements.txt`

Muitas delas são para rodar um arquivo do tipo Jupyter Notebook (.ipynb).

### Rodando o projeto
Rodar o projeto com este comando deveria ser o suficiente para gerar todos os arquivos e [TODO] imagens.
> $ `python main.py`

No entanto, é mais interessante ver o que eu fiz passo a passo. Para isso, incluí arquivos do tipo .ipynb (e seus respectivos .pdf's para visualização).
*Para rodar o arquivo do tipo Jupyter Notebook (ipynb), ver arquivo `explicacoes.md`.*

## Parte 1: Criação e análise de dados
### Sobre os dados: 
* Foi simulado o controle de vendas de uma padaria
* Cada entrada se refere a apenas um produto, identificado por seu nome;
* Há 8 produtos possíveis, com preços de R$1,00 a R$4,50 (fixos)
* O número de unidades do produto compradas (quantidade) vai de 1 a 10

Toda as funções de criação estão em *data_creator.py*

### Limpeza de dados:
Toda a limpeza está em *data_cleaning.ipynb*, mas pode também ser visualizada em *data_cleaning.pdf*. As funções importantes estão na main, mas como o dataset *data_clean.csv* já foi gerado no notebook, elas estão comentadas.

### Análise de dados
Toda a análise está em *data_analysis.ipynb*, mas as funções importantes foram replicadas na main. Estão comentadas, assim como a limpeza, para não gerar os arquivos novamente.

## Parte 2: SQL
TODO
