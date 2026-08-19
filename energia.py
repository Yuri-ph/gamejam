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

        print("|_____________________________________")
        
        escolhaMenuEnergia = input("| qual sera sua escolha: ")
        
        if escolhaMenuEnergia == "1":
            CalculoBanho()
            
        if escolhaMenuEnergia == "2":
            CalculoAr()

        if escolhaMenuEnergia == "3":
            CalculoTv()

        if escolhaMenuEnergia == "4":
            CalculoComputador()

        if escolhaMenuEnergia == "5":
            CalculoVideoGame()

        if escolhaMenuEnergia == "6":
            return 

        else:
            print("| opção inválida")
            print("| voltando para o menu principal...")
            time.sleep(2)
            return menuEnergia()
            
def CalculoBanho():
    while True:
        print("| ")
        banhosdiarios = input("| Quantos banhos você toma por dia: ")

        if not banhosdiarios.isdigit():
            print("|")
            print("| Digite um número inteiro válido.")
            time.sleep(2)
            return menuEnergia()

        banhosdiarios = int(banhosdiarios)

        if banhosdiarios < 1:
            print("|")
            print("| O número de banhos deve ser positivo.")
            time.sleep(2)
            return menuEnergia()
        break
    while True:       
        print("|")
        banhotempo = input("| Qual a média de minutos que você toma banho: ")

        if not banhotempo.isdigit():
            print("|")
            print("| O tempo deve ser em minutos inteiros.")
            time.sleep(2)
            return menuEnergia()

        banhotempo = int(banhotempo)

        if banhotempo >= 1440:
                    print("|")
                    print("| O tempo máximo permitido é de 24 horas")
                    time.sleep(2)
                    return menuEnergia()

        if banhotempo < 1:
            print("|")
            print("| O tempo deve ser positivo.")
            time.sleep(2)
            return menuEnergia()

        calculobanho = banhotempo * 550 * banhosdiarios
        print("|")
        print(f"| Seu banho consome diariamente {calculobanho} W")
        time.sleep(2)
        return menuEnergia()
        



def CalculoAr():

    while True:
        artempo = input("| Em média quantas horas por dia você deixa o ar condicionado ligado: ")
        if not artempo.isdigit():
            print("|")
            print("| Digite um número inteiro válido.")
            time.sleep(2)
            return menuEnergia()
        
        artempo = int (artempo)

        if artempo > 24:
            print("|")
            print("| O tempo máximo permitido é de 24 horas")
            time.sleep(2)
            return menuEnergia()

        if artempo <0:
            print("|")
            print("| O tempo não pode ser negativo")
            time.sleep(2)
            return menuEnergia()
        break
    while True:
        print("|")
        temperatura = input("| Qual a temperatura média que o ar condicionado está configurado durante o uso (Digite apenas os numeros): ")
        if not temperatura.isdigit():
            print("|")
            print("| Temperatura deve ser um valor numérico")
            time.sleep(2)
            return menuEnergia()

        temperatura = int(temperatura)

        if temperatura >32:
            print("|")
            print("| A temperatura máxima permitida é de 32°")
            time.sleep(2)
            return menuEnergia()
        


        if temperatura <16:
            print("|")
            print("| A temperatura minima permitida é de 16°")
            time.sleep(2)
            return menuEnergia()

        argasto = 1200 * artempo * ((30 - temperatura) / 10)  

        print(f"| O gasto de energia com o ar condionado é de {argasto} W")
        time.sleep(2)
        return menuEnergia


def CalculoTv():
    while True:
        print("|")
        tvtempo = input("| Em média quantas horas por dia você deixa a televisão ligada: ")

        if not tvtempo.isdigit():
            print("|")
            print("| Digite um número inteiro válido.")
            time.sleep(2)
            return menuEnergia()
        
        tvtempo = int(tvtempo)

        if tvtempo > 24:
            print("|")
            print("| O tempo maxino é de 24 horas")
            time.sleep(2)
            return menuEnergia()

        if tvtempo < 1:
            print("|")
            print("| O tempo deve ser positivo.")
            time.sleep(2)
            return menuEnergia()

        tvgasto = 100 * tvtempo
        print("|")
        print(f"| Sua televisão consome aproximadamente {tvgasto} Wh por dia")
        time.sleep(2)
        return menuEnergia
    

def CalculoComputador():
    while True:
        print("|")
        comptempo = input("| Em média quantas horas por dia você deixa o computador ligado: ")

        if not comptempo.isdigit():
            print("|")
            print("| Digite um número inteiro válido.")
            time.sleep(2)
            return menuEnergia()

        comptempo = int(comptempo)

        if comptempo > 24:
            print("|")
            print("| O tempo máximo é de 24 horas.")
            time.sleep(2)
            return menuEnergia()

        if comptempo < 1:
            print("|")
            print("| O tempo deve ser positivo.")
            time.sleep(2)
            return menuEnergia()

        break

    compgasto = 200 * comptempo
    print("|")
    print(f"| Seu computador consome aproximadamente {compgasto} Wh por dia")
    time.sleep(2)


def CalculoVideoGame():
    while True:
        print("|")
        gametempo = input("| Em média quantas horas por dia você deixa o video game ligado: ")

        if not gametempo.isdigit():
            print("|")
            print("| Digite um número inteiro válido.")
            time.sleep(2)
            return menuEnergia()

        gametempo = int(gametempo)

        if gametempo > 24:
            print("|")
            print("| O tempo máximo é de 24 horas.")
            time.sleep(2)
            return menuEnergia()

        if gametempo < 1:
            print("|")
            print("| O tempo deve ser positivo.")
            time.sleep(2)
            return menuEnergia()

        gamegasto = 150 * gametempo
        print("|")
        print(f"| Seu video game consome aproximadamente {gamegasto} Wh por dia")
        time.sleep(2)

        break

def Calculotota():
    calculototal = CalculoAr + CalculoBanho + CalculoComputador + CalculoTv + CalculoVideoGame

    print(calculototal)
    
