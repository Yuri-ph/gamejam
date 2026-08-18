def CalcularAgua():
    while True:
        try:
            tempo = float(input("quanto tempo em minutos dura o seu banho?: "))

            if tempo <= 0:
                print("Digite um número acima de 0!")
                continue
            break

        except ValueError:
            print("apenas números por favor!")
            continue
    litros_gastos_minuto = 10

    gasto_banho = tempo * litros_gastos_minuto
    gasto_semana = gasto_banho * 7

    print("---Resultado---")

    print("Gasto por banho: ", gasto_banho, "litros")
    print("O gasto semanal é:", gasto_semana, "litros")

    if gasto_banho <= 50:
        print("🟢pouco gasto de água🟢")
    elif gasto_banho <= 150:
        print("🟡medio gasto de água🟡")
    else:
        print("🔴muito gasto de água🔴")

CalcularAgua()
