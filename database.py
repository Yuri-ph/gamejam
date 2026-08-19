import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="SUA_SENHA"
)

cursor = conexao.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS hackaton")

print("Banco de dados criado com sucesso!")

cursor.close()
conexao.close()