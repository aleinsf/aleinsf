""" 
* EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
"""

# estructuras de datos
# lista
lista = ["Alejandro", "Insfran", "aleinsf"] # se puede modificar
lista.append("nuevo dato")
lista.remove("nuevo dato")
lista[2] = 1.74
print(lista)

nums = [1, 2, 3, 4, 5]
sorted_nums = sorted(nums)
print(sorted_nums)
sort_nums = nums.sort(reverse=True)
print(nums)

# tupla
tupla = ("Alejandro", "Insfran", "aleinsf") # no se puede modificar
print(tupla)

# conjunto
conjunto = {"Alejandro", "Insfran", "aleinsf"} # no se puede modificar, se puede reconstruir, no almacena datos duplicados
conjunto.add("nuevo dato")
# conjunto.remove("nuevo dato")
print(conjunto)

# diccionario
diccionario = {
    "nombre" : "Alejandro",
    "apellido" : "Insfran",
    "usuario" : "aleinsf"
}
diccionario["usuario"] = "aleinsf2"
print(diccionario)

"""
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
"""

# agenda
def agenda():
    contactos = {}
    while True:
        print("1. Buscar contacto")
        print("2. Insertar contacto")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")
        operacion = input("Introduce el número de la operación a realizar: ")
        if operacion == "1":
            nombre = input("Introduce el nombre del contacto: ")
            if nombre in contactos:
                print(contactos[nombre])
            else:
                print("El contacto no existe")
        elif operacion == "2":
            nombre = input("Introduce el nombre del contacto: ")
            telefono = input("Introduce el teléfono del contacto: ")
            if telefono.isdigit() and len(telefono) >= 11:
                contactos[nombre] = telefono
            else:
                print("Número de teléfono no válido")
        elif operacion == "3":
            nombre = input("Introduce el nombre del contacto: ")
            telefono = input("Introduce el teléfono del contacto: ")
            if telefono.isdigit() and len(telefono) >= 11:
                contactos[nombre] = telefono
            else:
                print("Número de teléfono no válido")
        elif operacion == "4":
            nombre = input("Introduce el nombre del contacto: ")
            if nombre in contactos:
                del contactos[nombre]
            else:
                print("El contacto no existe")
        elif operacion == "5":
            break
        else:
            print("Operación no válida")

agenda()    

