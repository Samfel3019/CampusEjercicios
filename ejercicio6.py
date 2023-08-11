#CALCULAR LA CANTIDAD DE DIGITOS QUE TIENE UN NUMERO ENTERO POSITIVO.
#EJEMPLO
#   num = 101
#   cantidad de dígitos = 3
num = int(input("Numero entero positivo: "))


if num < 10:
    cdig = 1
elif num < 100:
    cdig = 2
elif num < 1000:
    cdig = 3
elif num < 10_000:
    cdig = 4
elif num < 100_000:
    cdig = 5
elif num < 1_000_000:
    cdig = 6
elif num < 10_000_000:
    cdig = 7

print("cantidad de digitos: ", cdig)
