print('======== CALCULAR MULTAS =====')
print('Onde cirulava o veículo?')
print('Escolha uma opção:')
print('1 - Localidade')
print('2 - Fora da localidade')
print('3 - Autoestrada')
print()
loc = int(input('Introduza o local'))
print('Qual a velocidade do veículo?')
vel = int(input('Introduza a velocidade: '))

if vel <= 50:
    print('Não há multa a pagar.')
    
elif loc == 1:
    if vel > 50 and vel < 90:
        print('A multa a pagar é de 60 euros.')
    elif vel >= 90 and vel < 120:
        print('A multa a pagar é de 120 euros.')
    elif vel >= 120:
        print('A multa a pagar é de 320 euros.')
        
elif loc == 2:
    if vel > 90 and vel < 120:
        print('A multa a pagar é de 60 euros.')
    elif vel >= 120.
        print('A multa a pagar é de 120 euros.')
        


