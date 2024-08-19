# driver code
from dataCreator import *

from random import seed

if __name__ == '__main__':
    # Cenario: padaria
    # criacao do dataframe
    # como ele eh aleatorio, faço isso pra garantir que vai sempre gerar o mesmo
    seed(10)
    # numero de produtos
    
    # para nao gerar o mesmo dataset toda vez
    recriate = False
    if (recriate):
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
