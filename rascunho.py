lista = ['Maria', 'helena', 'Luiz']


def traço():
    print('-'*30)


# for i, name in enumerate(lista):
#     print(i, name)

traço()
# Itera de 0 até o comprimento da lista - 1
for i in range(len(lista)):
    # Usa o índice 'i' para acessar o nome na lista
    nome = lista[i]
    print(i, nome)
traço()