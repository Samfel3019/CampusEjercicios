nombre = input("Nombre del conductor: ")
placa = input("Ingrese placa del vehículo: ")
vpcp = input("ingrese el valor por concepto de pasajes: ")
vpve = input("Ingrese el valor total por concepto de encomiendas: ")

liqpas = (vpcp / 100) * 25
liqenc = (vpve / 100) * 15

vtl = liqpas + liqenc 

print(f"Nombre: ", {nombre})
print(f"Placa: ", {placa})
print(f"Valor total por concepto de pasajes: $ {vpcp:,.0f}")
print(f"Valor a pagar por concepto de pasajes: $ {liqpas:,.0f}")
print(f"Valor total por concepto de encomiendas: $ {vpve:,.0f}")
print(f"Valor a pagar por concepto de encomiendas: $ {liqenc:,.0f}")
print(f"Valor total por pagar al conductor: $ {vtl:,.0f}")
1