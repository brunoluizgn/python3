"""Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
entra_hora = input ('Digite a hora em números inteiros: ')

try:
    hora = int(entra_hora)

    #if hora >= 0 and hora <= 11: