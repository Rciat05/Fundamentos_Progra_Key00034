lista = [[1,2,3,4],
        [3,4,5,6], 
        [8,9,10,11], 
        [12,13,14,15]]

# Accediendo a la lista
print(lista[0])

# Accediendo a la fila 3
print(lista[2])

matriz = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12],
          [13,14,15,16]]

for fila in matriz:
    for elemento in fila:
        print(f"{elemento}", end=' ')
    print()  # Para saltar a la siguiente línea después de cada fila


for fila in range(len(matriz)):
    for j in range(len(matriz[fila])):
        print(f"{matriz[fila][j]}", end=' ')
    print()  # Para saltar a la siguiente línea después de cada fila
 