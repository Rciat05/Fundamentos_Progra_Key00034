'''
Clase:        Fundamentos de Programacion G2
Tema:         Bloques iterativos
Ejercicio:    5.3.1
Descripción:  Suma de valores

Autor:        Roberto Carlos Iglesias Álvarez
Fecha:        2025-05-31
Estado:       [Terminado]
'''


listaDeNumeros = input("Ingresa una lista de numeros separadas por espacios:")
lista = list(map(int, listaDeNumeros.split()))
suma = 0

for numero in lista:
    suma += numero

print(f"La el resultado de sumar: {listaDeNumeros}, es {suma}")
    

