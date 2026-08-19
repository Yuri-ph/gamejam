import time
import random
import os
from agua import *
from carbono import *
from energia import *
dicas = [
    "Reduza, Recicle e Reutilize \n| Diminua o consumo de descartáveis, \n| use itens reutilizáveis e separe o lixo reciclável para evitar que materiais vão para aterros",
    "Economize água \n| Feche a torneira ao escovar os dentes, conserte vazamentos e instale redutores de vazão em chuveiros e torneiras",
    "Economize energia \n| Desligue aparelhos quando não estiverem em uso, use lâmpadas LED e aproveite a luz natural ",
    "Economize energia \n| Desligue aparelhos quando não estiverem em uso, use lâmpadas LED e aproveite a luz natural ",
    "Opte por transporte sustentável \n| Prefira bicicleta, transporte público, caronas ou veículos elétricos para reduzir emissões",
    "Consuma de forma consciente \n| Compre produtos locais, orgânicos e com embalagens mínimas; evite marcas que não adotem práticas sustentáveis"
]

def menu():
    while True:
        dica = random.choice(dicas)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("__________MENU__________")
        print("|")
        print("| 1- Calculo de gasto de água")
        print("| 2- Calculo de gasto de energia")
        print("| 3- Calculo de gasto de caborno")
        print("|")
        print("|💡 DICA: ", dica)
        print("|")
        print("|________________________")
        
        escolhaMenu = input("| qual sera sua escolha: ")
        
        if escolhaMenu == "1":
            CalcularAgua()
            
        elif escolhaMenu == "2":
            menuEnergia()
            
        # if escolhaMenu == "3":
        #     CalculoCarbono()

        else:
            print("| Opção inválida!")
            time.sleep(2)
        


menu()
