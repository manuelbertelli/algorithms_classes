quantidade = int(input('Quantos números você quer analisar? '))
menor = 0
maior = 0
indice = 1
primeira_vez = True

while indice <= quantidade:
    numero = int(input('Digite o ' + str(indice) + ' número: '))

    if numero > 0:
        if primeira_vez:
            menor = numero
            maior = numero
            primeira_vez = False
        else:
            if numero < menor:
                menor = numero
            elif numero > maior:
                maior = numero

    indice = indice + 1

if menor == 0 and maior == 0:
    print('Nenhum número positivo foi digitado')
else:
    print('O menor número foi', menor, 'e o maior foi', maior)
