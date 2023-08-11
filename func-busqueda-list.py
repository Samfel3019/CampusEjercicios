def findlist(lst, elem):
    # encuentra el elemento y devuelve la posicion
    #devuelve None si no lo encuentra
    for i in range(len(lst)):
        if elem == lst[i]:
            return i
        
    return None

def existlst(lst, elem):
    # devuelve True si existe en la lista
    # devuelve un False si no existe en la lista
    for e in lst:
        if elem == e:
            return True
        
    return False