
"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

nome = input('digite seu nome: ')
idade = input('digite sua idade: ')
if idade:
 print(f'seu nome é: {nome}')
 print('Seu nome invertido é: ',nome [::-1])
 print('seu nome não contém espaços', '' in nome)
 print(f'seu nome tem {len(nome)} letras')
 print(f'a primeira letra do seu nome é:',nome[0])
 print(f'a ultima letra do seu nome é:',nome[-1])
else:
    print('não foi digitada a idade depois de voce digitar: ', nome)




