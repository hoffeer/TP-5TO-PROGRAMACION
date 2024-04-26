mayor = int(input("Ingrese su edad: "))
sueldo = int(input("Ingrese sus ingresos mensuales: "))

if mayor > 16 or sueldo >= 1000:
    print("Usted debe tributar")
else:
    print("Usted no debe tributar")
