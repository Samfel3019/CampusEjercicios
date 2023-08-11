#los telefonos de una empresa tienen el siguiente formato prefijo-numero-extension 
#donde el prefijo es el codigo del pais +34 y la extension tiene dos digitos
#por ejemplo +34-913724710-56


tel = input("ingrese telefono con formato(+codpais-num-ext): ")
parttel = tel.split("-")

#parttel : [codpais, num, ext]
#Validar +35
if len(parttel) == 3 and parttel[0].starwith("+") and \
    len(parttel[0]) == 3 and  parttel [0][1:].isdigit() and \
        parttel[1].isdigit() and len(parttel[2]) == 2 and \
            parttel[2].isdigit():
                print(parttel[1])
else:
    print("Formato inválido")

