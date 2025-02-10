"""
/*
 * EJERCICIO:
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (teniendo en cuenta las posibilidades
 * de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función.
 *
 * DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.
 * 
 */
"""


class Usuario:
    
    def __init__(self, name:str, age:int, mail:str):
        self.name = name
        self.age = age
        self.mail = mail

    def print(self):
        print(
            f"Nombre: {self.name}, Edad: {self.age}, Mail: {self.mail}.")

usuarios = [
    Usuario("Juan", 25, "juan@example.com"),
    Usuario("María", 30, "maria@example.com"),
    Usuario("Carlos", 22, "carlos@example.com"),
]

for usuario in usuarios:
    usuario.print()

# LIFO

class Stack:

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if self.count() == 0:
            return None
        
        return self.stack.pop()
    
    def count(self):
        return len(self.stack)
    
    def print(self):
        for item in reversed(self.stack):
            print(item)

my_stack = Stack()
my_stack.push("A")
my_stack.push("B")
my_stack.push("C")
print(my_stack.count())
my_stack.print()
my_stack.pop()


# FIFO

class Queue:
    
    def __init__(self):
        self.queue = []

    def equeue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        if self.count() == 0:
            return None       
        return self.queue.pop(0)
    
    def count(self):
        return len(self.queue)
    
    def print(self):
        for item in (self.queue):
            print(item)

my_queue = Queue()
my_queue.equeue("A")
my_queue.equeue("B")
my_queue.equeue("C")

print(my_queue.count())
my_queue.print()
my_queue.dequeue()
my_queue.dequeue()
my_queue.print()

