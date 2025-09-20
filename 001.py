"""
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""


try:
    n = int(input('Digite um número: '))

except ValueError:
    print(f'O numero digitado não é um número inteiro.')

else:
    if n % 2 == 0:
        print(f'O número {n} é um número inteiro PAR.')
    else:
        print(f'O número {n} é um número inteiro IMPAR.')