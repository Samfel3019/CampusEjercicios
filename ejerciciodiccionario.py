
dic = {
    "Nombre" : "nom" , 
    "Numero" : "num"
}

while True:
    try:
        nom = input("\nNombre: ")
        if nom == None or nom.strip() == "":
            print("\nNombre invalido.")
            input("\nPresione ENTER para continuar...")
            continue
        break
    except ValueError:
            print("\nNombre inválido.")
            input("\nPresione ENTER para continuar...")

if nom == nom:
    print("\nNo se puede repetir nombre.")
    input("\nPresione ENTER para continuar...")


while True:
    try:
        num = int(input("\nNúmero: "))
        if num < 1:
            print("\nNúmero inválido, intente de nuevo.")
            input("\nPresione ENTER para continuar...")
            continue
        break
    except ValueError:
            print("\nNúmero inválido.")
            input("\nPresione ENTER para continuar...")



