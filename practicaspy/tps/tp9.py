"""
/*
 * EJERCICIO:
 * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 * implemente una superclase Animal y un par de subclases Perro y Gato,
 * junto con una función que sirva para imprimir el sonido que emite cada Animal.
 *
 * DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo.
 */
"""


class Animal:

    def __init__(self, name: str):
        self.name = name

    def sound(self):
        pass

# SUBCLASE  

class Dog(Animal):
     def sound(self):
        print("Guau!")

class Cat(Animal):
    def sound(self):
        print("Miau!")

def print_sound(animal : Animal):
    animal.sound()

my_dog = Dog("Perro")
my_cat = Cat("Gato")
my_animal = Animal("Animal")


print_sound(my_cat)
print_sound(my_dog)
print_sound(my_animal)




class Employees:
    def __init__(self, name : str, id : int):
        self.name = name
        self.id = id 
        self.employees = []
    
    def add(self, employees):
        self.employees.append(employees)

    def hierarchy(self):
        pass

class Managers(Employees):

    def hierarchy(self):
        print(f"{self.name} es manager")

    def add(self, employees : Employees):
        print(f"{self.name} esta a cargo de {employees.name}")
 

class Project_managers(Employees):
    
    def __init__(self, name : str, id : int, proyect : str):
        super().__init__(name, id)
        self.proyect = proyect

    def hierarchy(self):
        print(f"{self.name} es manager de proyectos")


class Programmers(Employees):
    
    def __init__(self, name : str, id : int, language : str):
        super().__init__(name, id)
        self.language = language

    def hierarchy(self):
        print(f"{self.name} es programador y su lenguaje es {self.language}")

    def add(self, employees):
        pass

def print_employeers(empleados : Employees):
    empleados.hierarchy()

managers = Managers("Juan Luaces", 82)
proyect_managers = Project_managers("Julio Sosa", 81, "ia dev")
programmers =  Programmers("Miguel Calo", 32, "python")

managers.add(proyect_managers)
proyect_managers.add(programmers)

print_employeers(managers)
print_employeers(proyect_managers)
print_employeers(programmers)

