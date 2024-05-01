cadena = " Esta es una prueba con Python "

print("upper:", cadena.upper())
print("lower:", cadena.lower())
print("title:", cadena.title())
cadena_strip = cadena.strip()
print("strip:", cadena_strip, end= "***")
print("capitalize:", cadena_strip.capitalize())

print("replace:", cadena.replace("Python", "Pithon"))
print("find:", cadena.find("a"))
print("find:", cadena.find("A"))

print("startswith:", cadena.startswith(" Esta"))
print("count:", cadena.count("a"))
print("isdigit:", cadena.isdigit())

print(" ** Esta es una Prueba **".strip("**"))
