while True:    
    print('======== CALCULAR MULTAS =====')
    print('Onde cirulava o veículo?')
    print('Escolha uma opção:')
    print('1 - Localidade')
    print('2 - Fora da localidade')
    print('3 - Autoestrada')
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
        elif vel >= 120:
            print('A multa a pagar é de 120 euros.')
            
    elif loc == 3:
        if vel > 120 and vel <= 150:
            print('A multa a pagar é de 60 euros.')
        elif vel > 150 and vel <= 175:
            print('A multa a pagar é de 120 euros.')
        elif vel > 175:
            print('A multa a pagar é de 360 euros.')

    print()
    continuar = input('Deseja continuar? (s/n): ')
    if continuar.lower() != 's':
        print('Adeus!')
        break
