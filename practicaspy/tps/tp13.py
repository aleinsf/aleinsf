"""
/*
 * EJERCICIO:
 * Crea una función que se encargue de sumar dos números y retornar
 * su resultado.
 * Crea un test, utilizando las herramientas de tu lenguaje, que sea
 * capaz de determinar si esa función se ejecuta correctamente.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un diccionario con las siguientes claves y valores:
 * "name": "Tu nombre"
 * "age": "Tu edad"
 * "birth_date": "Tu fecha de nacimiento"
 * "programming_languages": ["Listado de lenguajes de programación"]
 * Crea dos test:
 * - Un primero que determine que existen todos los campos.
 * - Un segundo que determine que los datos introducidos son correctos.
 */
"""
import unittest as ut

def suma(a, b):

    return a + b


class TestSuma(ut.TestCase):
   
    def test_suma_positivos(self):
        self.assertEqual(suma(2, 3), 5)
    
    def test_suma_negativos(self):
        self.assertEqual(suma(-1, -1), -2)
    
    def test_suma_ceros(self):
        self.assertEqual(suma(0, 0), 0)


if __name__ == "__main__":
    ut.main()
