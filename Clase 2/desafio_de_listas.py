# Desafio de Listas
# Paso 1:Crea dos listas: lista_1 y lista_2
# Paso 2: añade a la lista_1 el <int> 456789 y luego el <str> "Hola Mundo"
lista_1 = [1, "Hola"]
lista_1.append(456789)
lista_1.append("Hola Mundo")
print(f"{lista_1=}")

# Paso 3: Luego añade a la lista_2 el <str> "Hola y Adios", y luego el <int> 5555
lista_2 = [2, "Chau"]
lista_2.append("Hola y Adios")
lista_2.append(5555)
print(f"{lista_2=}")

# Paso 4: Genera una lista_3 con todos los elemento sde la lista_1 sin considerar 
# el ultimo elemento
lista_3 = lista_1[:-1]
print(f"{lista_3=}")

# Paso 5: Genera una lista_4 con todos los elementos de la lista_2 menos el primero
# y el ultimo elemento 
lista_4 = lista_2[1:-1]
print(f"{lista_4=}")

# Paso 6: Finamente, genera una lista_5 con los elementos de lista_4 y lista_3
lista_5 = lista_4 + lista_3
print(f"{lista_5=}")