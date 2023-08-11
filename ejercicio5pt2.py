nombre = input("Ingrese el nombre del estudiante: ")
ncuant = float(input("Ingrese la nota cuantitativa (0 - 100): "))

if ncuant < 0 and ncuant > 100:
    print("Error. Nota inválida")
elif ncuant < 60:
    ncual = "D"
elif ncuant < 80:
    ncual= "C"
elif ncuant < 90:
    ncual = "B"
else:
    ncual = "A"

print("Nombre:", nombre)
print(f"Nota cuantitativa : {ncuant:.1f}")
print(f"Nota cualitativa : {ncual}")

