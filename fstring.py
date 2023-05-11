"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal 
(caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
Sinal - + ou - 
Ex.: 0>-100, .1f
Conversion flags - !r !s !a
= - força o numero aparecer antes dos zeros
"""
Variavel = "ABC"
print(f'{Variavel}')
print(f'{Variavel: >10}')
print(f'{Variavel: <10}.')
print(f'{Variavel: ^10}')
print(f'{10000.45465545454546:.1f}')
print(f'O hexadecimal de 1500 é {1500:08X}')

