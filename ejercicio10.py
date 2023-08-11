# imprimir los numeros primos entre 100 y 500 que no terminen en 3.  

for numpri in range (100, 501):
    esprimo = True
    for div in range(3, numpri, 2):
        if numpri % div == 0:
            esprimo = False
            break
            
    if esprimo == True:
        if numpri % 10 == 3:
            continue
        print(numpri, end=", ")

