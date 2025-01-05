import pandas as pd
import numpy as np

naranjas = pd.Series([3, 2, 0, 1])

manzanas = pd.Series([10, 23, 1, 93, 2, 0, 1])

datos = pd.Series({"peso": 100, "altura": 1.75, "edad": 21})
# print(datos)

# print(datos.size)
# print(datos.index)
# print(datos.dtype)
 
# print(datos["peso":"edad"])

edades = [29, 10 , 13, 12, 10]
nombres = ["Juan", "Pedro", "Maria", "Ana", "Luis"]

serie_edades = pd.Series(edades, index=nombres)
# print(serie_edades)
# print(serie_edades["Juan":"Ana"])

######################## dataframes

datos = {
    "nombre": ["Juan", "Pedro", "Maria", "Ana", "Luis"],
    "edad": [29, 10 , 13, 12, 10],
    "peso": [70, 45, 50, 40, 30]
}

dataframe = pd.DataFrame(datos, index=["a", "b", "c", "d", "e"])
print(dataframe)

df = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns=["a", "b", "c"])
print(df) 

dfnp = pd.DataFrame(np.random.rand(10, 10), columns=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"])
#print(dfnp)