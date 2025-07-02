'''
Clase:        Fundamentos de Programacion G2
Tema:         Juego del Entorno 
Ejercicio:    10.3.2
Descripción:  Calcula la suma de los elementos vecinos de cada celda en una matriz

Autor:        Roberto Carlos Iglesias Álvarez
Fecha:        2025-07-01
Estado:       [Terminado]
'''
filas = int(input())
columnas = int(input())

matriz = []
for _ in range(filas):
    fila = input()
    numeros = list(map(int, fila.split(',')))
    matriz.append(numeros)

resultado = []
for i in range(filas):
    fila_resultado = []
    for j in range(columnas):
        suma_vecinos = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                ni = i + dx
                nj = j + dy
                if 0 <= ni < filas and 0 <= nj < columnas:
                    if matriz[ni][nj] == 1:
                        suma_vecinos += 1
        fila_resultado.append(suma_vecinos)
    resultado.append(fila_resultado)

for fila in resultado:
    print(fila)
