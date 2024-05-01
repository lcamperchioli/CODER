# Te piden que calcules la nota final de estudiantes de Python
# La nota final se calcula basandonos en 3 notas previas de las cuales, cada una
# corresponde un % distintos de la nota final.
# Los % se detallan a continuacion: 
# - "nota_1" cuenta como el 20% de la nota final
# - "nota_2" cuenta como el 30% de la nota final
# - "nota_3" cuenta como el 50% de la nota final

# Aspectos a incluir

# Tener en cuenta los temas vistos en clase 1: numeros, print, input, variables,
# operaciones matematicas, cadena de texto.
# Los datos deben guardarse en variables y deben ser dinamicos por medio del input

# Resolucion 
# Ingreso de datos
nota_1 = int(input("Ingrese nota 1 "))
nota_2 = int(input("Ingrese nota 2 "))
nota_3 = int(input("Ingrese nota 3 "))

# Condiciones de borde

ponderacion_nota_1 = 0.2
ponderacion_nota_2 = 0.3
ponderacion_nota_3 = 0.5

# Formula 
nota_final = nota_1 * ponderacion_nota_1 + nota_2 * ponderacion_nota_2 + nota_3 * ponderacion_nota_3
nota_final = int(nota_final)

# Print
print(f"La nota final es {nota_final}")

