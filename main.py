from database import criarBancoDados
from menu import menu
import time

print("CRIANDO BANCO...")
time.sleep(2)

criarBancoDados()

print("ABRINDO MENU...")
menu()