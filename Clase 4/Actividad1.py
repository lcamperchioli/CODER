# Una sola cadena de una linea, aunque en el editor se vea de varias linea
texto_original="gordon lanzó su curva&strawberry ha fallado por un pie! -gritó Joe Castiglione&dos pies -le corrigió Troop&strawberry menea la cabeza como disgustado... -agrega el comentarista"
print(texto_original)

# Dividir la cadena en una lista de palabras
lista_de_texto = texto_original.split("&")
print(lista_de_texto)

# Primera palabra con letra mayuscula
lista_de_texto[0] = lista_de_texto[0].capitalize() + "..."
print(lista_de_texto)

# Arreglar la segunda oracion
lista_de_texto[1] = f"- {lista_de_texto[1].capitalize()}.".replace("joe","Joe").replace("castiglione", "Castiglione")
print(lista_de_texto)

# Arreglar la tercera oracion
lista_de_texto[2] = f"- {lista_de_texto[2].capitalize()}.".replace("-le","le").replace("troop", "Troop")
print(lista_de_texto)

# Arreglar la cuarta oracion 
lista_de_texto[3] = f"- {lista_de_texto[3].capitalize()}."
print(lista_de_texto)

# Crear la nueva cadena porque lo que tengo es una lista
texto_nuevo = "\n".join(lista_de_texto)
print(texto_nuevo)

