# Algumas explicações sobre o código

## Rodando arquivos do tipo .IPYNB
Para rodar um arquivo do tipo .ipynb, é possível:
- Baixar a extensão 'Jupyter' da Microsoft para o Visual Studio Code, ou
- Rodar o projeto no servidor do Jupyter Notebook localmente

Para rodar localmente, digite no terminal:
> $ `jupyter notebook`

Isso vai abrir a pasta atual em localhost:8888 no navegador. 

## Limpeza de dados
* Não há dados faltantes no CSV original, porém, criei o arquivo *fake_missing_data.csv* e retirei alguns dados manualmente. Aqui estão minhas estratégias para dados faltantes:
  * Para o preço: copiar o preço da venda anterior ao dado faltante daquele produto;
  * Para a categoria: basta olhar o produto, já que sempre depende dele;
  * Para a quantidade: média, moda ou mediana, dependendo de outras métricas;
  * Para o nome do produto: predição com base na categoria e preço;
  * Para a data: se for importante para a análise, tirar aquela linha; se não, ignorar a coluna data;

## Análise de dados
* Uma nova coluna, Total gasto, com Quantidade * Preço, foi criada;
* Foi criado um pequeno dataset com a receita que cada produto gerou (não foi salvo em .CSV);
* Os gráficos de pizza foram gerados a partir desse dataset e salvos na pasta `figures`
* Foi feita outra operação de agrupamento para verificar as vendas em cada mês. Esses dados foram plotados com matplotlib e a figura foi salva junto com as outras imagens.