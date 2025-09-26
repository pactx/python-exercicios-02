"""
faça uma lista de comprar com listas;
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista. 
Não permita que o programa quebre 
com erros de índice inexistentes na lista
"""
import os

def linha():
    print('-='*30)

lista = []

while True:
    linha()
    Opção = str(input('Selecione uma opção: ' \
    '[I]nserir: ' \
    '[A]pagar: ' \
    '[L]istar: ' \
    '[S]air: ')).upper()[0]

    if Opção == 'I':
        os.system('cls')
        linha()
        print(f'{"Adicionando os items..":^60}')
        linha()
        
        if lista:
            for i, item_dicionario in enumerate(lista):
                indice = i
                nome = item_dicionario['item']
                valor = item_dicionario['valor']
                print(f'{indice:<25} {nome:<24} R$ {valor:.2f}')
            linha()

        dicionário = {}

        dicionário['item'] = str(input('Qual item deseja inserir? '))
        dicionário['valor'] = float(input(f'Qual o valor da(o) {dicionário['item']}? R$ '))
        lista.append(dicionário)
        print(f'\nItem {dicionário['item'].upper()} adicionado com sucesso!')

    elif Opção == 'A':
        os.system('cls')
        linha()
        print(f'{"Qual item da lista você deseja apagar? ":^60}')
        linha()
        for i, item_dicionario in enumerate(lista):
            indice = i
            nome = item_dicionario['item']
            valor = item_dicionario['valor']
            print(f'{indice:<25} {nome:<24} R$ {valor:.2f}')
        linha()

        try:
            apagar = int(input('Qual o número do item você deseja apagar? '))            

            if 0 <= apagar < len(lista):
                nome_do_item = lista[apagar]['item']
                while True:
                    resposta = str(input(f'Tem certeza que deseja apagar {nome_do_item.upper()}? [S]im/[N]ão: ')).upper()[0]
                    if resposta == 'S':
                        lista.pop(apagar)
                        print(f'\nItem removido com sucesso!')
                        break
                    elif resposta == 'N':
                        print('\nOperação cancelada.')
                        break
                    else:
                        print('Resposta inválida.')
            else:
                print('Erro: Esse número não corresponde a nenhum item da lista.')

        except ValueError:
            print('Erro: Por favor, digite um número válido.')

    elif Opção == 'L':
        os.system('cls')
        linha()
        print(f'{"Lista de Compras":^60}')
        linha()

        if not lista:
            print("Sua lista de compras está vazia.".center(60))
        else:
            total_compra = 0.0

            for i, item_dicionario in enumerate(lista):
                indice = i
                nome = item_dicionario['item']
                valor = item_dicionario['valor']
                print(f'{indice:<25} {nome:<24} R$ {valor:.2f}')
                
                total_compra += valor            
            linha()

            print(f'{"TOTAL:":<50} R$ {total_compra:.2f}')
    
    elif Opção == 'S':
        linha()
        print(f'{"Encerrando.. Até a próxima ! ":^60}')
        linha()
        exit()

    
    else:
        linha()
        print(f'{"Opção inválida tente novamente!":^60}')
        continue 