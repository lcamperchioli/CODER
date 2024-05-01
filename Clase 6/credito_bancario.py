# Para aprobar el credito, el cliente debe ser mayor de edad. Ademas, debe tener
# una antiguedad en el sistema financiero de minimo 3 años y un ingreso mayor a
# 2.500 dolares. En caso no tenga la antiguedad suficiente, su ingreso mensual 
# debe ser como minimo 400 dolares. Si no cumple ninguna de las condiciones, no
# se aprueba el credito.

# Datos iniciales
# edad = 15
# antiguedad = 10
# ingreso = 1500

# Ingreso de datos
edad = int(input("Ingrese edad "))
antiguedad = int(input("Ingrese antiguedad "))
ingresos = float(input("Ingresos mensuales "))

# Operaciones
mayor_edad = (edad >= 18)
condicion_1 = (mayor_edad and antiguedad >= 3 and ingresos > 2500)
condicion_2 = (mayor_edad and antiguedad <3 and ingresos >= 4000)

# Salida de datos
if condicion_1 or condicion_2: 
    print("Credito aprobado")
else: 
    print("Credito denegado")

