while True:
    try:
        n= input("Nombre: ")
        if n == None or n.strip() == "":
            print("Nombre invalido.")
            continue
        break
    except Exception as e:
        print("Ha sucedido un Error: ", e)
        
print("\n el nombre que se digitó es: ", n) 