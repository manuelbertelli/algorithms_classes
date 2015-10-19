quantidade = int(input('Deseja imprimir quantos termos da sequência de Fibonacci? '))
termo_inicial = int(input('Digite o termo inicial: '))

if quantidade > 0:
    if quantidade >= 1 and termo_inicial <= 0:
        print(0)
    if quantidade >= 2 and termo_inicial <= 1:
        print(1)
    if quantidade >= 3:
        if termo_inicial <= 1:
            print(1)

        termo_anterior = 1
        termo_atual = 1

        indice = 3
        
        while indice < quantidade:
            termo = termo_atual + termo_anterior

            if termo >= termo_inicial:
                print(termo)

            termo_anterior = termo_atual
            termo_atual = termo
            indice = indice + 1
