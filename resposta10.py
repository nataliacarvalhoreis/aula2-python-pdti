turno = input("Informe o turno em que você estuda:")

turno = turno.lower()

if turno == 'm':
    print("Bom dia!")
elif turno == 'v':
    print("Boa tarde!")
elif turno == 'n':
    print("Boa noite!")
else:
    print("Valor inválido!")

