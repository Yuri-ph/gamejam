import time
import random
dicas = [
    "dica 1",
    "dica 2",
    "dica 3"
]

def menu():
    while True:
        dica = random.choice(dicas)
        print(" __________MENU__________")
        print("|")
        print("| 1- ")
        print("| 2- ")
        print("| 3- ")
        print("| 💡", dica)

menu()