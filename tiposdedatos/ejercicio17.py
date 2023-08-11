def leerEntero(msg):
    while True:
        try:
            num = int(input(msg))
            if n < 1:
                print("El numero no puede menor 1")
                input("Presione ENTER para continuar...")
                continue
            break
        except ValueError:
            print("Numero invàlido")
            input("Presione ENTER para continuar...")
            
    return num

def leerNombre(msg):
    while True:
        try:
            nom = input(msg)
            if nom == None or nom.strip() == "":
                print("No puede ser vacio")
                input("Presione ENTER para continuar...")
                continue
            break
        except Exception as e:
            print("Nombre invàlido", e)
            input("Presione ENTER para continuar...")
            
    return nom

def leerEstrato(msg):
    while True:
        try:
            nom = input(msg)
            if n < 1 or n > 5:
                print("El estrato debe ser de 1 a 5")
                input("Presione ENTER para continuar...")
                continue
            break
        except Exception as e:
            print("Estrato invàlido", e)
            input("Presione ENTER para continuar...")
            
    return nom


def tarifabasica(msg):
        if est == 1:
            return 10_000
        elif est == 2:
            return 15_000
        elif est == 3:
            return 20_000
        elif est == 4:
            return 25_000
        elif est == 5:
            return 30_000

def calcularImpulso(imp):
    return imp * 100

def mostrarValPagar(nom, tbas, valimp):
    print("\nNOmbre: ", nom)
    print(f"Valor a pagar: $"{tbas+valimp:,.0f}")
    print(f"Valor a pagar: $"{tbas:,.0f}")
    print(f"Valor impulsos: $"{valimp:,.0f}")

n = leerEntero("Cantidad abonados: ")
valtot = 0
for i in range(1, n+1):
    print("Abonado #", i)
    nom = leerNombre("Nombre: ")
    est = leerEstrato("Estrato: ")
    imp = leerEntero("cantidad Impulso: ")
    tbas = tarifabasica(est)
    valimp = calcularImpulso(imp)
    
    mostrarValPagar(nom, valimp, tbas)
    valtot += tbas + valimp
    
print(f"\nValor total a pagar: ${valtot:,.0f} ")
