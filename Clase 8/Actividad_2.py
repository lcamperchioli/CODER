# Escribir una funcioon que reciba una muestra de numeros en una lista y devuelva
# su media.

def promediar(notas: list[float]) -> float:
    promedio = sum(notas) / len(notas)
    return promedio 

def ingresar_notas() -> list[float]:
    notas = []
    while True: 
        entrada = input("Ingrese nota (s para salir): ")
        if entrada == "s":
            break
        nota = float(entrada)
        notas.append(nota)
    return notas

def mostrar_datos(promedio: float) -> None:
    print(f"El promedio de las notas es: {promedio}")

def main():
    notas = ingresar_notas()
    promedio = promediar(notas)
    mostrar_datos(promedio) 

main()