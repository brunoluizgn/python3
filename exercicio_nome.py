nome = input('Digite seu nome: ')
tamanhho_nome = len(nome)

if tamanhho_nome > 1:
    if tamanhho_nome <= 4:
        print('Seu nome é curto')
    elif tamanhho_nome >= 5 and tamanhho_nome <= 6:
        print(' Seu nome é normal')
    else:
        (print(' Seu nome é grande'))    
else:
    print('Por favor, digite mais de uma letra')    