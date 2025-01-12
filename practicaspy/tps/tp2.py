""" 
* EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 """

# def funcion():
def funcion():
    print("hola")
    def funcion_interna():
        print("hola desde funcion interna")
    funcion_interna()
funcion()

def funcion_con_parametros(parametro1, parametro2):
    print(parametro1, parametro2)
funcion_con_parametros("hola", "mundo")

def funcion_con_retorno():
    return "hola"
print(funcion_con_retorno())

def funcion_con_parametros_y_retorno(parametro1, parametro2):
    return parametro1 + parametro2
print(funcion_con_parametros_y_retorno("hola", "mundo"))

# global 
def funcion_global():
    global variable_global
    variable_global = "hola"
funcion_global()
print(variable_global)

# local
def funcion_local():
    variable_local = "hola"
    print(variable_local)
funcion_local()
# print(variable_local) # error

""" 
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
"""

def funcion_extra(parametro1, parametro2):
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(parametro1 + " " + parametro2)
        elif i % 3 == 0:
            print(parametro1)
        elif i % 5 == 0:
            print(parametro2)
        else:
            print(i)
    return i

print(funcion_extra("fizz", "buzz"))