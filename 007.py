from rich import print

perguntas = [
    {
        'Pergunta': 'Quanto é 2 + 2 ?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5 * 5 ?',
        'Opções': ['25', '55', '10', '51', '5'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10 / 2 ?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

for pergunta in perguntas:
    print(f"[yellow]{pergunta['Pergunta']}[/]")

    for indice, opcao in enumerate(pergunta['Opções']):
        letra = chr(65 + indice)
        print(f"{letra}) {opcao}")

    escolha = input("Escolha uma opção: ").upper()
    indice = ord(escolha) - 65

    if pergunta['Opções'][indice] == pergunta['Resposta']:
        print("[green]✅ Acertou ![/]\n")
    else:
        print("[red]❌ Errou ![/]\n")