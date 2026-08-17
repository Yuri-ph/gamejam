FATOR_GASOLINA = 0.192
print("=== Calculadora de carbono semanal (carro) ===")
print()

km_dia = float(input("Quantos km você roda de carro por dia?"))

dias_semanas = float(input("Quantos dias por semana você usa o carro? "))

km_semana = km_dia * dias_semanas

co2_semana = km_dia * FATOR_GASOLINA

print()
print("--- Resultado ---")
print(f"Km rodados na semana: {km_semana:.1f} km")
print(f"CO2 emitido na semana: {co2_semana:.1f} kg")
