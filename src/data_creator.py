import numpy as np
import pandas as pd

from datetime import date, timedelta
from random import randrange, choice

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

# Criador/seletor de dados
# gera colunas (listas) de dados
def generateData(products, dates):
    n = len(dates)
    prod = []
    cat = []
    quant = []
    price = []

    # escolhe um produto aleatoriamente cada vez
    while(n > 0):
        prods = choice(products)
        prod.append(prods[0])
        cat.append(prods[2])
        i = randrange(1, 11)
        quant.append(i)
        price.append(prods[1])
        n -= 1
    
    # gera um dataframe e salva em um csv
    lst = [dates, prod, cat, quant, price]
    data = np.array(lst)
    columns = ['Data', 'Produto', 'Categoria', 'Quantidade', 'Preço']
    df = pd.DataFrame(data.transpose(), columns=columns)
    df.to_csv('fake_data.csv')

# gera um numero aleatorio de 0 a 365-1
# soma esse numero de dias a data inicial (01/01/2023)
# retorna uma lista com k datas no ano de 2023
def randomDates(k):
    d1 = date(2023, 1, 1)

    dates = []
    while k > 0:
        i = randrange(0, 365)
        d = d1 + timedelta(days=i)
        dates.append(d)
        k -= 1

    return dates
