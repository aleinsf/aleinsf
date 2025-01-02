from numpy import random
import numpy as np

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
print(matriz)

matriz2 = random.rand(5, 5)
print(matriz2)