minimo = int(input('Digite o valor mínimo: '))
maximo = 0

while maximo < minimo:
    maximo = int(input('Digite o valor máximo: '))

    if maximo < minimo:
        print('Valor máximo tem que ser maior que o mínimo')

print('Os valores divisíveis por 5 são:')

indice = minimo

while indice <= maximo:
    if indice % 5 == 0:
        print(indice)

    indice = indice + 1
