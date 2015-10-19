categoria = ''
dado = 0
peso = 0

while peso <= 0:
    dado = input('Digite o peso do boxeador:')
    peso = int(dado)

    if peso <= 0:
        print('Peso inválido')
 
if peso < 65:
    categoria = 'Pena'
elif peso >= 65 and peso < 72:
    categoria = 'Leve'
elif peso >= 72 and peso < 79:
    categoria = 'Ligeiro'
elif peso >= 79 and peso < 86:
    categoria = 'Meio médio'
elif peso >= 86 and peso < 93:
    categoria = 'Médio'
elif peso >= 93 and peso < 100:
    categoria = 'Meio pesado'
elif peso >= 100:
    categoria = 'Pesado'
    
print('Boxeador lutará na categoria', categoria)
