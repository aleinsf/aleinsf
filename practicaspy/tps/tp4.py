"""
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
 *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
"""
cadena_ejemplo = "hola mundo"   
print(cadena_ejemplo[0]) # h
print(cadena_ejemplo[0:4]) # hola
print(len(cadena_ejemplo)) # 10
print(cadena_ejemplo + " " + "python") # hola mundo python
print(cadena_ejemplo * 3) # hola mundo hola mundo hola mundo
for letra in cadena_ejemplo:
    print(letra)
print(cadena_ejemplo.upper()) # HOLAMUNDO
print(cadena_ejemplo.lower()) # holamundo
print(cadena_ejemplo.replace("hola", "adios")) # adios mundo
print(cadena_ejemplo.split(" ")) # ['hola', 'mundo']
print(" ".join(cadena_ejemplo)) # h o l a   m u n d o
print(f"{cadena_ejemplo} python") # hola mundo python
print(cadena_ejemplo.isalnum()) # False
print(cadena_ejemplo.isalpha()) # False
print(cadena_ejemplo.isdecimal()) # False
print(cadena_ejemplo.isdigit()) # False
print(cadena_ejemplo.isidentifier()) # False
print(cadena_ejemplo.islower()) # True
print(cadena_ejemplo.isnumeric()) # False
print(cadena_ejemplo.isprintable()) # True
print(cadena_ejemplo.isspace()) # False
print(cadena_ejemplo.istitle()) # False
print(cadena_ejemplo.isupper()) # False
print(cadena_ejemplo.startswith("hola")) # True
print(cadena_ejemplo.endswith("mundo")) # True
print(cadena_ejemplo.count("o")) # 2
print(cadena_ejemplo.find("o")) # 1



"""
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
"""
anagramas = [
    ("amor", "roma"),
    ("arte", "reta"),
    ("dame", "meda"),
    ("rama", "amar"),
    ("barco", "cobra"),
    ("ratón", "tornar"),
    ("salta", "atlas"),
    ("nada", "adan"),
    ("perla", "lapre"),
    ("mora", "ramo"),
    ("corte", "tocer"),
    ("roca", "caro"),
    ("pico", "copi"),
    ("tenso", "santo"),
    ("esto", "otes"),
    ("pieza", "ezpa"),
]
def programa(palabra1, palabra2):
    
    if palabra1 == palabra1[::-1]:
        print(f"{palabra1} es palíndromo")
    else:
        print(f"{palabra1} no es palíndromo")
    if palabra2 == palabra2[::-1]:
        print(f"{palabra2} es palíndromo")
    else:
        print(f"{palabra2} no es palíndromo")
    
    if palabra1 and palabra2 in anagramas:
        print(f"{palabra1} y {palabra2} son anagramas")
    elif palabra1 in anagramas and palabra2 not in anagramas:
        print(f"{palabra1} es anagrama y {palabra2} no")
    elif palabra1 not in anagramas and palabra2 in anagramas: 
        print(f"{palabra2} es anagrama y {palabra1} no")
    elif palabra1 not in anagramas and palabra2 not in anagramas:
        print(f"{palabra1} y {palabra2} no son anagramas")
    
    if len(set(palabra1)) == len(palabra1)
        print(f"{palabra1} es isograma")
    else:
        print(f"{palabra1} no es isograma")
    if len(set(palabra2)) == len(palabra2)
        print(f"{palabra2} es isograma")
    else:
        print(f"{palabra2} no es isograma")

print(programa("oso", "ramon")) # True

        
    
    

    


print(programa("oso")) # True