# imprima los numeros pares del 2 al 50 incluyendo el 50.

# for par in range(2, 51, 2):
#     print(par, end=", ")

# imprima los multiplos de 5 que hay menores de 100

# for m in range(5, 100, 5):
#     print(m, end=", ")

# indicar si un numero ingresado por el usuario es primo o no

num = int(input("Ingrese numero: "))

if num > 1:
    esprimo = True
    for div in range(2, num):
        if num % div == 0:
            esprimo = False
            break
    if esprimo == True:
        print("EL numero es primo")
    else:
        print("EL numero no es primo") 
else:
    print("Error. Numero invalido, deben ser mayores a 1.")


