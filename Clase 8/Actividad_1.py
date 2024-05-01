# Escribir una funcion a la que se le pase una cadena del nombre de una ciudad
# <ciudad> y muestre por pantalla el saludo ¡Le damos la bienvenida a <ciudad>!

# def saludar_ciudad(nombre):
#   print(f"¡Le damos la bienvenida a {nombre}!")

# saludar_ciudad("Mendoza")

def saludar_ciudad(nombre: str) -> str:
    mensaje = f"¡Le damos la bienvenida a {nombre}!"
    return mensaje

entrada = input("Ciudad: ")
mensaje = saludar_ciudad(entrada)
print(mensaje)

def ingresar_ciudad():
    entrada = input("Ciudad: ")
    return entrada

ciudad = ingresar_ciudad()
saludo = saludar_ciudad(ciudad)
print(saludo)

def main():
    entrada = ingresar_ciudad()
    mensaje = saludar_ciudad(entrada)
    print(mensaje)

main()
