primeira_vez = True
valor = 1
maior = 0
menor = 0
quantidade = 0
soma = 0
media = 0

while valor > 0:
    entrada = input('Insira um valor positivo inteiro (0 ou negativo para terminar): ')
    valor = int(entrada)
    
    if valor > 0:
        quantidade = quantidade + 1
        soma = soma + valor
        
        if primeira_vez:
            maior = valor
            menor = valor
            primeira_vez = False
        else:
            if valor < menor:
                menor = valor
            elif valor > maior:
                maior = valor

if quantidade > 0:
    print('========= RESULTADOS =========')
    print('Menor valor:', menor)
    print('Maior valor:', maior)
    print('Quantidade de valores:', quantidade)
    print('Soma dos valores:', soma)
    print('Média dos valores:', soma / quantidade)
    print('==============================')
