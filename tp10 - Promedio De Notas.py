import os
os.system("cls")
Nota1 = int(input("Ingrese la primer nota: "))
Nota2 = int(input("Ingrese la segunda nota: "))
Nota3 = int(input("Ingrese la tercer nota: "))

promedio=(Nota1+Nota2+Nota3)/3

if promedio >= 7:
    print("Usted esta aprobado con",promedio)
elif promedio >= 4:
    print("Usted esta en instancia regular con",promedio)
else:
    print("Usted esta reprobado con",promedio)