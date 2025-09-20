"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""


n = str(input('Qual é o seu nome? '))

if len(n) <= 4:
    print('Seu nome é curto.')
elif len(n) > 6:
    print('Seu nome é MUITO GRANDE..')
else:
    print('Seu nome é normal.')

