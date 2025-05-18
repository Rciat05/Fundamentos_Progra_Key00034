# 1.3.2. Generador del correo de Key

'''
Clase:        Fundamentos de Programacion G2
Tema:         Variables, Tipos, entrada y salidad
Ejercicio:    1.3.2
Descripción:  Generador del Correo Key

Autor:        Roberto Carlos Iglesias Álvarez
Fecha:        2025-05-18
Estado:       [Terminado]
'''

Nombres= str(input("Escriba sus nombres: "))
Apellidos = str(input("Escriba sus apellidos: "))
parteNombre = Nombres.split()
parteApellidos = Apellidos.split()


print(f"Nombre Completo: {Nombres} {Apellidos}")
print(f"Tu correo es {parteNombre[0]}.{parteApellidos[0]}@keyinstitute.edu.sv")