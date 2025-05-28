# Fase de fortalecimiento

# 5.1 caso de estudio

# Objetivo: Desarrollar una solución digital en Python que resuelva un problema real en el entorno de Key Institute, formentando tanto
# habilidades técnicas como blandas, trabajo en equipo, gestión de presupuesto(basico).

for i in range(3, 15, 3): # Va desde el numero 3 al 15 de 3 valores en 3 valores
 print(i , end=" -> ") # Imprime I y por cada valor en rango al final imprime ->

print()
for i in range(5, 0, -1):
    for j in range(i):
       print("*", end="")
    print()

print()

numeros = [1,2,3,4,5,6,7,8,9,10]

for num in numeros:
   if num in [2,3,5,7]:
      continue # Si se cumple la condicion, se cancela y pasa a la siguiente si encuentra el 2 y el 2 existe en la lista, lo salta.
   print(num)