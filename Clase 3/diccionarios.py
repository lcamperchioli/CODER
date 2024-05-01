paises_capitales = {
    "Argentina": "Buenos Aires",
    "Brazil": "Brasilia",
    "France": "Paris",
    "Japan": "Tokyo",
    "Australia": "Canberra"
}

tipo = type(paises_capitales)
print(tipo)

longitud = len(paises_capitales)
print(longitud)

obtener_valor = paises_capitales["Argentina"]
print(obtener_valor)

# Nuevo valor
paises_capitales["Colombia"]= "Bogota"
print(paises_capitales)

# Cambiar valor
paises_capitales["Australia"]= "Melborne"
print(paises_capitales)

# Eliminar un elemento 
del paises_capitales["Japan"]
print(paises_capitales)

obtener_valor = paises_capitales.get("Argentinaas", "No encontrado")
print(obtener_valor)

# paises_capitales.pop("Japan")
# print(paises_capitales)

# Otro diccionario con mas paises con sus capitales
paises_capitales2 = {
    "Colombia": "Bogota",
    "Chile": "Santiago",
    "Mexico": "Mexico City",
}

paises_capitales.update(paises_capitales2)
print(paises_capitales)

from pprint import pprint
pprint(paises_capitales)

respuesta = "Chile" in paises_capitales
print(respuesta)