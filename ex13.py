limite = 100
pulos = 2
faixa = limite - 1
soma = 2

while faixa < limite:
    faixa = int(input('Digite um número maior ou igual a ' + str(limite) + ': '))

    if faixa >= limite:
        indice = pulos
        
        while indice < faixa:
            indice = indice + pulos
            soma = soma + indice

        print('Soma dos pares é igual a', soma)
    else:
        print('Número menor que', limite)
        
        
