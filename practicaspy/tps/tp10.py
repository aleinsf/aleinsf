"""
/*
 * EJERCICIO:
 * Explora el concepto de manejo de excepciones según tu lenguaje.
 * Fuerza un error en tu código, captura el error, imprime dicho error
 * y evita que el programa se detenga de manera inesperada.
 * Prueba a dividir "10/0" o acceder a un índice no existente
 * de un listado para intentar provocar un error.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que sea capaz de procesar parámetros, pero que también
 * pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
 * corresponderse con un tipo de excepción creada por nosotros de manera
 * personalizada, y debe ser lanzada de manera manual) en caso de error.
 * - Captura todas las excepciones desde el lugar donde llamas a la función.
 * - Imprime el tipo de error.
 * - Imprime si no se ha producido ningún error.
 * - Imprime que la ejecución ha finalizado. 
 */
"""

def error(num1: int, num2: int):
    try:
        resultado = num1 / num2
        print(resultado)
    except Exception as e:
        print(f"Se ha producido un error: {type(e)}")


error(1, 0) 

def process_params(parameters: list):
    
    if len(parameters) < 3:
        raise IndexError()
    elif parameters[1] == 0:
        raise ZeroDivisionError()  
    
    else: 
        print("Se ha ejecutado el programa de manera correcta")

    print(parameters[2])
    print(parameters[0]/parameters[1])

try:
    process_params([1, 3, 2])
except IndexError as e:
    print("La lista debe tener al menos 2(dos) elementos")
except ZeroDivisionError as e:
    print("No se puede dividir por 0(cero)")
except Exception as e:
    print(f"Se ha producido un error inesperado: {e}")

print("El programa finalizo")



