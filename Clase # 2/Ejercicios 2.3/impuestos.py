'''
Clase:        Fundamentos de Programacion G2
Tema:         Bloque condicional
Ejercicio:    2.3.2
Descripción:  Ejercicios de Impuestos

Autor:        Roberto Carlos Iglesias Álvarez
Fecha:        2025-05-18
Estado:       [Terminado]
'''


Energia = int(input("Unidades consumidad de energia: "))

if Energia <= 100:
    print(" No hay impuestos por energia.")
    impuestos = 0
elif Energia >= 101 or Energia <= 200:
    impuestos = Energia + Energia * 0.5
elif Energia >= 201:
    impuestos = Energia + Energia * 0.7
else:
    ("Valor ingresado no valido")

print(f"El total a pagar de impuestos por energia es: {impuestos}")