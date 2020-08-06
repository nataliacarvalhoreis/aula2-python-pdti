prod1 = float(input("Informe o valor do primeiro produto:"))
prod2 = float(input("Informe o valor do segundo produto:"))
prod3 = float(input("Informe o valor do terceiro produto:"))

if prod1<prod2 and prod1<prod3:
    print("Você deve comprar o produto 1. Valor: R$", prod1)
elif prod2<prod1 and prod2<prod3:
    print("Você deve comprar o produto 2. Valor: R$", prod2)
else:
    print("Você deve comprar o produto 3. Valor: R$", prod3)