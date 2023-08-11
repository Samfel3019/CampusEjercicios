año = int(input("Año: "))

if año % 4 == 0:
    if año % 100 == 0 and año % 400 != 0:
        print("NO es bisiesto")
    else:
        print("Si es bisiesto")
else:
    print("NO es bisiesto")

