# Base de datos de usuarios 
usuario_base_de_datos = {}

def contraseña_usuario(caracteres):
 
    # Variables
    letras = len(caracteres)
    minuscula = 0
    mayuscula = 0
    numero = 0
    espacio = 0
 
    # Verificacion de la contraseña
    if letras < 8:
        print('La contraseña debe contener 8 caracteres')
    else:
        for content in caracteres:
            if content.islower() == True:
                minuscula += 1
            elif content.isupper() == True:
                mayuscula += 1
            elif content.isdigit() == True:
                numero += 1
            else:
                if content.isspace() == True:
                    espacio += 1
 
        # Verificacion de la contraseña 
        if minuscula >= 1:
            if mayuscula >= 1:
                if numero >= 1:
                    if espacio >= 1:
                        print('La contraseña no puede contener espacio en blanco')
                    else:
                        return True
                else:
                    print('La contraseña debe tener como mínimo un caracter numérico')
            else:
                print('La contraseña debe tener como mínimo un caracter en mayúscula')
        else:
            print('La contraseña debe tener como mínimo un caracter en minúscula')


# Registro nuevo usuario 
def registrar_usuario():
    nombre_usuario = input("Ingresa tu nombre de usuario: ")
    contraseña = input("Ingresa tu contraseña: ")
    usuario_base_de_datos[nombre_usuario] = contraseña
    print(f"¡Usuario {nombre_usuario} registrado exitosamente!")

# Informacion de los usuarios
def mostrar_usuarios():
    print("Usuarios registrados:")
    for nombre_usuario in usuario_base_de_datos:
        print(f"Nombre de usuario: {nombre_usuario}")

# Iniciar sesion 
def iniciar_sesion():
    nombre_usuario = input("Ingresa tu nombre de usuario: ")
    contraseña = input("Ingresa tu contraseña: ")
    if nombre_usuario in usuario_base_de_datos and usuario_base_de_datos[nombre_usuario] == contraseña:
        print(f"¡Bienvenido, {nombre_usuario}!")
    else:
        print("Nombre de usuario o contraseña incorrectos")

# Menú principal
while True:
    print("\nSistema de Registro de Usuarios")
    print("1. Registrar un nuevo usuario")
    print("2. Mostrar usuarios registrados")
    print("3. Iniciar sesión")
    print("4. Salir")
    opcion = input("Ingresa tu opción: ")

    if opcion == "1":
        registrar_usuario()
    elif opcion == "2":
        mostrar_usuarios()
    elif opcion == "3":
        iniciar_sesion()
    elif opcion == "4":
        print("Salida del programa")
        break
    else:
        print("Opción erronea")