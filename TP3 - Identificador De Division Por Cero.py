print("DIGITE DOS NUMEROS")
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

div = num1/num2

if div == 0 or num1 == 0 or num2 == 0:
    ZeroDivisionError
else:
    print(div)
