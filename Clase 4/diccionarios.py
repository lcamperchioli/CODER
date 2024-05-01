# *** COPY & CLEAR
diccionario = {"sal": 10.58, "pan": 20.00, "leche": 25.25, "vino":100.00}

diccionario_copia = diccionario
diccionario_copia["fideos"] =  200.2

print(diccionario)
print(diccionario_copia)

# del diccionario_copia -> De esta manera no existe mas
# Para dejar el conjunto vacio:
diccionario_copia = {}
diccionario_copia.clear()

print(diccionario)
print(diccionario_copia)

# *** KEYS & VALUES
print(diccionario.keys())
claves = diccionario.keys()
# a, b, c, d = claves
# print(a, b, c, d)
print(*claves)

print(diccionario.values())
valores = diccionario.values()
print(*valores)

# *** ITEMS
claves_valores = diccionario.items()
print(claves_valores)
# a, b, c, d = diccionario.items()
# print(*a, *b, *c, *d)

# UPDATE
diccionario.update({"carne": "500", "verduras": 500})
print(diccionario)

otro_dict = {"carne": "500", "verduras": 500}
diccionario.update(otro_dict)
print(diccionario)