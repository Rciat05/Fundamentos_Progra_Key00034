'''
Clase:        Fundamentos de Programacion G2
Tema:         Manejo de listas
Ejercicio:    6.3.1
Descripción:  Números lideres

Autor:        Roberto Carlos Iglesias Álvarez
Fecha:        2025-06-02
Estado:       [Terminado]
'''

numeros = list(map(int, input("Ingresa una lista de números separados por espacios: ").split()))
lideres = []
max_derecha = float('-inf')

for num in reversed(numeros):
    if num > max_derecha:
        lideres.append(num)
        max_derecha = num

print("Números líderes:", *reversed(lideres))

