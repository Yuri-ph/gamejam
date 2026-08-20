import os
import time
from database import criarBancoDados, conectarBanco


def menuEnergia():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("__________MENU_DE_ENERGIA__________")
        print("|")
        print("| 1- Calcular energia")
        print("| 2- Consultar cálculos")
        print("| 3- Atualizar cálculo")
        print("| 4- Excluir cálculo")
        print("| 5- Voltar ao menu principal")
        print("|_____________________________________")
        
        escolhaMenuEnergia = input("| qual sera sua escolha: ")
        
        

        if escolhaMenuEnergia == "1":
            Calculototal()

        elif escolhaMenuEnergia == "2":
            consultarEnergia()

        elif escolhaMenuEnergia == "3":
            atualizarEnergia()

        elif escolhaMenuEnergia == "4":
            excluirEnergia()

        elif escolhaMenuEnergia == "5":
            return
        else:
            print("| Opção inválida")
            time.sleep(2)
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
        print("|")
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
        tvtempo = input("| Em média quantas horas por dia você deixa a televisão ligada: ")

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

    conexao = conectarBanco()

    if conexao is None:
        print("|")
        print("| Não foi possível conectar ao banco de dados.")
        time.sleep(2)
        return

    try:
        cursor = conexao.cursor()

        sql = """
            INSERT INTO energia (
                gasto_banho,
                gasto_ar,
                gasto_tv,
                gasto_computador,
                gasto_video_game,
                gasto_total
            )
            VALUES (%s, %s, %s, %s, %s, %s)
        """

        valores = (
            banho,
            ar,
            tv,
            computador,
            videogame,
            total
        )

        cursor.execute(sql, valores)

        conexao.commit()

        print("|")
        print("| Cálculo salvo no MySQL com sucesso!")

        cursor.close()

    except Exception as erro:
        print("|")
        print("| Erro ao salvar o cálculo:")
        print("|", erro)

        conexao.rollback()

    finally:
        conexao.close()

    time.sleep(2)


def consultarEnergia():
    conexao = conectarBanco()

    if conexao is None:
        print("|")
        print("| Não foi possível conectar ao banco de dados.")
        time.sleep(2)
        return

    try:
        cursor = conexao.cursor()

        sql = """
            SELECT
                id_energia,
                gasto_banho,
                gasto_ar,
                gasto_tv,
                gasto_computador,
                gasto_video_game,
                gasto_total
            FROM energia
            ORDER BY id_energia DESC
        """

        cursor.execute(sql)

        resultados = cursor.fetchall()

        os.system('cls' if os.name == 'nt' else 'clear')

        print("_____________CÁLCULOS DE ENERGIA_____________")
        print()

        if not resultados:
            print("| Nenhum cálculo encontrado.")
        else:
            for registro in resultados:
                print("|---------------------------------------------")
                print(f"| ID: {registro[0]}")
                print(f"| Banho: {registro[1]} Wh")
                print(f"| Ar condicionado: {registro[2]} Wh")
                print(f"| Televisão: {registro[3]} Wh")
                print(f"| Computador: {registro[4]} Wh")
                print(f"| Video game: {registro[5]} Wh")
                print(f"| TOTAL: {registro[6]} Wh")
                print(f"| Os dados exibidos são apenas uma estimativa, não leve como fato absoluto ")

               

            print("|---------------------------------------------")

        cursor.close()

    except Exception as erro:
        print("|")
        print("| Erro ao consultar os cálculos:")
        print("|", erro)

    finally:
        conexao.close()

    input("\n| Pressione ENTER para continuar...")

    
