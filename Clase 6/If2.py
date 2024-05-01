num = 24
if num > 30:
    print("El numero es mayor a 30")
else: 
    print("El numero es menor o igual a 30")

x = 25
if x > 10:
    print("Por encima de 10")
    if x > 20:
        print("y tambien mayor a 20")
    else: 
        print("pero no es mayor que 20")

a = 2 + 3
if a == 4:
    print("a es igual a 4")
    if a == 5:
        print("es igual a 5")
        if a == 6:
            print("a es igual a 6")
        else:
            print("Fuera de rango") 

comando = "SALIR"

if comando == "ENTRAR":
        print("Bienvenido al sistema")
if comando == "SALUDO":
        print("HOLA")
if comando == "SALIR":
        print("Saliendo del sistema")
else: 
        print("No se reconoce el comando")

if comando == "ENTRAR":
     print("Bienvenido al sistema")
elif comando == "SALUDO":
      print("HOLA")
print("FIN")
