n = int(input("Digite un numero: "))
acum = 0
for i in range(1, n+1):
    if i % 2 == 0:
        acum = acum - 1/i
    else:
        acum = acum + 1/i
        
print("Cantidad de terminos: ", n)
print("Resultado de la serie: ", acum)

