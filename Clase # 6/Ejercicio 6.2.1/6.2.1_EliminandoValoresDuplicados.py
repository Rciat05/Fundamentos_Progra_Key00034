'''
Clase:        Fundamentos de Programacion G2
Tema:         Manejo de listas
Ejercicio:    6.2.2
Descripción:  Manejo de valores repetidos

Autor:        Roberto Carlos Iglesias Álvarez
Fecha:        2025-05-30
Estado:       [Terminado]
'''


# Manejo de listas.
ValoresEntrada = input("Ingrese los numeros de entrada separado por espacios: ")
lista = ValoresEntrada.split()
lista_NoRepetidos = []

for i in lista:
    if i not in  lista_NoRepetidos:
        lista_NoRepetidos.append(i)

imprimirLista = ", ".join(lista_NoRepetidos)

print(imprimirLista)