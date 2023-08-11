nov = int(input("Digite numero de vendedores: "))

total_ventas = 0

for v in range(nov, nov+1):
    print("Información de los vendedores: ", v)
    
    while True:
        try:
            d_i = int(input("\nDigite el numero de identidad: "))
            if d_i < 1:
                print("Documento de identidad inválido, intente de nuevo.")
                input("Presione ENTER para continuar...")
                continue
            break
        except ValueError:
            print("Documento de identidad inválido.")
            input("Presione ENTER para continuar...")
            

    while True:
        try:
            nom = input("\nIngrese el nombre: ")
            if nom == None or nom.strip() == "":
                print("Nombre invalido.")
                input("Presione ENTER para continuar...")
                continue
            break
        except ValueError:
            print("Nombre inválido.")
            input("Presione ENTER para continuar...")
            
    while True:
        try:
            tv = int(input("Tipo de vendedor (1 = puerta a puerta)(2 = telemercadeo)(3 = Ejecutivo de ventas): "))
            if tv < 1 or tv > 3:
                print("Numero inválido, digite un numero del 1 al 3.")
                continue
            break
        except ValueError:
            print("Inválido.")
            input("Presione ENTER para continuar...")

nv = int(input("Ingrese numero de ventas: "))

comision_total_venta = 0
comision_total = 0

for ven in range(1, nv+1): 
    print("Información de las ventas: ", ven)

    while True:
        try:
            nc = input("\nIngrese nombre del cliente: ")
            if nc == None or nc.strip() == "":
                print("Nombre invalido.")
                input("Presione ENTER para continuar...")
                continue
            break
        except ValueError:
            print("Nombre inválido.")
            input("Presione ENTER para continuar...")
    
    while True:
        try:
            cc = int(input("\nDigite el código del cliente: "))
            if cc < 1:
                print("Código inválido, intente de nuevo.")
                input("Presione ENTER para continuar...")
                continue
            break
        except ValueError:
            print("Código del cliente inválido.")
            input("Presione ENTER para continuar...")

    while True:
        try:
            tve = int(input("Tipo de venta (1 = contado)(2 = crédito): "))
            if tve < 1 or tve > 2:
                print("Numero inválido, digite un numero del 1 al 2.")
                continue
            break
        except ValueError:
            print("Inválido.")
            input("Presione ENTER para continuar...")

    while True:
        try:
            vdv = int(input("Ingrese el valor de la venta: "))
            if vdv <= 0:
                print("Valor de venta inválido...")
                input("Presione ENTER para continuar...")
                continue
            break
        except ValueError:
            print("Valor de venta inválido: ")
            input("Presione ENTER para continuar...")

    comision_de_venta = 0
    if tv == 1:
        if tve == 1:
            comision_de_venta = vdv * 0.25
        if tve == 2:
            comision_de_venta = vdv * 0.20
    if tv == 2:
        if tve == 1:
            comision_de_venta = vdv * 0.15
        if tve == 2:
            comision_de_venta = vdv * 0.10
    if tv == 3:
        if tve == 1:
            comision_de_venta = vdv * 0.20
        if tve == 2:
            comision_de_venta = vdv * 0.15

    comision_total += comision_de_venta
    comision_total_venta += vdv

    print(f"Valor a pagar a cada vendedor por concepto de comisiones: ${comision_total_venta:,.0f}")
    print(f"Valor a pagar por comisiones (todos los vendedores): ${comision_total:,.0f}")

    total_ventas += comision_total

print(f"Valor total de ventas por cada vendedor: ${total_ventas:,.0f}")


