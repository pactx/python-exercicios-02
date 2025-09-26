# palavra SECRETA
p = 'PACT'
# Contador de tentativas
c = 0

def linha():
    print('-' * 30)

# cria a lista com '_' para cada letra da palavra
progresso = ['_' for _ in p]
# guarda letras já usadas
usadas = []

while True:
    while True:        
        t = input('Digite uma letra: ').upper().strip()

        # Verifica se digitou apenas uma letra válida
        if len(t) == 1 and t.isalpha():
            if t in usadas:
                print(f'Você já tentou a letra "{t}". Escolha outra.')
            else:
                usadas.append(t)
                c += 1
                break
        else:
            print('Entrada inválida! Digite apenas UMA letra.')

    linha()
    if t in p:
        print(f'A palavra contém a letra {t}')

        # Revela a letra no progresso
        for i, letra in enumerate(p):
            if letra == t:
                progresso[i] = t
    else:
        print(f'A palavra não contém essa letra *')

    # Mostra o progresso atual da forca
    print(' '.join(progresso))

    # Se já montou toda a palavra, acaba
    if '_' not in progresso:
        linha()
        print(f'Parabéns! Você completou a palavra secreta "{p}" com {c} tentativas!')
        linha()
        break

    while True:
        linha()
        continuar = input('Quer tentar advinhar qual foi a palavra secreta? [S/N] ').upper().strip()[0]

        if continuar == 'S':
            a = input('Qual é a palavra secreta? ').upper()
            c += 1
            
            if a == p:
                linha()
                print(f'Parabéns você advinhou a palavra secreta!! Com {c} tentativas.')
                linha()
                exit()
            else:
                linha()
                print('Você errou, tente novamente advinhar a palavra, ou volte para mais dicas de letras.')
        elif continuar == 'N':
            break
        else:
            print('Opção inválida, digite apenas [S]im para continuar ou [N]ão para tentar outra letra.')
            