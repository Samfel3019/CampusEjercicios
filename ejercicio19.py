cant_est_ing = int(input("Cantidad de estudiantes en inglés: "))
cod_en_ing = set(input("Códigos de estudiantes inscritos en inglés: ").split())
cant_est_fra = int(input("Cantidad de estudiantes en francés: "))
cod_en_fra = set(input("Códigos de estudiantes inscritos en francés: ").split())

ing = cod_en_ing - cod_en_fra
print(len(ing))





