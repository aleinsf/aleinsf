""" 
* EJERCICIO:
 * - Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.
 * - Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 * - Crea una variable (y una constante si el lenguaje lo soporta).
 * - Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).
 * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
"""
# https://www.python.org/
# comentario de una sola línea

string = "string"
integer = 20
float = 20.2
boolean = True

# variables y concatenación
name = "Python"
welcome = "¡Hola, " + name + "!"
print(welcome)

# f-strings
welcome = f"¡Hola, {name}!"
print(welcome)  

# operadores de pertenencia
print("Python" in welcome) # true
print("Python" not in welcome) # false

# datos compuestos
list = ["Alejandro","Insfran", 1,78] # se puede modificar
tuple = ("Alejandro","Insfran", 1,78) # no se puede modificar
set = {"Alejandro","Insfran", 1,78} # no se puede modificar, se puede reconstruir, no almacena datos duplicados
dictionary = {
    "nombre" : "--",
    "apellido" : "--",
    "altura" : "--",
    "estado" : True
}

list[2] = 1.74 # acceder a dato 
print(set)
print(list[1])
print(dictionary["estado"])
