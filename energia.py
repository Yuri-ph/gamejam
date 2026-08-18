
def menuEnergia():
    while True:
        print("\n __________MENU_DE_ENERGIA__________")
        print("|")
        print("| 1- Calcular energia do banho")
        print("| 2- Calcular energia do ar condicionado")
        print("|")
        print("|_____________________________________")
        
        escolhaMenu = input("| qual sera sua escolha: ")
        
        if escolhaMenu == "1":
            CalculoBanho()
            
        if escolhaMenu == "2":
            CalculoAr()
            
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
        artempo = input("Em média quantas horas por dia você deixa o ar condicionado ligado")
        if not artempo.isdigit():
            print("\nDigite um número inteiro válido.\n")
            continue

        artempo = int (artempo)

        if artempo <0:
            print("O tempo não pode ser negativo")
            continue
        break
    while True:
        temperatura = input("Qual a temperatura média que o ar condicionado está configurado durante o uso")
        if not temperatura.isdigit():
            print(temperatura)

        



    



