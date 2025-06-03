
'''
Clase:        Fundamentos de Programacion G2
Tema:         Guía Numpy
Ejercicio:    1.3.2
Descripción:  Cuestionario usando Numpy

Autor:        Roberto Carlos Iglesias Álvarez
Fecha:        2025-06-03
Estado:       [Terminado]
'''

import numpy as np

consumo = np.array([
    [12.5, 13.2, 11.9, 14.0, 13.5, 15.0, 14.3],
    [10.1, 10.5, 10.0, 11.2, 11.5, 12.0, 11.8],
    [14.0, 14.2, 13.9, 15.5, 15.1, 16.0, 15.8],
    [9.0, 9.2, 8.9, 9.5, 9.8, 10.0, 9.7],
    [16.2, 16.5, 16.0, 17.1, 17.4, 18.0, 17.8],
    [11.0, 11.3, 11.1, 12.0, 12.4, 12.8, 12.5],
    [13.5, 13.8, 13.2, 14.1, 14.6, 15.0, 14.9],
    [10.8, 11.0, 10.6, 11.5, 11.8, 12.2, 12.0],
    [15.1, 15.5, 15.0, 16.0, 16.4, 17.0, 16.7],
    [8.5, 8.7, 8.4, 9.0, 9.2, 9.5, 9.3],
])

# 1. ¿Cuál es el consumo del hogar 5 el viernes (día 5)?

print("Consumo del hogar 5 el viernes:", consumo[4,4])

# 2. Usando indexación, muestra el consumo de los últimos 3 hogares el domingo.

consumo_domingo_3_casas = consumo[-3:, -1]
print("Las utlimas 3 casa consumiendo el dia domingo un total de: ", consumo_domingo_3_casas)

# 3 Calcula el promedio de consumo los fines de semana (sábado y domingo, columnas 5 y 6).
columnas_fin_de_Semana = consumo[:, 5:7]
promedio_fin_de_Semana = np.mean(columnas_fin_de_Semana)

print()
# 4. ¿Qué día de la semana tiene la mayor desviación estándar entre hogares? Explica qué indica esto.

desviaciones = np.std(consumo, axis = 0)
print("desviaciones:", desviaciones)
indice_mayor = np.argmax(desviaciones)
print("Indice mayor; ",indice_mayor) # 5

'''
El índice 5 indica que el día sábado (índice 5 en la semana) tiene la mayor desviación estándar entre los hogares.

Esto significa que el consumo de energía ese día fue muy desigual entre las casas: algunas consumieron mucho, otras poco.
En cambio, los días con desviación más baja tuvieron un consumo más uniforme entre todas las casas. '''

# 5. Identifica los 3 hogares con menor consumo total durante la semana. Muestra sus índices y valores.

consulo_por_casa = np.sum(consumo, axis = 1)
consumo_menor = np.argsort(consulo_por_casa)[:3]

print("Las casa con menor consumo son: ", consumo_menor)

print()
# 6. Si el hogar 3 aumenta su consumo en un 10% cada día, ¿cuál sería su nuevo consumo total semanal?

casa3 = consumo[2] * 1.10
consumo_total_3 = np.sum(casa3)
print("El consumo total de la casa 3 mas por el 10 por ciento de consumo es", consumo_total_3 )
