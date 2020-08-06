num1 = float(input("Informe o primeiro número:"))
num2 = float(input("Informe o segundo número:"))
num3 = float(input("Informe o terceiro número:"))

maior = 0
menor = 0

if num1>num2 and num1>num3:
    maior = num1
    if num2<num3:
        menor = num2
    else:
        menor = num3
elif num2>num1 and num2>num3:
    maior = num2
    if num1<num3:
        menor = num1
    else:
        menor = num3
else:
    maior = num3
    if num1<num2:
        menor = num1
    else:
        menor = num2

print("O maior número é: ", maior)
print("O menor número é ", menor)