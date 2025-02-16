"""
/*
 * IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
 * 
 * EJERCICIO:
 * Desarrolla un programa capaz de crear un archivo que se llame como
 * tu usuario de GitHub y tenga la extensión .txt.
 * Añade varias líneas en ese fichero:
 * - Tu nombre.
 * - Edad.
 * - Lenguaje de programación favorito.
 * Imprime el contenido.
 * Borra el fichero.
 *
 * DIFICULTAD EXTRA (opcional):
 * Desarrolla un programa de gestión de ventas que almacena sus datos en un 
 * archivo .txt.
 * - Cada producto se guarda en una línea del archivo de la siguiente manera:
 *   [nombre_producto], [cantidad_vendida], [precio].
 * - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
 *   actualizar, eliminar productos y salir.
 * - También debe poseer opciones para calcular la venta total y por producto.
 * - La opción salir borra el .txt.
 */
"""
import os

def my_txt(name: str, content: list):
    with open(name, "w") as file:
        file.write("\n".join(map(str, content))) 

    with open(name, "r") as file:
        print(file.read())

    print(f"El archivo {name} ha sido creado con éxito y su contenido es: {content}")

content = "contenido"
contenido = [1, 2, 3, 4, 5, 6, 7]

my_txt("aleinsf", contenido)

os.remove() # remover




import os

def gestion():

    file_name = "Gestion ventas"

    while True:
        print("1. Añadir")
        print("2. Actualizar")
        print("3. Buscar")
        print("4. Eliminar")
        print("5. Mostrar productos")
        print("6. Calcular la venta total")
        print("7. Calcular venta por producto")
        print("8. Salir")
        action = input("Elige una de las opciones anteriores: ")
    
        if action == "1":
            product_name = input("Ingrese el nombre del producto: ")
            quantity = input("Ingrese la cantidad a añadir: ")
            price = input("Ingrese el precio del producto: ")

            with open( file_name, "a") as file:
                file.write(f"\n{product_name}, {quantity}, {price}")
                
        elif action == "2":
            with open(file_name, "r") as file:
                lines = file.readlines()

            num_line = int(input("Elija la linea a modificar: "))
            product_name = input("Ingrese el nombre del producto: ")
            quantity = input("Ingrese la cantidad a añadir: ")
            price = input("Ingrese el precio del producto: ")
            lines[num_line] = (f"{product_name}, {quantity}, {price}\n")
        
            with open(file_name, "w") as file:
                file.writelines(lines)
            print("Modificado con exito")
                     
        elif action == "3":           
            searched_word = input("ingrese el producto a buscar: ")

            with open(file_name, "r") as file:
                for num_line, line in enumerate(file, start=0):  # Leer línea por línea
                    if searched_word in line:  # Si la palabra está en la línea
                        print(f"Encontrado en línea {num_line}: {line.strip()}")
                    else:
                        print(f"El producto {searched_word} no esta listado en la linea {num_line}")
                          
        elif action == "4":
            num_line = int(input("Ingrese el numero de linea a borrar: "))

            with open(file_name, "r") as file:
                pop_lines = file.readlines()
            new_lines = []
            for i, line in enumerate(pop_lines):
                if i != num_line:  
                    new_lines.append(line)
            with open(file_name, "w") as files:
                files.writelines(new_lines)
            print("Eliminado con exito")
    
        elif action == "5":
            with open(file_name, "r") as file:
                for num_line, line in enumerate(file, start=0):
                    print(f"{num_line} {line}")
                    
        elif action == "6":
            total = 0 
            with open(file_name, "r")as file:
                for line in file.readlines():
                    components = line.split(", ")
                    quantity = int(components[1])
                    price = float(components[2])
                    total += quantity * price
            print(total)
        elif action == "7":
            name = input("Ingrese el nombre: ")
            total = 0 
            with open(file_name, "r")as file:
                for line in file.readlines():
                    components = line.split(", ")
                    if components[0] == name:
                        quantity = int(components[1])
                        price = float(components[2])
                        total += quantity * price
                    else:
                        print("El nombre del producto no esta listado :(")
            print(total) 
        elif action == "8":
            break
        else:
            print("Operacion invalida")
        

gestion()

