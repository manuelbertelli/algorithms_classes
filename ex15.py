entrada = input('Digite um número: ')
indice = 1
numero = int(entrada)
primo = True

while indice <= numero and primo:
    indice = indice + 1
    
    if numero % indice == 0 and numero != indice:
        primo = False
        print('Não é primo')

if primo:
    print('É primo')
        
        
    
