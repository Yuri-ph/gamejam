def CalcularAgua():
    while True:
        try:
            tempo = float(input("| Quantos minutos dura o seu banho?: "))

            if tempo <= 0:
                print("| Digite um número acima de 0!")
                continue
            break

        except ValueError:
            print("| Apenas números por favor!")
            continue
    litros_gastos_minuto = 10

    gasto_banho = tempo * litros_gastos_minuto
    gasto_semana = gasto_banho * 7

    print("__________RESULTADO__________")

    print("| Gasto por banho: ", gasto_banho, "litros")
    print("| O gasto semanal é:", gasto_semana, "litros")

    if gasto_banho <= 50:
        print("| 🟢pouco gasto de água🟢")
    elif gasto_banho <= 150:
        print("| 🟡medio gasto de água🟡")
    else:
        print("| 🔴muito gasto de água🔴")

    while True:

        while True:
            continuar = input("| Deseja fazer outro cálculo? (sim/não): ").strip().lower()
    
            if continuar in ("sim", "s", "não", "nao", "n"):
                break
            else:
                print("| resposta inválida, digite 'sim' ou 'não'")

        if continuar in ("nao", "não", "n"):
         print("| encerrando o programa...")
        break  