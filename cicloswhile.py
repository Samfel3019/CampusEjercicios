#en las variables tipo contador, se aplica la formula asi:
#cont = cont + 1
#en las variables tipo sumador, se aplica la formula asi:
# variable = variable + el nuevo valor  

#calcular el promedio de n notas ingresadas por un docente.

n = int(input("Cuantas notas son: "))

sumnotas = 0
for i in range(1, n+1):
    nota = float(input(f"Nota {i} (0.0 - 5.0): "))
    sumnotas = sumnotas + nota
    
prom = round(sumnotas / n, 1)
print(f"El promedio de las notas es:   {prom:.1f}")
