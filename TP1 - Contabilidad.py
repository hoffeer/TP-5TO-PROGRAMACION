import os
os.system("cls")

b=0;
c=0;

for x in range (2):
    x=int(input("Ingrese una nota: "))
    if x>=7:
        b=b+1
    else:
        c=c+1
    
print("La cantidad de alumnos aprobados son: ",b)
print("La cantidad de desaprobados son: ",c)