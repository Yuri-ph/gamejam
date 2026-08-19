
def menuEnergia():
    while True:
        print("__________MENU_DE_ENERGIA__________")
        print("|")
        print("| 1- Calcular energia do banho")
        print("| 2- Calcular energia do ar condicionado")
        print("| 3- Calcular energia da televisão")
        print("| 4- Calcular energia do computador")
        print("| 5- Calcular energia do video game")

        print("|_____________________________________")
        
        escolhaMenu = input("| qual sera sua escolha: ")
        
        if escolhaMenu == "1":
            CalculoBanho()
            
        elif escolhaMenu == "2":
            CalculoAr()

        elif escolhaMenu == "3":
            CalculoTv()

        elif escolhaMenu == "4":
            CalculoComputador()

        elif escolhaMenu == "5":
            CalculoVideoGame()
            
def CalculoBanho():
    while True:
        banhosdiarios = input("| Quantos banhos você toma por dia: ")

        if not banhosdiarios.isdigit():
            print("|")
            print("| Digite um número inteiro válido.")
            continue

        banhosdiarios = int(banhosdiarios)

        if banhosdiarios < 1:
            print("|")
            print("| O número de banhos deve ser positivo.")
            continue
        break
    while True:       
        print("|")
        banhotempo = input("| Qual a média de minutos que você toma banho: ")

        if not banhotempo.isdigit():
            print("|")
            print("| O tempo deve ser em minutos inteiros.")
            continue

        banhotempo = int(banhotempo)

        if banhotempo >= 1440:
                    print("|")
                    print("| O tempo máximo permitido é de 24 horas")
                    continue

        if banhotempo < 1:
            print("|")
            print("| O tempo deve ser positivo.")
            continue

        calculobanho = banhotempo * 550 * banhosdiarios
        print("|")
        print(f"| Seu banho consome diariamente {calculobanho} W")

        break
        



def CalculoAr():

    while True:
        artempo = input("| Em média quantas horas por dia você deixa o ar condicionado ligado: ")
        if not artempo.isdigit():
            print("|")
            print("| Digite um número inteiro válido.")
            continue
        
        artempo = int (artempo)

        if artempo > 24:
            print("|")
            print("| O tempo máximo permitido é de 24 horas")

        if artempo <0:
            print("|")
            print("| O tempo não pode ser negativo")
            continue
        break
    while True:
        print("|")
        temperatura = input("| Qual a temperatura média que o ar condicionado está configurado durante o uso (Digite apenas os numeros): ")
        if not temperatura.isdigit():
            print("|")
            print("| Temperatura deve ser um valor numérico")
            continue

        temperatura = int(temperatura)

        if temperatura >32:
            print("|")
            print("| A temperatura máxima permitida é de 32°")
            continue

        if temperatura <16:
            print("|")
            print("| A temperatura minima permitida é de 16°")
            continue

        argasto = 1200 * artempo * ((30 - temperatura) / 10)  

        print(f"| O gasto de energia com o ar condionado é de {argasto} W")
        break

def CalculoTv():
    while True:
        print("|")
        tvtempo = input("| Em média quantas horas por dia você deixa a televisão ligada: ")

        if not tvtempo.isdigit():
            print("|")
            print("| Digite um número inteiro válido.")
            continue
        
        tvtempo = int(tvtempo)

        if tvtempo > 24:
            print("|")
            print("| O tempo maxino é de 24 horas")
            continue

        if tvtempo < 1:
            print("|")
            print("| O tempo deve ser positivo.")
            continue

        tvgasto = 100 * tvtempo
        print("|")
        print(f"| Sua televisão consome aproximadamente {tvgasto} Wh por dia")

        break

def CalculoComputador():
    while True:
        print("|")
        comptempo = input("| Em média quantas horas por dia você deixa o computador ligado: ")

        if not comptempo.isdigit():
            print("|")
            print("| Digite um número inteiro válido.")
            continue

        comptempo = int(comptempo)

        if comptempo > 24:
            print("|")
            print("| O tempo máximo é de 24 horas.")
            continue

        if comptempo < 1:
            print("|")
            print("| O tempo deve ser positivo.\n")
            continue

        break

    compgasto = 200 * comptempo
    print("|")
    print(f"| Seu computador consome aproximadamente {compgasto} Wh por dia")


def CalculoVideoGame():
    while True:
        print("|")
        gametempo = input("| Em média quantas horas por dia você deixa o video game ligado: ")

        if not gametempo.isdigit():
            print("|")
            print("| Digite um número inteiro válido.")
            continue

        gametempo = int(gametempo)

        if gametempo > 24:
            print("|")
            print("| O tempo máximo é de 24 horas.")
            continue

        if gametempo < 1:
            print("|")
            print("| O tempo deve ser positivo.")
            continue

        gamegasto = 150 * gametempo
        print("|")
        print(f"| Seu video game consome aproximadamente {gamegasto} Wh por dia")

        break
def Caulacompleto(gamegasto,):