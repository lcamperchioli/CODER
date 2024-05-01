# Escribir un programa que indique la generacion correspondiente para un año de
# nacimiento indicado. Trabajaron con el notebook de clase 4
# Importante: para los años que no pertenezcan a ninguna generacion, se debera
# colocar: "No existe generacion asociada"

# generacion    año
# silenciosa    1920 - 1940
# Baby Boomer   1946 - 1964
# X             1965 - 1979
# Y             1980 - 2000
# Z             2001 - 2010

entrada = input("Año: ").strip()

if entrada.isdigit():
    año = int(entrada)

    if 1920 <= año <= 1940:
        generacion = "Generacion silenciosa"
    elif 1941 <= año <= 1964:
        generacion = "Sin generacion"
    elif 1965 <= año <= 1979:
        generacion = "Generacion X"
    elif 1980 <= año <= 2000:
        generacion = "Generacion Y"
    elif 2001 <= año <= 2010:
        generacion = "Generacion Z"
    else: 
        generacion = "No existe una generacion asociada"

else: 
        print("Debe ingresar digitos")

print(f"El año {año} corresponde a la {generacion}")

generacion_silenciosa = range(1920, 1941)
baby_boomer = range(1946, 1965)
generacion_x = range(1965, 1980)
generacion_y = range(1980, 2000)
generacion_z = range(2001, 2011)

entrada = input("Año: ").strip()

if entrada.isdigt():
     año = int(entrada)
     if año in generacion_silenciosa:
        mensaje = "Eres de la generacion silenciosa"
     elif año in baby_boomer: 
        mensaje = "Eres un Baby Boomer"
     elif año in generacion_x: 
        mensaje = "Eres de la generacion x"
     elif año in generacion_y: 
        mensaje = "Eres de la generacion y"
     elif año in generacion_z: 
        mensaje = "Eres de la generacion z"
     else:
         mensaje = "No existe generacion asociada"
else: 
    print("Debe ingresar digitos")

print(mensaje)

