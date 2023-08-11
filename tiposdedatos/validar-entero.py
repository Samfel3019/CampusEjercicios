while True:
    try:
        n = int(input("Numero: "))
        break
    except ValueError:
        print("Error. Numero entero invalido. intente de nuevo.")
        input("Presione ENTER para continuar...")
        
print("\n el numero que se digito es: ", n)