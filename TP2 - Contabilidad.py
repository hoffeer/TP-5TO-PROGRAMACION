import os
os.system("cls")

b=0;
c=0;

for x in range (2):
    x=int(input("Ingrese un numero: "))

    if x%3 == 0:
        b=b+1
    if x%5 == 0:
        c=c+1
print("La cantidad de multiplos de 3 son: ",b)
print("La cantidad de multiplos de 5 son: ",c)