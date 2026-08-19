import os
import time


def menuEnergia():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("__________MENU_DE_ENERGIA__________")
        print("|")
        print("| 1- Calcular energia do banho")
        print("| 2- Calcular energia do ar condicionado")
        print("| 3- Calcular energia da televisão")
        print("| 4- Calcular energia do computador")
        print("| 5- Calcular energia do video game")
        print("| 6- Calcular gasto total de energia")
        print("| 7- Voltar ao menu principal")

        print("|_____________________________________")
        
        escolhaMenuEnergia = input("| qual sera sua escolha: ")
        
        if escolhaMenuEnergia == "1":
            CalculoBanho()
            
        elif escolhaMenuEnergia == "2":
            CalculoAr()

        elif escolhaMenuEnergia == "3":
            CalculoTv()

        elif escolhaMenuEnergia == "4":
            CalculoComputador()

        elif escolhaMenuEnergia == "5":
            CalculoVideoGame()

        elif escolhaMenuEnergia == "6":
            Calculototal()
        elif escolhaMenuEnergia == "7":
            return
        else:
            print("labubu")
def CalculoBanho():
    while True:
        print("| ")
        banhosdiarios = input("| Quantos banhos você toma por dia: ")

        if not banhosdiarios.isdigit():
            print("|")
            print("| Digite um número inteiro válido.")
            time.sleep(2)
            continue

        banhosdiarios = int(banhosdiarios)

        if banhosdiarios < 1:
            print("|")
            print("| O número de banhos deve ser positivo.")
            time.sleep(2)
            continue
        break
    while True:       
        print("|")
        banhotempo = input("| Qual a média de minutos que você toma banho: ")

        if not banhotempo.isdigit():
            print("|")
            print("| O tempo deve ser em minutos inteiros.")
            time.sleep(2)
            continue

        banhotempo = int(banhotempo)

        if banhotempo > 1440:
            print("|")
            print("| O tempo máximo permitido é de 24 horas")
            time.sleep(2)
            continue
                    

        if banhotempo < 1:
            print("|")
            print("| O tempo deve ser positivo.")
            time.sleep(2)
            continue

        calculobanho = (banhotempo / 60)* 550 * banhosdiarios
        print("|")
        print(f"| Seu banho consome diariamente {calculobanho} Wh")
        time.sleep(2)
        return calculobanho
        



def CalculoAr():

    while True:
        artempo = input("| Em média quantas horas por dia você deixa o ar condicionado ligado: ")
        if not artempo.isdigit():
            print("|")
            print("| Digite um número inteiro válido.")
            time.sleep(2)
            continue
        
        artempo = int (artempo)

        if artempo > 24:
            print("|")
            print("| O tempo máximo permitido é de 24 horas")
            time.sleep(2)
            continue

        if artempo <0:
            print("|")
            print("| O tempo não pode ser negativo")
            time.sleep(2)
            continue
        break
    while True:
        print("|")
        temperatura = input("| Qual a temperatura média que o ar condicionado está configurado durante o uso (Digite apenas os numeros): ")
        if not temperatura.isdigit():
            print("|")
            print("| Temperatura deve ser um valor numérico")
            time.sleep(2)
            continue

        temperatura = int(temperatura)

        if temperatura >32:
            print("|")
            print("| A temperatura máxima permitida é de 32°")
            time.sleep(2)
            continue
        


        if temperatura <16:
            print("|")
            print("| A temperatura minima permitida é de 16°")
            time.sleep(2)
            continue

        argasto = 1200 * artempo * ((30 - temperatura) / 10)  

        print(f"| O gasto de energia com o ar condionado é de {argasto} Wh")
        time.sleep(2)
        return argasto


def CalculoTv():
    while True:
        print("|")
        tvtempo = input("\n| Em média quantas horas por dia você deixa a televisão ligada: ")

        if not tvtempo.isdigit():
            print("|")
            print("| Digite um número inteiro válido.")
            time.sleep(2)
            continue
        
        tvtempo = int(tvtempo)

        if tvtempo > 24:
            print("|")
            print("| O tempo maxino é de 24 horas")
            time.sleep(2)
            continue

        if tvtempo < 1:
            print("|")
            print("| O tempo deve ser positivo.")
            time.sleep(2)
            continue

        tvgasto = 100 * tvtempo
        print("|")
        print(f"| Sua televisão consome aproximadamente {tvgasto} Wh por dia")
        time.sleep(2)
        return tvgasto
    

def CalculoComputador():
    while True:
        print("|")
        comptempo = input("| Em média quantas horas por dia você deixa o computador ligado: ")

        if not comptempo.isdigit():
            print("|")
            print("| Digite um número inteiro válido.")
            time.sleep(2)
            continue

        comptempo = int(comptempo)

        if comptempo > 24:
            print("|")
            print("| O tempo máximo é de 24 horas.")
            time.sleep(2)
            continue

        if comptempo < 1:
            print("|")
            print("| O tempo deve ser positivo.")
            time.sleep(2)
            continue

        break

    compgasto = 200 * comptempo
    print("|")
    print(f"| Seu computador consome aproximadamente {compgasto} Wh por dia")
    time.sleep(2)
    return compgasto


def CalculoVideoGame():
    while True:
        print("|")
        gametempo = input("| Em média quantas horas por dia você deixa o video game ligado: ")

        if not gametempo.isdigit():
            print("|")
            print("| Digite um número inteiro válido.")
            time.sleep(2)
            continue

        gametempo = int(gametempo)

        if gametempo > 24:
            print("|")
            print("| O tempo máximo é de 24 horas.")
            time.sleep(2)
            continue

        if gametempo < 1:
            print("|")
            print("| O tempo deve ser positivo.")
            time.sleep(2)
            continue

        gamegasto = 150 * gametempo
        print("|")
        print(f"| Seu video game consome aproximadamente {gamegasto} Wh por dia")
        time.sleep(2)

        return gamegasto

def Calculototal():
    banho = CalculoBanho()
    ar = CalculoAr()
    tv = CalculoTv()
    computador = CalculoComputador()
    videogame = CalculoVideoGame()

    total = banho + ar + tv + computador + videogame

    print("|")
    print(f"| Gasto total diário: {total} Wh")
    
