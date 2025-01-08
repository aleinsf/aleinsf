import random 

# datos simples
"string"
'string'
"""datos:
         nombre: --
         apellido: -- """
int = 20
float = 20.2
booleanos = True + False

# variables y concatenación 
nombre = "--"
bienvenida_al_usuario = "hola " + nombre + " ¿como estas?"
print(bienvenida_al_usuario)


# f-strings (f=pasar a string)
bienvenida = f"Hola {nombre} ¿como estas?"

# operadores de pertenencia 
# print("--" in bienvenida) # true
# print("--" not in bienvenida) # false

# datos compuestos 
lista = ["Alejandro","Insfran", 1,78] # se puede modificar
tupla = ("Alejandro","Insfran", 1,78) # no se puede modificar
conjunto = {"Alejandro","Insfran", 1,78} # no se puede modificar, se puede reconstruir, no almacena datos duplicados
diccionario = {
    "nombre" : "--",
    "apellido" : "--",
    "altura" : "--",
    "estado" : True
}

lista[2] = 1.74
# print(conjunto)
# print(lista[1])
# print(diccionario["estado"])

# op. aripmeticos
suma = 12 + 5 
resta = 12 - 5
mult = 12 * 5
div = 12 / 5
exp = 12 ** 5
div_doble = 12 // 5
resto = 12 % 5

# type(dato) nos devuelve que tipo de dato es
tipo_de_dato = type(suma)
# print(tipo_de_dato)

# op. de comparación 
op_comparacion = {
        "igual_que" : 5 == 6 ,
        "distinto_que" : 5 != 6 ,
        "mayor_que" : 5 > 6 ,
        "menor_que" : 5 < 6 ,
        "mayor_o_igual" : 5 >= 6 ,
        "menor_o_igual" : 5 <= 6
}
# print(op_comparacion) 

ingreso_mensual = 1234500
gasto_mensual = 123456

# condicionales; if, else, elif 
if ingreso_mensual > 1000 :
    if ingreso_mensual - gasto_mensual < 0 :
         print("estas en deficit")
    elif ingreso_mensual - gasto_mensual > 30000 : 
         print("bien")
    else : 
         print("cagaste")

# logicos; AND; OR; NOT
resultados = {
    "resultado1" : True & True ,
    "resultado2" : True & False ,
    "resultado3" : False & True ,
    "resultado4" : False & False ,
    "resultado5" : True | True ,
    "resultado6" : True | False , 
    "resultado7" : False | True ,
    "resultado8" : False | False ,
    "resultado9" : not True ,
    "resultado10" : not False 
}
# print(resultados)

# metodos de cadenas (dir = función)
# print(dir(12)) # lista de metodos 
# print(dir("si")) # lista de metodos

mayusc = "si y no".upper()
minusc = "si y no".lower()
primer_letra_minusc = "si y no".capitalize()

busqueda_find = mayusc.find("SI")
busqueda_index = mayusc.index("SI")

# es_numerico = mayusc.isnumeric("1")
# es_alfa_numerico = mayusc.isalpha("a")

coincidencias = mayusc.count("a")

# print(busqueda_find)

# def

num = random.randint(1,28)

def crear_contraseña_random(num):
     chars = "abcdefghijklmnñopqrstuvwxyz"
     num_entero = str(num)
     c1 = num - 2
     c2 = num
     c3 = num - 5 
     contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}{num**12}"
     print(contraseña)

crear_contraseña_random(num)
