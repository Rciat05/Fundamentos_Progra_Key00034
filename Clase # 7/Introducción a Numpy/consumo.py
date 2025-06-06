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

print("funciones:", consumo.ndim)
print("Forma:", consumo.shape)
print("Tipos de datos:", consumo.dtype)
print("Consumo primer hogar:", consumo[0])
print("Consumo el miercoles dia 3", consumo[:,2])

print()
# Promedio consumido por hogar
promedio_por_hogar = np.mean(consumo, axis = 1) # Axis 1 promedia por fila

# Promedio de consumo diario de todos los hogares
promedio_por_dia = np.mean(consumo, axis=0) # Axis = 0 promedia por columna

# Sumas total del consumo en la semana de los 10 hogares
promedio_semana = np.sum(consumo)

print(promedio_por_dia)
print(promedio_por_hogar)
print(promedio_semana)

print()
print()

#Maximos por hogar
maximos = np.max(consumo, axis = 1) # Mide el valor mas alto de cada hogar.

# Minimo por dia
minimos = np.min(consumo, axis=0) # Mide el valor mas bajo de cada dia.

# Desviaciones estandar global
desviaciones = np.std(consumo) # Mide cuanto varias los datos respecto al promedio.

print(maximos) 
print(minimos)
print(desviaciones)


print()

# Suma por hogar (semana)
consumo_total_hogar = np.sum(consumo, axis = 1)
# Indice del hogar con mayor consumo
consumo_minimo_semana = np.argmax(consumo_total_hogar)
# Indice del hogar con mejor consumo
hogar_mas_eficiente = np.argmin(consumo_total_hogar)

# np.sum(axis=1): Suma el consumo de cada hogar durante los 7 días.
# np.argmax y np.argmin: Encuentran la posición (índice) del hogar que consumió más y menos energía en la semana.

print(consumo_total_hogar)
print(consumo_minimo_semana)
print(hogar_mas_eficiente)
