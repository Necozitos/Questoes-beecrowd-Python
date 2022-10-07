#Programa ira solicitar 2 números e logo após ira perguntar qual operação deseja realizar ocm eles.

a = float(input("Primeiro número:"))
b = float(input("Segundo número:"))
operação = input("Digite a operação a realizar (+,-,* ou /):")
if operação == "+":
    resultado = a + b
elif operação == "-":
    resultado = a - b
elif operação == "*":
    resultado = a * b
elif operação == "/":
    resultado = a / b
else:
    print("Operação inválida!")
    resultado = 0
print("Resultado: ", resultado)
