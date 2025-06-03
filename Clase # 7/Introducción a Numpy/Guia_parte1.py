# Introduccion a numpy

import numpy as np

my_list = [1, 2, 3, 4, 5] # Crea una matriz a partir de una lista
arr = np.array(my_list) 
print(arr)

zeros = np.zeros(5) # Crea una matriz de ceros
print(zeros)

ones = np.ones(5) # Crea una matriz de unos
print(ones)


# OPERACIONES CON MATRICES

# 1.5.1 Suma

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
resultado = arr1 + arr2
print(resultado)

# 1.5.2 multiplicacion

resultado = arr1 * arr2 
print(resultado)


# 1.6 BROADCAST

''' 1.6.1. Reglas de Broadcasting.
Si dos matrices tienen un número diferente de dimensiones, la forma de la matriz de menor dimensión se rellena con unos en el lado izquierdo.
Si la forma de las dos matrices no coincide en ninguna dimensión, la matriz con forma igual a 1 en esa dimensión se estira para 
que coincida con la forma de la otra matriz. Si no se cumple ninguna de estas condiciones, NumPy genera un error "ValueError".'''

# 1.6.2 Ejemplos de broadcasting 
arr = np.array([1 ,2 ,3 ])
resultado = arr + 5
print(resultado)

arr1 = np.array([1, 2, 3])
arr2 = np.array([[10], [20], [30]])
result = arr1 + arr2
print(result)


