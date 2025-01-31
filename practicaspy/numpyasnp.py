from numpy import random
import numpy as np
import pandas as pd



array1 = np.array([[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], [[11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]])
# print(array1)

# array1 = array1.reshape(5, 2)
# print(array1)

# for matriz in array1:
  # for fila in matriz:
      # for elemento in fila:
        # print(elemento)

####################################################################################################

array01 = np.array([[1, 2,], [3, 4]])
array02 = np.array([[5, 6], [7, 8]])

arcon = np.concatenate((array01, array02), axis=1)
# print(arcon)
newarr = np.array_split(arcon, 2)
# print(newarr)

array03 = np.array([1, 2, 3, 4, 5, 1, 7, 8, 1, 1])
x = np.where(array03 == 1)
# print(x)

array04 = np.array([0, 3, 2, 5, 1])
# print(np.sort(array04))


#for x in range(11):
 # numero = random.randint(10)
 # print(numero)

decimal = random.rand()
# print(round(decimal, 5) + 5)

####################################################################################################

matriz = random.randint(2, size=(5, 5))
# print(matriz)

matriz2 = random.rand(5, 5)
# print(matriz2)

 

nombres = ["Juan", "Pedro", "Maria", "Ana"]
ganador = random.choice(nombres, size = (3, 5))
# print(ganador)


arreglo = np.array([1, 2, 3, 4, 5])

# Operaciones básicas con arreglos
suma = arreglo + 10           # Sumar 10 a cada elemento
multiplicacion = arreglo * 2  # Multiplicar cada elemento por 2
potencia = arreglo ** 2       # Elevar cada elemento al cuadrado 

print("Arreglo original:", arreglo)
print("Suma:", suma)
print("Multiplicación:", multiplicacion)
print("Potencia:", potencia)

# Crear matrices y realizar operaciones
matriz = np.array([[1, 2], [3, 4]])
transpuesta = matriz.T  # Transponer la matriz

# Operaciones entre matrices
matriz2 = np.array([[5, 6], [7, 8]])
producto_punto = np.dot(matriz, matriz2)  # Producto punto
suma_matrices = matriz + matriz2          # Suma de matrices


print("\nMatriz original:")
print(matriz)
print("Transpuesta:")
print(transpuesta)
print("Producto punto:")
print(producto_punto)
print("Suma de matrices:")
print(suma_matrices)

# Funciones útiles
arreglo_grande = np.random.rand(5)  # Arreglo de números aleatorios
media = np.mean(arreglo_grande)     # Media del arreglo
desviacion = np.std(arreglo_grande) # Desviación estándar

print("\nArreglo aleatorio:", arreglo_grande)
print("Media:", media)
print("Desviación estándar:", desviacion)


naranjas = pd.Series([3, 2, 1])

print(naranjas) 