palabra = input("Palabra: ")

if palabra[::1] == palabra:
    print("La palabra es un palíndrome")
else:
    print("La palabra no es un palìndrome")