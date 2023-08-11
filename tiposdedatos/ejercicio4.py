nombre = input("Ingrese el nombre del empleado: ")
salario = int(input("Ingrese el salario del empleado: "))

if salario <= 1_200_000:
    aux = 120_000
else: 
    aux = 0
    
print("Nombre: ",nombre)
print(f"Salario: ${salario:,.0f}")
print(f"Aux de transporte: ${aux:,.0f}")
