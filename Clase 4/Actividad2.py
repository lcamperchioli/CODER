# Escribir un programa que guarde en una variable en un diccionario 
# {'Dolar':'$','Euro':'€', 'Libra':'£'}.
# Luego se le debera solicitar al usuario que ingrese la divisa que desea visualizar
# En el caso de ingresar una divisa no existente, deberemos indicarle con un
# mensaje de notificacion que la divisa no se encuentra disponible

# Creamos el diccionario de divisas 
divisas = {'Dolar':'$','Euro':'€', 'Libra':'£'}

# Solicitamos al usuario que ingrese la divisa
entrada = input("Ingrese la divisa: ").strip().capitalize()

# Buscamos la divisa en el diccionario y la imprimimos
valor = divisas.get(entrada)
print(f"La divisa {entrada} tiene el simbolo {valor}")
