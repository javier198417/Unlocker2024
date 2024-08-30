# ordenar_matriz.py
def ordenar_fila(matriz, fila):
    matriz[fila].sort()
    return matriz

matriz = [
    [3, 2, 1],
    [6, 5, 4],
    [9, 8, 7]
]

fila_a_ordenar = 1
print("Matriz original:")
for fila in matriz:
    print(fila)

matriz_ordenada = ordenar_fila(matriz, fila_a_ordenar)
print("\nMatriz con la fila ordenada:")
for fila in matriz_ordenada:
    print(fila)