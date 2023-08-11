# Hallar un promedio de notas de (0 a 5.0) hasta que la nota
# sea -1 o cualquier otro numero negativo.

suma = 0.0
nota = 0
cant = 0
while nota >= 0:
    while True:
        nota = float(input("Ingrese la nota: "))
        if nota > 5:
            print("Error. Ingrese una nota (0.0 a 5.0) o -1 para terminar")
            continue
        break
    if nota > 0:
        cant += 1
        suma += nota

prom = round(suma / cant, 1)
print(f"El promedio es: {prom:.1f}")

