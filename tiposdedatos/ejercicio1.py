seg = int(input("ingrese seg: "))

h = seg // 3600
m = (seg % 3600) // 60
seg = (seg % 3600) % 60

print("La cantidad de horas es: ",h)
print("la cantidad de minutos es: ",m)
print("la cantidad de segundos es; ",seg)

