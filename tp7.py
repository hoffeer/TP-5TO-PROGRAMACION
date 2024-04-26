renta = int(input("Ingrese el monto que paga de renta: "))

if renta < 10000:
    print("A usted le corresponde 5%")
elif renta >= 10000 and renta <= 20000:
    print("A usted le corresponde 15%")
elif renta >= 20000 and renta <= 35000:
    print("A usted le corresponde 20%")
elif renta >= 35000 and renta <= 60000:
    print("A usted le corresponde 30%")
else:
    print("A usted le corresponde un 45% de tipo impositivo")