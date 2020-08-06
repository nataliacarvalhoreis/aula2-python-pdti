letra = input("Informe a letra: ")

vogal = "aeiou"

letra = letra.lower()

if vogal.find(letra)>=0:
    print("A letra é uma vogal")
else:
    print("A letra é uma consoante")


