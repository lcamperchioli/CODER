# Solicitar al usuario el nombre de un producto y luego su precio. El programa
# debera agregar un impuesto sobre el precio del producto
# Crear un dict con los siguientes indices:
# "producto": precio del producto
# Mostrar un mensaje con el siguiente formato:
# El producto {producto} tiene un precio de {precio}

# Solicitar al usuario el nombre del producto 
nombre_producto = input("Ingrese el nombre del producto")

# Solicitar al usuario el precio del producto
# precio_producto = float(input("Ingrese el precio del producto"))

# Definir la tasa de impuesto
TASA_IMPUESTO = 0.10

# Calcular el precio con impuesto 
# precio_con_impuesto = precio_producto * (1 + TASA_IMPUESTO)

# Crear el diccionario con la informacion
producto_info = {"producto": nombre_producto, "precio": precio_con_impuesto}

# Mostrar el mensaje con el formato deseado
print(f"El producto {producto_info["producto"]} tiene un precio de {producto_info["precio"]:.2f}")

