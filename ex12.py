print('========= T A B U A D A ==========')

tabuada = 1

while tabuada > 0:
    tabuada = int(input('Quer ver a tabuada de qual número? ("0" para sair) '))

    if tabuada > 0:
        print('==== Tabuada do', tabuada, '====')

        indice = 1

        while indice <= 10:
            print(tabuada, 'x', indice, '=', tabuada * indice)
            indice = indice + 1

        print('================================')
