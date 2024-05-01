# Crea un programa que le pida dos numeros enteros al usuario y diga por consola;
# si alguno de ellos es  multiplo del otro.La funcion debe llamarse es_multiplo()

def es_multiplo(numero1: int, numero2: int) -> bool:
    """Determina si un numero es multiplo de otro"""
    if numero1 % numero2 == 0:
        return True
    elif numero2 % numero1 == 0:
        return True
    else: 
        return False

def mostrar_resultado(respuesta: bool) -> None:
    """Muestra el resultado de la funcion es multiplo"""
    if respuesta == True: 
        print(f"Son multiplos")
    else: 
        print("No son multiplos")


def introducir_numeros() -> tuple[int, int]:
    numero_1 = int(input("Numero 1: "))
    numero_2 = int(input("Numero 2: "))
    return numero_1, numero_2

def main():
    numero1, numero2 = introducir_numeros()
    respuesta = es_multiplo(numero1, numero2)
    mostrar_resultado(respuesta) 

main()