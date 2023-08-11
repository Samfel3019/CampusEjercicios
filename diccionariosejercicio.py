def calcular_total_compra(articulos, valores):
    total_compra = 0
    compra = {}

    try:
        n = int(input("Ingrese el número de artículos a comprar: "))
        for _ in range(n):
            codigo = int(input("Ingrese el código del artículo: "))
            cantidad = int(input("Ingrese la cantidad comprada: "))
            
            if codigo in articulos and cantidad > 0:
                nombre_articulo = articulos[codigo]
                valor_unitario = valores[codigo]
                valor_total = valor_unitario * cantidad

                compra[nombre_articulo] = {
                    'Cantidad': cantidad,
                    'Valor Unitario': valor_unitario,
                    'Valor Total': valor_total
                    
                }
                total_compra += valor_total
            else:
                print("Código de artículo inválido o cantidad no válida. Intente nuevamente.")

        print("\nDetalle de la compra:")
        for articulo, info in compra.items():
            print(f"{articulo}: Cantidad: {info['Cantidad']}, Valor Unitario: ${info['Valor Unitario']}, Valor Total: ${info['Valor Total']}")
        
        print(f"\nValor total de la compra: ${total_compra}")
    except ValueError:
        print("Entrada inválida. Asegúrese de ingresar valores numéricos.")

articulos = {1: "Lapiz", 2: "Cuadernos", 3: "Borrador", 4: "Calculadora", 5: "Escuadra"}
valores = {1: 2500, 2: 3800, 3: 1200, 4: 35000, 5: 3700}

calcular_total_compra(articulos, valores)