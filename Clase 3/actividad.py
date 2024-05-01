# Crear un conjunto que osea los siguientes elementos:
# Colores: Rojo, Blanco, Azul
# Agrega posteriormente al set de colores, los valores de: Violeta y Dorado
# Elimina los colores Celeste, Blanco y Dorado

# ¿Que pasa si queremos eliminar el color Celeste usando el metodo discard?

# Resolucion 
colores = {"Rojo", "Blanco", "Azul"}
print(colores)

colores.add("Violeta")
colores.add("Dorado")
print(colores)

colores.discard("Blanco")
print(colores)
colores.discard("Celeste")
print(colores)
colores.discard("Dorado")
print(colores)

colores.remove("Violeta")
print(colores)

# Con remove se levanta un error porque te avisa que lo que queres eliminar no
# existe

