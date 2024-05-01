# Partiras de: 
# matriz = [
# [1,5,1],
# [2,1,2],
# [3,0,1],
# [1,4,4],
# ]

# Debes llegar a: 
# matriz = [
# [1,5,1,7],
# [2,1,2,5],
# [3,0,1,4],
# [1,4,4,9],
# ]

# Resolucion 
matriz = [
 [1,5,1],
 [2,1,2],
 [3,0,1],
 [1,4,4],
 ]

matriz[0] += [sum(matriz[0])]
matriz[1] += [sum(matriz[1])]
matriz[2] += [sum(matriz[2])]
matriz[3] += [sum(matriz[3])]

print(matriz)



