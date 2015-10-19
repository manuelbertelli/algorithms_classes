quantidade = int(input('Quantos termos terá sua progressão geométrica? '))
razao = int(input('Qual será a razão? '))
primeiro_termo = int(input('Digite o primeiro termo: '))
termo_atual = primeiro_termo
soma = 0
indice = 0

print('\nOs termos da progressão geométrica são:')

while indice < quantidade:
    print(termo_atual)

    soma = soma + termo_atual
    termo_atual = termo_atual * razao
    indice = indice + 1

print('A soma dos termos é', soma)
