import random

def imprimirMat(m):
    for f in range(len(m)):
        for c in range(len(m[f])):
            print(m[f][c], end="\t")
        print("")


    

def llenarMat(m):
    for f in range(len(m)):
        for c in range(len(m[f])):
            m[f][c] = random.randint(18, 119)

def crearMatriz(fil, col):
    m = []
    for i in range(fil):
        c = [0] * col
        m.append(c)
        
    return m

mat = crearMatriz(5, 7)
llenarMat(mat)
imprimirMat(mat)

print("\nEl producto que genera mas ingresos a la semana es: ", )