# driver code
from dataCreator import *


# Dados a criar:
# ID, Data, Produto, Categoria, Quantidade, Preco
# Produtos, preco, categoria: Lista pre definida (main)
# Quantidade 1 a 10
# Data: 01/01/2023 a 31/12/2023
# Um ID (entrada) = venda uma ou mais unidades
#     de um mesmo produto
#     o pandas ja cria isso por padrao
# Os dados sao colocados em um dicionario
#     e depois salvos em um arquivo CSV


if __name__ == '__main__':
    # Cenario: padaria

    # numero de produtos
    n = 200
                # produto     preco  categoria
    products = [['Bread roll', 1.50, 'bread'],
                ['Bread loaf', 4.50, 'bread'],
                ['Cake slice', 3.50, 'slice'],
                ['Pie slice', 4.00, 'slice'],
                ['Chicken sandwich', 3.00, 'sandwich'],
                ['Veggie sandwich', 2.80, 'sandwich'],
                ['Chocolate bar', 2.00, 'ready-made'],
                ['Mints', 1.00, 'ready-made']]

    dates = randomDates(n)

    generateData(products, dates)
