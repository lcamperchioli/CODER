# Crea una cadena de texto
texto = input("Ingresa una oracion: ")
print(texto)

# Convertir el texto a una lista de palabras
palabras = texto.split()
print(palabras)

# Convertir la lista de palabras en un conjunto para eliminar duplicados
palabras_unicas = set(palabras)
print(palabras_unicas)

# Convertir el conjunto en una lista
lista_palabras_unicas = list(palabras_unicas)
print(lista_palabras_unicas)

# Ordenar la lista
lista_palabras_unicas.sort()
print(lista_palabras_unicas)

conjunto = {"11", "22", "33"}
lista_palabras_unicas.extend(conjunto)
print(lista_palabras_unicas)

lista_palabras_unicas.insert(0, "Hola")
print(lista_palabras_unicas)

lista_palabras_unicas.reverse()
print(lista_palabras_unicas)