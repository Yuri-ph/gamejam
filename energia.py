def CalculoBanho():
    banhosdiarios = input("Quantos banhos você toma por dia: ")

    if not banhosdiarios.isdigit():
        print("Digite um número inteiro válido.\n")
        return

    banhosdiarios = int(banhosdiarios)

    if banhosdiarios < 1:
        print("O número de banhos deve ser positivo.\n")
        return

    banhotempo = input("\nQual a média de minutos que você toma banho: ")

    if not banhotempo.isdigit():
        print("O tempo deve ser em minutos inteiros.\n")
        return

    banhotempo = int(banhotempo)

    if banhotempo < 1:
        print("O tempo deve ser positivo.\n")
        return

    calculobanho = banhotempo * 550 * banhosdiarios

    print(f"\nSeu banho consome diariamente {calculobanho} W\n")


CalculoBanho()

def calcular():
    print("")