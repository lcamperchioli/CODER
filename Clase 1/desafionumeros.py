cantidad_de_partidos = int(20)
cantidad_de_partidos_ganados = input("Ingrese cantidad de partidos ganados")
cantidad_de_partidos_ganados = int(cantidad_de_partidos_ganados)
cantidad_de_partidos_perdidos = cantidad_de_partidos - cantidad_de_partidos_ganados
cantidad_de_partidos_perdidos = int(cantidad_de_partidos_perdidos)

#calculo
puntos_totales = int(3 * cantidad_de_partidos_ganados - 1 * cantidad_de_partidos_perdidos)
puntos_totales = int(puntos_totales)
promedio = puntos_totales / cantidad_de_partidos

#Print

print(promedio)