def atualizarEnergia():
    id_energia = escolherEnergia()

    if id_energia is None:
        return
    conexao = conectarBanco()

    if conexao is None:
        print("|")
        print("| Não foi possível conectar ao banco de dados.")
        time.sleep(2)
        return

    try:
        cursor = conexao.cursor()

        print("|")
        id_energia = input("| Digite o ID do cálculo que deseja atualizar: ")

        if not id_energia.isdigit():
            print("| ID inválido.")
            cursor.close()
            conexao.close()
            time.sleep(2)
            return

        id_energia = int(id_energia)

        # Verifica se o ID existe
        cursor.execute(
            "SELECT * FROM energia WHERE id_energia = %s",
            (id_energia,)
        )

        registro = cursor.fetchone()

        if registro is None:
            print("|")
            print("| Cálculo não encontrado.")
            cursor.close()
            conexao.close()
            time.sleep(2)
            return

        print("|")
        print("| Recalculando os valores...")
        print("|")

        # Faz um novo cálculo
        banho = CalculoBanho()
        ar = CalculoAr()
        tv = CalculoTv()
        computador = CalculoComputador()
        videogame = CalculoVideoGame()

        total = banho + ar + tv + computador + videogame

        sql = """
            UPDATE energia
            SET
                gasto_banho = %s,
                gasto_ar = %s,
                gasto_tv = %s,
                gasto_computador = %s,
                gasto_video_game = %s,
                gasto_total = %s
            WHERE id_energia = %s
        """

        valores = (
            banho,
            ar,
            tv,
            computador,
            videogame,
            total,
            id_energia
        )

        cursor.execute(sql, valores)

        conexao.commit()

        print("|")
        print("| Cálculo atualizado com sucesso!")
        print(f"| Novo gasto total: {total} Wh")

        cursor.close()

    except Exception as erro:
        print("|")
        print("| Erro ao atualizar o cálculo:")
        print("|", erro)

        conexao.rollback()

    finally:
        conexao.close()

    time.sleep(2)


def excluirEnergia():
    id_energia = escolherEnergia()

    if id_energia is None:
        return
    conexao = conectarBanco()

    if conexao is None:
        print("|")
        print("| Não foi possível conectar ao banco de dados.")
        time.sleep(2)
        return

    try:
        cursor = conexao.cursor()

        print("|")
        id_energia = input("| Digite o ID do cálculo que deseja excluir: ")

        if not id_energia.isdigit():
            print("|")
            print("| ID inválido.")
            cursor.close()
            conexao.close()
            time.sleep(2)
            return

        id_energia = int(id_energia)

        # Verifica se existe
        cursor.execute(
            "SELECT * FROM energia WHERE id_energia = %s",
            (id_energia,)
        )

        registro = cursor.fetchone()

        if registro is None:
            print("|")
            print("| Cálculo não encontrado.")
            cursor.close()
            conexao.close()
            time.sleep(2)
            return

        print("|")
        print(f"| Cálculo encontrado: ID {id_energia}")
        print(f"| Gasto total: {registro[6]} Wh")

        confirmacao = input("| Tem certeza que deseja excluir? (sim/não): ").strip().lower()

        if confirmacao not in ("sim", "s"):
            print("|")
            print("| Exclusão cancelada.")
            cursor.close()
            conexao.close()
            time.sleep(2)
            return

        cursor.execute(
            "DELETE FROM energia WHERE id_energia = %s",
            (id_energia,)
        )

        conexao.commit()

        print("|")
        print("| Cálculo excluído com sucesso!")

        cursor.close()

    except Exception as erro:
        print("|")
        print("| Erro ao excluir o cálculo:")
        print("|", erro)

        conexao.rollback()

    finally:
        conexao.close()

    time.sleep(2)

def escolherEnergia():
    
    conexao = conectarBanco()

    if conexao is None:
        print("|")
        print("| Não foi possível conectar ao banco de dados.")
        time.sleep(2)
        return None

    try:
        cursor = conexao.cursor()

        cursor.execute("""
            SELECT id_energia, gasto_total
            FROM energia
            ORDER BY id_energia
        """)

        resultados = cursor.fetchall()

        os.system('cls' if os.name == 'nt' else 'clear')

        print("_____________ESCOLHER CÁLCULO_____________")
        print()

        if not resultados:
            print("| Nenhum cálculo encontrado.")
            cursor.close()
            conexao.close()
            input("\n| Pressione ENTER para continuar...")
            return None

        print("| ID | Gasto total")
        print("|---------------------------")

        for registro in resultados:
            print(f"| {registro[0]}  | {registro[1]} Wh")

        print("|---------------------------")
        print()

        while True:
            id_energia = input("| Digite o ID do cálculo: ")

            if not id_energia.isdigit():
                print("| ID inválido. Digite apenas números.")
                continue

            id_energia = int(id_energia)

            cursor.execute(
                "SELECT id_energia FROM energia WHERE id_energia = %s",
                (id_energia,)
            )

            registro = cursor.fetchone()

            if registro is None:
                print("| Esse ID não existe.")
                continue

            cursor.close()
            conexao.close()

            return id_energia

    except Exception as erro:
        print("|")
        print("| Erro ao consultar os cálculos:")
        print("|", erro)

        conexao.close()
        time.sleep(2)
        return None