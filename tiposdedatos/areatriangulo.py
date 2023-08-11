base= float(input("ingrese base: "))
altura= float(input("ingrese altura: "))

a = base * altura / 2

print("el area es:", a)
# f-string
print(f"El area es: {a:,.3f}")
# funcion format
print("El area es: {:,.2f}".format(a))