quantidade = int(input('Quantos números você quer analisar? '))
menor = 0
maior = 0
indice = 1

while indice <= quantidade:
    numero = int(input('Digite o ' + str(indice) + ' número: '))

    if numero < menor or indice == 1:
        menor = numero
    elif numero > maior:
        maior = numero

    indice = indice + 1

print('O menor número foi', menor, 'e o maior foi', maior)
