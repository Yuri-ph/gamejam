import time
import random
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
        print("\n __________MENU__________")
        print("|")
        print("|")
        print("| 1- ")
        print("| 2- ")
        print("| 3- ")
        print("|💡 DICA: ", dica)
        print("|")
        print("|________________________")
        
        escolhaMenu = input("| qual sera sua escolha: ")
        
        if escolhaMenu == "1":
            print("")
            
        if escolhaMenu == "2":
            print("")
            
        if escolhaMenu == "3":
            print("")



menu()