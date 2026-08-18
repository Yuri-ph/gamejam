def CalculoCarbono():
    FATOR_GASOLINA = 0.192
    print("=== Calculadora de carbono semanal (carro) ===")
    print()

    km_dia = float(input("Quantos km você roda de carro por dia? "))
    dias_semanas = float(input("Quantos dias por semana você usa o carro?"))

    km_semana = km_dia * dias_semanas
    co2_semana = km_semana * FATOR_GASOLINA

    print()
    print("--- Resultado ---")
    print("Km rodados na semana:", km_semana, "km")
    print("CO2 emitido na semana:", co2_semana, "Kg")

CalculoCarbono()