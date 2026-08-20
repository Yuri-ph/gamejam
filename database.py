import mysql.connector


def criarBancoDados():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Senac2026@"
        )

        cursor = conexao.cursor()

        # Criar banco
        cursor.execute("CREATE DATABASE IF NOT EXISTS hackaton")

        # Selecionar banco
        cursor.execute("USE hackaton")

        # Criar tabela de energia
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS energia (
                id_energia INT AUTO_INCREMENT PRIMARY KEY,

                gasto_banho DECIMAL(10,2) NOT NULL,
                gasto_ar DECIMAL(10,2) NOT NULL,
                gasto_tv DECIMAL(10,2) NOT NULL,
                gasto_computador DECIMAL(10,2) NOT NULL,
                gasto_video_game DECIMAL(10,2) NOT NULL,

                gasto_total DECIMAL(10,2) NOT NULL

            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS calculos_agua (
                id_agua INT AUTO_INCREMENT PRIMARY KEY,

                tempo DECIMAL(10,2) NOT NULL,
                gasto_banho DECIMAL(10,2) NOT NULL,
                gasto_semana DECIMAL(10,2) NOT NULL
            )
        """)

        conexao.commit()

        cursor.close()
        conexao.close()

        print("| Banco de dados conectado!")
        print("| Banco 'hackaton' verificado!")
        print("| Tabela 'energia' verificada!")
        print("| Tabela 'calculos_agua' verificada!")

    except mysql.connector.Error as erro:
        print("|")
        print("| Erro ao criar o banco de dados:")
        print("|", erro)


def conectarBanco():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Senac2026@",
            database="hackaton"
        )

        return conexao

    except mysql.connector.Error as erro:
        print("|")
        print("| Erro ao conectar ao banco:")
        print("|", erro)

        return None