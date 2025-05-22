# 1.3.1. Automatizando el cálculo de la propina

'''
Clase:        Fundamentos de Programacion G2
Tema:         Variables, Tipos, entrada y salidad
Ejercicio:    1.3.1
Descripción:  Generador del Correo Key

Autor:        Roberto Carlos Iglesias Álvarez
Fecha:        2025-05-18
Estado:       [Terminado]
'''

Cuenta = float(input("Cual es el total de la cuenta a pagar: "))
Propina = float(input("Cuanto porcentaje de propina quiere dar? (5%, 10%, 15%): "))

if Propina == 5:
     Total = Cuenta + Cuenta * 0.05
elif Propina == 10:
     Total = Cuenta + Cuenta * 0.10
elif Propina == 15:
     Total = Cuenta + Cuenta * 0.15
else:
     print("Lo siento, porcentaje de propina no aceptado. seleccione uno entre 5% y 15%")

print("Total de la cuenta a pagar:", Total) 
