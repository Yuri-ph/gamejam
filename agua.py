import mysql.connector
from mysql.connector import Error
from datetime import datetime

Fator_Gasolina = 0.192
 
CONFIG_BANCO = {
    "host": "127.0.0.1",
    "user": "root",
    "password": "Senac2026@",
    "database": "hackaton"
}

def salvar_calculo_agua(tempo, gasto_banho, gasto_semana):
    try:
        conexao = mysql.connector.connect(**CONFIG_BANCO)
        cursor = conexao.cursor()
 
 
        cursor.execute("INSERT INTO calculos_agua (tempo, gasto_banho, gasto_semana) VALUES (%s, %s, %s)", (tempo, gasto_banho, gasto_semana))
 
        conexao.commit()
        cursor.close()
        conexao.close()
 
        print("Cálculo salvo no banco de dados")
 
    except Error as e:
        print(f"Erro ao salvar dados no banco de dados: {e}")

def CalcularAgua():
    while True:

        while True:
            try:
                tempo = float(input("| Quantos minutos dura o seu banho?: "))

                if tempo <= 0:
                    print("| Digite um número acima de 0!")
                    continue

                break

            except ValueError:
                print("| Apenas números por favor!")

        litros_gastos_minuto = 10

        gasto_banho = tempo * litros_gastos_minuto
        gasto_semana = gasto_banho * 7

        print("__________RESULTADO__________")

        print("| Gasto por banho:", gasto_banho, "litros")
        print("| O gasto semanal é:", gasto_semana, "litros")

        if gasto_banho <= 50:
            print("| 🟢 pouco gasto de água 🟢")
        elif gasto_banho <= 150:
            print("| 🟡 medio gasto de água 🟡")
        else:
            print("| 🔴 muito gasto de água 🔴")

        salvar_calculo_agua(tempo, gasto_banho, gasto_semana)

        continuar = input(
            "| Deseja fazer outro cálculo? (sim/não): "
        ).strip().lower()

        if continuar in ("s", "sim"):
            print("| Reiniciando...")
            continue

        elif continuar in ("n", "nao", "não"):
            print("| Encerrando o programa...")
            break

        else:
            print("| Resposta inválida. Encerrando o programa...")
            break


