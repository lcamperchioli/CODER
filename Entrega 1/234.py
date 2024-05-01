# Función para la contraseña
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

# Registro de usuarios
def register():
    nombre_usuario = input('Ingrese un nombre de usuario: ').capitalize()
    while True:
        if user(nombre_usuario):
            break
        else:
            nombre_usuario = input('Ingrese un nombre de usuario: ')
 
    caracteres = input('Ingrese una contraseña: ').strip()
    while True:
        if contraseña_usuario(caracteres):
            break
        else:
            caracteres = input('Ingrese una contraseña: ').strip()
 
    print('¡Bienvenido!')
   

# Nombre de usuarios
def user(nombre_usuario):
    letras = len(nombre_usuario)
    respuesta = nombre_usuario.isalnum()
 
    if letras < 6:
        print('El nombre de usuario debe contener al menos 6 caracteres')
    elif letras > 12:
        print('El nombre de usuario debe contener menos de 12 caracteres')
    elif not respuesta:
        print('El nombre de usuario puede contener solo letras y números')
        print('Hay espacios en blanco')
    else:
        return True

# Registrar usuarios
register()
