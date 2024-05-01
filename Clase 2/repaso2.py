cadena = "acitametaM , 5.8 ,otipeP ordeP"

# cadena[principio: fin : paso]
cadena_2 = cadena[0:10:2]
print(cadena_2)

# Pasos
# Paso 1: Dar vuelta la cadena 
cadena_volteada = cadena[::-1]
print(cadena_volteada)

# Paso 2: Extraer nombre y apellido 
nombre_apellido = cadena_volteada[0:12]

# Paso 3: Extraer la nota
nota = cadena_volteada[14:17]

#Paso 4: Extraer la materia
materia = cadena_volteada[19:]

# Paso 5: Moestrar lo solicitado 
texto = f"{nombre_apellido} ha sacado una nota de {nota} en la materia {materia}"
print(texto)


# Como traer letras
a = "cadena"

# Devuelve: Primera letra
a[0]

# Devuelde: Palabra entera
a[0:]

# Devuelve: caden
a[0:-1]

# Devuelve: cade
a[0:-2]

# Devuelve: cad
a[0:3]

