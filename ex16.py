entrada = input('Deseja imprimir quantos termos da sequência de Fibonacci? ')
quantidade = int(entrada)

if quantidade > 0:
    if quantidade >= 1:
        print(0)
    if quantidade >= 2:
        print(1)
    if quantidade >= 3:
        print(1)
        termo_anterior = 1
        termo_atual = 1

        indice = 3
        
        while indice < quantidade:
            termo = termo_atual + termo_anterior
            print(termo)

            termo_anterior = termo_atual
            termo_atual = termo
            indice = indice + 1
