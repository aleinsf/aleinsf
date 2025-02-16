"""
/*
 * IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
 * 
 * EJERCICIO:
 * Desarrolla un programa capaz de crear un archivo XML y JSON que guarde los
 * siguientes datos (haciendo uso de la sintaxis correcta en cada caso):
 * - Nombre
 * - Edad
 * - Fecha de nacimiento
 * - Listado de lenguajes de programación
 * Muestra el contenido de los archivos.
 * Borra los archivos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la lógica de creación de los archivos anteriores, crea un
 * programa capaz de leer y transformar en una misma clase custom de tu 
 * lenguaje los datos almacenados en el XML y el JSON.
 * Borra los archivos.
 */
"""
import json
import os

# JSON 

json_file = "aleinsf.json"
datos = { 
        "name": "Alejandro",
        "age": 19,
        "birthdate": "11 de noviembre año 2005",
        "languages": ["R",  "Python"]
    }

with open(json_file, "w") as file:
    json.dump(datos, file, indent=4)




# XML

import xml.etree.ElementTree as xml

data = { 
    "name": "Alejandro",
    "age": 19,
    "birthdate": "11 de noviembre año 2005",
    "languages": ["R", "Python"]
}

xml_file = "aleinsf.xml"
def save_xml():

    root = xml.Element("data")

    for key, value in data.items():
        child = xml.SubElement(root, key)
        if isinstance(value, list):
            for item in value:
                xml.SubElement(child, "item").text = item

        else:    
            child.text = str(value)
    
    tree = xml.ElementTree(root)
    tree.write(xml_file)

save_xml()





# delete


#os.remove(xml_file)
#os.remove(json_file)


class Data:
    def __init__(self, name, age, birthdate, languages):
        self.name = name
        self.age = age
        self.birthdate = birthdate
        self.languages = languages

with open(xml_file, "r") as xml_data:

    root = xml.fromstring(xml_data.read())
    name = root.find("name").text
    age = root.find("age").text
    birthdate = root.find("birthdate").text
    languages = root. find("languages").text

    xml_class = Data(name, age, birthdate, languages)
    print(xml_class.__dict__)


with open(json_file, "r") as json_data:
    json_dict = json.load(json_data)
    json_class = Data(
        json_dict["name"], 
        json_dict["age"], 
        json_dict["birthdate"], 
        json_dict["languages"]
    )
    print(json_class.__dict__)
        
        

