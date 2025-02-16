""" 
* EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
"""

# operadores de pertenencia
nombre = "--"
bienvenida_al_usuario = "hola " + nombre + " ¿como estas?"
print(bienvenida_al_usuario)

# operadores aritméticos
suma = 12 + 5
resta = 12 - 5
mult = 12 * 5
div = 12 / 5
exp = 12 ** 5
div_doble = 12 // 5
resto = 12 % 5
 
# operadores logicos
op_logicos = {
    "and" : True and False,
    "or" : True or False,
    "not" : not True
} 

# operadores de comparación
op_comparacion = {
    "igual_que" : 5 == 6 ,
    "distinto_que" : 5 != 6 ,
    "mayor_que" : 5 > 6 ,
    "menor_que" : 5 < 6 ,
    "mayor_o_igual" : 5 >= 6 ,
    "menor_o_igual" : 5 <= 6
}

# operadores de asignación
a = 5 # igual
a += 5 # suma
a -= 5 # resta
a *= 5 # multiplicación
a /= 5 # división
a **= 5 # exponenciación
a //= 5 # división entera
a %= 5 # módulo

# operadores de identidad
op_identidad = {
    "is" : 5 is 6,
    "is not" : 5 is not 6
}

# operadores de bits
op_bits = {
    "and" : 5 & 6,
    "or" : 5 | 6,
    "xor" : 5 ^ 6,
    "not" : ~5,
    "desplazamiento izquierda" : 5 << 6,
    "desplazamiento derecha" : 5 >> 6
}

""" * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
"""

for i in range(10,56):
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print(i)
    