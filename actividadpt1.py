#Construya un programa que muestro los números divisibles de 3 y 7 entre 1 y 1000.

for nd in range(1, 1001):
    if nd % 3   == 0 and nd % 7 == 0:
        print(nd, end = ", ")