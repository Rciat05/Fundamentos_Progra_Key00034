'''
Clase:        Fundamentos de Programacion G2
Tema:         Bloques iterativos
Ejercicio:    5.4.2
Descripción:  Sumador de valores posicionales

Autor:        Roberto Carlos Iglesias Álvarez
Fecha:        2025-05-31
Estado:       [Terminado]
'''

valores = input("Ingrese el número que quiere sumar: ")

while int(valores) >= 10:
    suma = 0
    for numero in valores:
        suma += int(numero)
    print(f"{valores} = {suma}") 
    valores = str(suma)

print("El resultado final es:", valores)
