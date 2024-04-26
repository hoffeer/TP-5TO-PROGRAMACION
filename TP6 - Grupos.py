name = input("Cual es tu nombre: ")
genero = input("Cual es tu sexo: ")
if genero == "M":
    if name.lower() < "m" :
        group = "A"
    else:
        group = "B"
else:
    if name.lower() > "n":
        group = "A"
    else:
        group = "B"
print("Tu grupo es " + group)
