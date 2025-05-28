'''
Clase:        Fundamentos de Programacion G2
Tema:         Bloque condicional
Ejercicio:    2.3.2
Descripción:  Validador de contraseña

Autor:        Roberto Carlos Iglesias Álvarez
Fecha:        2025-05-18
Estado:       [Terminado]
'''


# Contrasena valida
contrasena = input("Introduce la contraseña: ")

logintud = len(contrasena) >= 8
mayuscula = any(caracter.isupper() for caracter in contrasena)
numero = any(caracter.isdigit() for caracter in contrasena)

if logintud and mayuscula and numero:
    print("Contrasena valida")
else:
    print("Contrasena no valida")
