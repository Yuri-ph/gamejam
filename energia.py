def CalculoBanho():
    while True:
        banhosdiarios = input("Quantos banhos você toma por dia: ")

        if not banhosdiarios.isdigit():
            print("\nDigite um número inteiro válido.\n")
            continue

        banhosdiarios = int(banhosdiarios)

        if banhosdiarios < 1:
            print("\nO número de banhos deve ser positivo.\n")
            continue
        break
    while True:       
        banhotempo = input("\nQual a média de minutos que você toma banho: ")

        if not banhotempo.isdigit():
            print("\nO tempo deve ser em minutos inteiros.")
            continue

        banhotempo = int(banhotempo)

        if banhotempo < 1:
            print("\nO tempo deve ser positivo.")
            continue

        calculobanho = banhotempo * 550 * banhosdiarios

        print(f"\nSeu banho consome diariamente {calculobanho} W")

        print(f"\nSeu banho consome semanalmente {calculobanho * 7}")
        break
        

CalculoBanho()

def CalculoAr():
    while True:
        artempo = input("Quanto tempo você deixa em média o ar condicionado ligado por dia")
        if not artempo.isdigit():
            print("\nDigite um número inteiro válido.\n")
            continue

        artempo = int (artempo)

        if artempo <0:
            print("O tempo não pode ser negativo")
            continue
        break

        



    

