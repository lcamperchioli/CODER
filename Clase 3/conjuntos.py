conjunto = {1, 2, 3, 4, 5}
print(type(conjunto))
otro_conjunto = {"Hola", "como", "estas"}
print(otro_conjunto)
longitud = len(otro_conjunto)
print(longitud)

conjunto_vacio = set()
print(conjunto_vacio)
conjunto_range = set(range(10))
print(conjunto_range)

mi_lista = list(otro_conjunto)
mi_lista.append("Adios")
print(mi_lista)
mi_nuevo_conjunto = set(mi_lista)
print(mi_nuevo_conjunto)
