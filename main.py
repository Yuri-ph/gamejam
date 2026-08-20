from database import criarBancoDados
from menu import menu
import time

print("CRIANDO BANCO...")
time.sleep(2)

criarBancoDados()
time.sleep(2)

print("ABRINDO MENU...")
menu()