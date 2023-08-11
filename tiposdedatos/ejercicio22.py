ntotal = 0
datos = {}
contador = 0

while True:
    contador += 1
    print("\nDatos del estudiante #", contador)
    cod = int(input("Código: "))
    if cod == 999:
        break
    nom = input("Nombre: ")
    n1 = int(input("Nota 1 (Valor: 30%): "))
    n2 = int(input("Nota 2 (Valor: 30%): "))
    n3 = int(input("Nota 3 (Valor: 40%): "))
    
    datos = {
        "código": cod,
        "nombre": nom,
        "nota 1": n1,
        "nota 2": n2,
        "nota 3": n3
    }
    
    
    
print("\n", "=" * 40)
print("* INFORME *")
print("=" * 40)
for k, v in dat.items():
    print(v["nombre"], "\t", f"${v['honorarios']:,.0f}")

print("\n", "=" * 40)
print("* RESUMEN *")
print("=" * 40)
print(f"Valor total de honorarios ${valTotal:,.0f}")