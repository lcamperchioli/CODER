# A partir de dos variables llamadas nombre y edad debes crear una variable que 
# almacene si se cumplen todas las siguientes condiciones, y mostrar al usuario
# True o False:

# Nombre que sea diferente de cuatro asteriscos ****
# Edad sea mayor que 5 y a su vez menor que 20
# Que la longitud de nombre sea mayor o igual a 4 pero menos que 8
# Edad multiplicada por 3 sea mayor que 35

# No debes ingresar datos con input
# No debes usar funciones, condicionales, bucles.

# Ingreso de datos
nombre = input("Nombre: ")
edad = int(input("Edad: "))

# Operaciones
validaciones = {
"condicion_1": nombre != "****",
"condicion_2":edad > 5 and edad < 20,
"condicion_3":len(nombre) >= 4 and len(nombre) < 8,
"condicion_4": (edad * 3) > 35, 
}

validar = (validaciones["condicion_1"] and validaciones["condicion_2"] and validaciones["condicion_3"] and validaciones["condicion_4"])

# bool: si tiene datos, devuelve True
# validacion = condicion_1 and condicion_2 and condicion_3 and condicion_4
print(validaciones.values())

# Salida
print(f"Es diferente de '****' : {validaciones['condicion_1']}")
print(f"La edad es mayor a 5 y menor que 20 : {validaciones['condicion_2']}")
print(f"La longitud del nombre es mayor o igual que 4 y menor que 8: {validaciones['condicion_3']}")
print(f"La edad multiplicada por 3 es mayor que 35 : {validaciones['condicion_4']}")
print(f"Se cumplen todas las condiciones? {validaciones}")



