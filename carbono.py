Fator_Gasolina = 0.192
 
 
def CalculoCarbono():
 
    print("=== Calculadora de carbono semanal (carro) ===")
    print()
 
    while True:
        try:
            km_dia = float(input("Quantos km você roda de carro por dia? "))
 
            if km_dia < 0:
                print("Erro: o valor não pode ser negativo. Tente novamente.")
                continue
 
            break
 
        except ValueError:
            print("Erro: digite um número válido (ex: 10 ou 10.5).")
 
 
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