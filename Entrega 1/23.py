# Funcion para la contraseña
def password(key):
 
    # Declara las variables
    letters = len(key)
    lower_case = 0
    upper_case = 0
    numeric = 0
    space = 0
 
    # Comprueba que la contraseña es correcta
    if letters < 8:
        print('La contraseña debe contener 8 caracteres')
    else:
        for content in key:
            if content.islower() == True:
                lower_case += 1
            elif content.isupper() == True:
                upper_case += 1
            elif content.isdigit() == True:
                numeric += 1
            elif content.isspace() == True:
                    space += 1
                
 
        # Comprueba si la contraseña cumple con los parametros
        if lower_case >= 1:
            if upper_case >= 1:
                if numeric >= 1:
                        if space >= 1:
                            print('La contraseña no puede contener espacio en blancos')
                        else:
                            return True
                else:
                    print('La contraseña debe tener como minimo un caracter numerico')
            else:
                print('La contraseña debe tener como minimo un caracter en mayuscula')
        else:
            print('La contraseña debe tener como minimo un caracter en minuscula')
 
# Funcion para el nombre de usuario
def user(name):
 
    # Cuenta la cantidad de letras
    letters = len(name)
    answer = name.isalnum()
 
    # Comprueba que el nombre cumple lo especificado
    if letters < 6:
        print('El nombre de usuario debe contener al menos 6 caracteres')
    elif letters > 12:
        print('El nombre de usuario no puede contener mas de 12 caracteres')
    elif answer == False:
        print('El nombre de usuario puede contener solo letras y numeros')
        print('Nota: Evita los espacios en blanco')
    else:
        return True
 
# Funcion para simular el registro
def register():
 
    name = input('Ingrese un nombre de usuario: ')
    while 1:
        answer01 = user(name)
        if answer01 == True:
            break
        else:
            name = input('Ingrese un nombre de usuario: ')
 
    key = input('Ingrese una contraseña: ')
    while 1:
        answer02 = password(key)
        if answer02 == True:
            break
        else:
            key = input('Ingrese una contraseña: ')
 
    print('Se a finalizado el registro')
    print('Su usuario es:', name)
    print('Su contraseña es:', key)
 
register()