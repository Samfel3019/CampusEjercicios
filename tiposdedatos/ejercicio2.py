nombre = input("ingrese su nombre: ")
nota1= float(input("ingrese nota 1 (1.0 a 5.0) "))
nota2= float(input("ingrese nota 2 (1.0 a 5.0) "))
nota3= float(input("ingrese nota 3 (1.0 a 5.0) "))
ing= float(input("ingrese nota ing (1.0 a 5.0) "))

nf = nota1 * 0.2 + nota2 * 0.25 + nota3 * 0.35 + ing * 0.2
nota1 = (nota1 / 100) * 20
nota2 = (nota2 / 100) * 25
nota3 = (nota3 / 100) * 35
ing = (ing / 100) * 20

print(f"la nota definitiva de {nombre} es {nf:.1f}")
