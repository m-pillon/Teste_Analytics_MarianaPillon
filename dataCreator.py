import numpy as np
import pandas as pd

from datetime import date, timedelta
from random import randrange, choice

# Criador/seletor de dados

def generateData(products, dates):
    n = len(dates)
    prod = []
    cat = []
    quant = []
    price = []

    while(n > 0):
        prods = choice(products)
        prod.append(prods[0])
        cat.append(prods[2])
        i = randrange(1, 11)
        quant.append(i)
        price.append(prods[1])
        n -= 1
    
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
