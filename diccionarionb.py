diccionario = {}

cont = 0

while True:
    cont += 1
    nom = input(f"Ingrese nombre de usuario # {cont}: ")
    if nom.lower() == "no":
        break
    if nom in diccionario:
        print("Nombre repetido.")
        continue
    telefono = int(input("Digite # de teléfono: "))

    diccionario[nom] = telefono

    for nom, telefono in diccionario.items():
        print(f"Nombre: {nom}, Telefono: {telefono}")