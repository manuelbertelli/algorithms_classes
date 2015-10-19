soma = 0
numeros = int(input('Digite quantos números quer somar: '))

while numeros > 0:
    valor = int(input('Digite o ' + str(numeros) + ' número a somar: '))

    if valor > 0:
        soma = soma + valor

    numeros = numeros - 1

print('O valor da soma dos positivos é', soma)
