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
 
 
def salvar_calculo(km_dia, dias_semana, km_semana, co2_semana):
    try:
        conexao = mysql.connector.connect(**CONFIG_BANCO)
        cursor = conexao.cursor()
 
 
        cursor.execute("INSERT INTO calculos (km_dia, dias_semana, km_semana, co2_semana) VALUES (%s, %s, %s, %s)", (km_dia, dias_semana, km_semana, co2_semana))
 
        conexao.commit()
        cursor.close()
        conexao.close()
 
        print("Cálculo salvo no banco de dados")
 
    except Error as e:
        print(f"Erro ao salvar dados no banco de dados: {e}")



def CalculoCarbono():
 
    print("=== Calculadora de carbono semanal (carro) ===")
    print()
 
    while True:
        try:
            km_dia = float(input("Quantos km você roda de carro por dia? "))
 
            if km_dia < 0:
                print("Erro: o valor não pode ser negativo. Tente novamente.")
                return
        except ValueError:
            print("Erro: digite um número válido (ex: 10 ou 10.5).")
 
 
<<<<<<< HEAD
    while True:
        try:
            dias_semana = float(input("Quantos dias por semana você usa o carro? "))
 
            if dias_semana < 0 or dias_semana > 7:
                print("Erro: o valor deve estar entre 0 e 7.")
                continue
 
            break
 
        except ValueError:
            print("Erro: digite um número válido (ex: 5).")
 
 
    km_semana = km_dia * dias_semana
    co2_semana = km_semana * Fator_Gasolina
 
    print()
    print("--- Resultado ---")
    print("Km rodados na semana:", km_semana, "km")
    print("CO2 emitido na semana:", co2_semana, "kg")
 
    salvar_calculo(km_dia, dias_semana, km_semana, co2_semana)
 
while True:
 
    CalculoCarbono()
 
    while True:
        continuar = input("\nDeseja fazer outro cálculo? (sim/não): ").strip().lower()
        
        if continuar in ("sim", "s", "não", "nao", "n"):
            break
        else:
            print("resposta inválida, digite 'sim' ou 'não'")
=======
        while True:
            try:
                dias_semana = float(input("Quantos dias por semana você usa o carro? "))
>>>>>>> df7280d51396d7ec01c1961ee8d7fd4f925b7cc1
    
                if dias_semana < 0 or dias_semana > 7:
                    print("Erro: o valor deve estar entre 0 e 7.")
                    return
    
            except ValueError:
                print("Erro: digite um número válido (ex: 5).")
 
 
            km_semana = km_dia * dias_semana
            co2_semana = km_semana * Fator_Gasolina
    
            print()
            print("--- Resultado ---")
            print("Km rodados na semana:", km_semana, "km")
            print("CO2 emitido na semana:", co2_semana, "kg")
        break


 
        while True:
            
                CalculoCarbono()
            
                while True:
                    continuar = input("\nDeseja fazer outro cálculo? (sim/não): ").strip().lower()
                    
                    if continuar in ("sim", "s", "não", "nao", "n"):
                        break
                    else:
                        print("resposta inválida, digite 'sim' ou 'não'")
                
                if continuar in ("nao", "não", "n"):
                    print("encerrando o programa...")
                    break  