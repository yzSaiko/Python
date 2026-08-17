print("****** CALCULADORA ******")

numero_1 = input("Informe o primeiro N°: ")
numero_2 = input("Informe o segundoo N°: ")
operador = input("Informe o tipo de cálculo: '+ , - , * , /' ")

if operador == "+":
    resultado = float(numero_1) + float(numero_2)
elif operador == "-":
    resultado = float(numero_1) - float(numero_2)
elif operador == "*":
    resultado = float(numero_1) * float(numero_2)
elif operador == "/":
    resultado = float(numero_1) / float(numero_2)
else:
    resultado = 0
    print("Você informou um operador que não existe!!!") 
print (resultado)