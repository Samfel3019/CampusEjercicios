while True:
    try:
        n = float(input("Numero: "))
        break
    except ValueError:
        print("Error. Numero real invalido. intente de nuevo.")
        input("Presione ENTER para continuar...")
    except Exception as e:
        print("Ha ocurrido un error: ",e)
print("\n el numero que se digito es: ", n)
