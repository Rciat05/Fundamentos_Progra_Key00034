# 1.3.1. Automatizando el cálculo de la propina

'''
Clase:        Fundamentos de Programacion G2
Tema:         Variables, Tipos, entrada y salidad
Ejercicio:    1.3.1
Descripción:  Calculador de propina

Autor:        Roberto Carlos Iglesias Álvarez
Fecha:        2025-05-18
Estado:       [Terminado]
'''

Cuenta = float(input("Cual es el total de la cuenta a pagar: "))
Propina = float(input("Cuanto porcentaje de propina quiere dar? ")) / 100

impuesto = Cuenta * Propina
Total = Cuenta + impuesto

print("Total de la cuenta a pagar:", Total) 
