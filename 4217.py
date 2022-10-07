#Programa ira socilitar o salario, caso ele seja maior que 1250 ira aplicar um aumento de 10%. Para os inferiores ou iguais, sera de 15%.

salário = float(input("Digite seu salário: "))
pc_aumento = 0.15
if salário > 1250:
    pc_aumento = 0.10
aumento = salário * pc_aumento
print(f"Seu aumento será de: R$ {aumento:7.2f}")
