numero = 1

while numero != 0:
    dado = input('Digite um número inteiro ("0" para sair): ')
    por_2 = False
    por_3 = False

    numero = int(dado)

    if numero != 0:
        if numero % 2 == 0:
            por_2 = True
        if numero % 3 == 0:
            por_3 = True

        if por_2 and por_3:
            print('Número', numero, 'é divisível por 2 ou 3')
        elif por_2:
            print('Número', numero, 'é divisível por 2')
        elif por_3:
            print('Número', numero, 'é divisível por 3')
        else:
            print('Número', numero, 'não é divisível por 2 ou 3')
