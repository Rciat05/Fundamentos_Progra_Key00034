# Manejo de listas.

ValoresEntrada = input("Ingrese los numeros de entrada separado por espacios: ")
lista = ValoresEntrada.split()
lista_NoRepetidos = []

for i in lista:
    if i not in  lista_NoRepetidos:
        lista_NoRepetidos.append(i)

imprimirLista = ", ".join(lista_NoRepetidos)

print(imprimirLista)