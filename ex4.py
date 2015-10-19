numero = 1
positivos = 0
negativos = 0

while numero != 0:
    numero = 0
    dado = input('Digite um número inteiro: ')

    numero = int(dado)

    if numero > 0:
        positivos = positivos + numero
    elif numero < 0:
        negativos = negativos + numero

print('O total dos número positivos é', positivos)
print('O total dos números negativos é', negativos)
