import mysql.connector
from mysql.connector import Error



 
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

def consultarAgua():
    try:
        conexao = mysql.connector.connect(**CONFIG_BANCO)
        cursor = conexao.cursor()

        cursor.execute("""
            SELECT
                id_agua,
                tempo,
                gasto_banho,
                gasto_semana
            FROM calculos_agua
            ORDER BY id_agua DESC
        """)

        resultados = cursor.fetchall()

        print("\n__________CÁLCULOS DE ÁGUA__________")

        if not resultados:
            print("| Nenhum cálculo encontrado.")
        else:
            for registro in resultados:
                print("|--------------------------------")
                print(f"| ID: {registro[0]}")
                print(f"| Tempo do banho: {registro[1]} minutos")
                print(f"| Gasto por banho: {registro[2]} litros")
                print(f"| Gasto semanal: {registro[3]} litros")

            print("|--------------------------------")

        cursor.close()
        conexao.close()

    except Error as e:
        print(f"| Erro ao consultar dados: {e}")

    input("| Pressione ENTER para continuar...")

def atualizarAgua():
    try:
        conexao = mysql.connector.connect(**CONFIG_BANCO)
        cursor = conexao.cursor()

        # Mostra os IDs existentes
        cursor.execute("""
            SELECT id_agua, tempo, gasto_banho, gasto_semana
            FROM calculos_agua
            ORDER BY id_agua DESC
        """)

        resultados = cursor.fetchall()

        print("\n__________CÁLCULOS DE ÁGUA__________")

        if not resultados:
            print("| Nenhum cálculo encontrado.")
            cursor.close()
            conexao.close()
            input("| Pressione ENTER para continuar...")
            return

        for registro in resultados:
            print("|--------------------------------")
            print(f"| ID: {registro[0]}")
            print(f"| Tempo: {registro[1]} minutos")
            print(f"| Gasto por banho: {registro[2]} litros")
            print(f"| Gasto semanal: {registro[3]} litros")

        print("|--------------------------------")

        id_agua = input(
            "| Digite o ID do cálculo que deseja atualizar: "
        )

        if not id_agua.isdigit():
            print("| ID inválido.")
            cursor.close()
            conexao.close()
            input("| Pressione ENTER para continuar...")
            return

        id_agua = int(id_agua)

        # Verifica se o ID existe
        cursor.execute(
            "SELECT * FROM calculos_agua WHERE id_agua = %s",
            (id_agua,)
        )

        registro = cursor.fetchone()

        if registro is None:
            print("| Cálculo não encontrado.")
            cursor.close()
            conexao.close()
            return

        # Novo tempo
        while True:
            try:
                tempo = float(
                    input("| Quantos minutos dura o seu banho?: ")
                )

                if tempo <= 0:
                    print("| Digite um número acima de 0!")
                    continue

                break

            except ValueError:
                print("| Apenas números por favor!")

        litros_gastos_minuto = 10

        gasto_banho = tempo * litros_gastos_minuto
        gasto_semana = gasto_banho * 7

        cursor.execute("""
            UPDATE calculos_agua
            SET
                tempo = %s,
                gasto_banho = %s,
                gasto_semana = %s
            WHERE id_agua = %s
        """, (
            tempo,
            gasto_banho,
            gasto_semana,
            id_agua
        ))

        conexao.commit()

        print("|")
        print("| Cálculo atualizado com sucesso!")

        cursor.close()
        conexao.close()

    except Error as e:
        print(f"| Erro ao atualizar dados: {e}")

def excluirAgua():
    try:
        conexao = mysql.connector.connect(**CONFIG_BANCO)
        cursor = conexao.cursor()

        # Mostra os IDs existentes
        cursor.execute("""
            SELECT id_agua, tempo, gasto_banho, gasto_semana
            FROM calculos_agua
            ORDER BY id_agua DESC
        """)

        resultados = cursor.fetchall()

        print("\n__________CÁLCULOS DE ÁGUA__________")

        if not resultados:
            print("| Nenhum cálculo encontrado.")
            cursor.close()
            conexao.close()
            input("| Pressione ENTER para continuar...")
            return

        for registro in resultados:
            print("|--------------------------------")
            print(f"| ID: {registro[0]}")
            print(f"| Tempo: {registro[1]} minutos")
            print(f"| Gasto por banho: {registro[2]} litros")
            print(f"| Gasto semanal: {registro[3]} litros")

        print("|--------------------------------")

        id_agua = input(
            "| Digite o ID do cálculo que deseja excluir: "
        )

        if not id_agua.isdigit():
            print("| ID inválido.")
            cursor.close()
            conexao.close()
            return

        id_agua = int(id_agua)

        # Verifica se o ID existe
        cursor.execute(
            "SELECT * FROM calculos_agua WHERE id_agua = %s",
            (id_agua,)
        )

        registro = cursor.fetchone()

        if registro is None:
            print("| Cálculo não encontrado.")
            cursor.close()
            conexao.close()
            return

        print("|")
        print(f"| Cálculo encontrado: ID {id_agua}")
        print(f"| Gasto por banho: {registro[2]} litros")
        print(f"| Gasto semanal: {registro[3]} litros")

        confirmacao = input(
            "| Tem certeza que deseja excluir? (sim/não): "
        ).strip().lower()

        if confirmacao not in ("sim", "s"):
            print("| Exclusão cancelada.")
            cursor.close()
            conexao.close()
            return

        cursor.execute(
            "DELETE FROM calculos_agua WHERE id_agua = %s",
            (id_agua,)
        )

        conexao.commit()

        print("|")
        print("| Cálculo excluído com sucesso!")

        cursor.close()
        conexao.close()

    except Error as e:
        print(f"| Erro ao excluir dados: {e}")


def menuAgua():
    while True:
        print("\n__________MENU DE ÁGUA__________")
        print("|")
        print("| 1 - Calcular consumo de água")
        print("| 2 - Consultar cálculos")
        print("| 3 - Atualizar cálculo")
        print("| 4 - Excluir cálculo")
        print("| 5 - Voltar ao menu principal")
        print("|________________________________")

        escolha = input("| Qual será sua escolha: ")

        if escolha == "1":
            CalcularAgua()

        elif escolha == "2":
            consultarAgua()

        elif escolha == "3":
            atualizarAgua()

        elif escolha == "4":
            excluirAgua()

        elif escolha == "5":
            return

        else:
            print("| Opção inválida.")