"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

cpf_mask = "___.___.___-__"

def linha():
    print('-='*30)

def format_cpf(text):
    digits = "".join(c for c in text if c.isdigit())
    masked = ""
    mask_index = 0
    for d in digits:
        while mask_index < len(cpf_mask) and cpf_mask[mask_index] != "_":
            masked += cpf_mask[mask_index]
            mask_index += 1
        masked += d
        mask_index += 1
    masked += cpf_mask[mask_index:]
    return masked

while True:
    cpf = input("Digite o CPF que deseja verificar (apenas números): ")
    linha()
    cpf_digits = "".join(c for c in cpf if c.isdigit())
    if len(cpf_digits) == 11:
        cpf = cpf_digits
        break
    print("Erro: digite exatamente 11 números.")
    linha()


print("CPF digitado:", format_cpf(cpf))

base = cpf[:9]

soma = sum(int(numero) * (10 - i) for i, numero in enumerate(base))
resto = (soma * 10) % 11
digito1 = 0 if resto > 9 else resto

base += str(digito1)
soma = sum(int(numero) * (11 - i) for i, numero in enumerate(base))
resto = (soma * 10) % 11
digito2 = 0 if resto >= 9 else resto

if cpf[-2:] == f"{digito1}{digito2}":
    linha()
    print("✅ CPF válido!")
    linha()
else:
    linha()
    print("❌ CPF inválido!")
    linha()