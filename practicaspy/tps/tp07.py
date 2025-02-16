"""
/*
 * EJERCICIO:
 * Implementa los mecanismos de introducción y recuperación de elementos propios de las
 * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 * o lista (dependiendo de las posibilidades de tu lenguaje).
 *
 * DIFICULTAD EXTRA (opcional):
 * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
 */
"""

# pila / stack 
stack = []

# push
stack.append(1)
stack.append(2)
stack.append(3)

# pop
stack_item = stack[len(stack) - 1]
del stack[len(stack) - 1]
print(stack)

print(stack.pop())
print(stack)


# cola / queue
queue = []

# enqueue 
queue.append(1)
queue.append(2)
queue.append(3)

# dequeue 
queue_item = queue[0]
del queue[0]
print(queue)

print(queue.pop(0))
print(queue)


def stack_web():
    
    stack = []

    while True:
        
        action = input(
            "URL o ordenes de navegacion (atras/ adelante/ salir): "
        )

        if action == "salir":
            print("Saliendo del navegador web")
            break

        elif action == "atras":
            if len(stack) > 0:
                stack.pop()

        elif action == "adelante":
            pass
        else:
            stack.append(action)  

        if len(stack) > 0:
            print(f"Has navegado a la URL: {stack[-1]}.")
        else:
            print("Has navegado a la pagina de inicio")

stack_web()


def impresora():

    queue = []

    while True:
        
        action = input(
            "salir/imprimir/agregar archivo "
        )

        if action == "salir":
            print("Saliendo de la impresora")
            break
        elif action == "imprimir":
            if len(queue) > 0: 
                print(f"Imprimiendo {(queue.pop(0))}")
            else:
                print("no hay archivos wachin")
        else:
            queue.append(action)
            print(f"Agregando: {action} a la lista")


impresora()


            