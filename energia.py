def CalculoEnergia():
    banhosdiarios = int(input("Quantos banhos você toma por dia: "))
    if banhosdiarios == 0:
        print("A quantidade não pode ser nula")
    elif banhosdiarios.isalpha():
        print("O numero de banhos deve ser digito válido")
    elif 
    
        
    print("")
    banhotempo = int(input("Qual seu tempo médio em minutos que você toma banho: "))
    print("")
    calculobanho = (banhotempo * 550 * banhosdiarios )
    print(f"Seu banho consome diariamente {calculobanho} W ")

CalculoEnergia()