"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

try:
    h = int(input('Quantas hoars são agora? '))
    
    if h == 0 and h <= 11:
        print('Bom dia!')
    elif h >= 12 and h <= 17:
        print('Boa tarde!')
    elif h >= 18 and h <= 23:
        print('Boa noite!')
    else:
        print('O número digitado não é um horário válido.')
        
except ValueError:
    print('Você digitou um valor inválido.')


    
    