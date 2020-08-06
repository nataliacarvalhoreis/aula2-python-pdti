num1 = float(input("Informe o primeiro número:"))
num2 = float(input("Informe o segundo número:"))
num3 = float(input("Informe o terceiro número:"))

if num1>num2 and num1>num3:
    print("O numero ", num1, " é o maior")
elif num2>num1 and num2>num3:
    print("O numero ", num2, " é o maior")
else:
    print("O numero ", num3, " é o maior")