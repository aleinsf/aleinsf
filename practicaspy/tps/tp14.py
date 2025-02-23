"""
/*
 * EJERCICIO:
 * Crea dos variables utilizando los objetos fecha (date, o semejante) de tu lenguaje:
 * - Una primera que represente la fecha (día, mes, año, hora, minuto, segundo) actual.
 * - Una segunda que represente tu fecha de nacimiento (te puedes inventar la hora).
 * Calcula cuántos años han transcurrido entre ambas fechas.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la fecha de tu cumpleaños, formatéala y muestra su resultado de
 * 10 maneras diferentes. Por ejemplo:
 * - Día, mes y año.
 * - Hora, minuto y segundo.
 * - Día de año.
 * - Día de la semana.
 * - Nombre del mes.
 * (lo que se te ocurra...)
 */
"""

import datetime

act_datetime = datetime.datetime.now()
birth_datetime = datetime.datetime(2005, 11, 11, 20, 30, 42)
"""
print(act_datetime)
print(birth_datetime)
print((act_datetime - birth_datetime))
"""
def format():
    a = birth_datetime.strftime("%d-%m-%Y %H:%M:%S")
    b = birth_datetime.strftime("%d-%m-%Y %H:%M")
    c = birth_datetime.strftime("%d-%m-%Y %H")
    d = birth_datetime.strftime("%d-%m-%Y")
    e = birth_datetime.strftime("%d-%m")
    f = birth_datetime.strftime("%d") 
    g = birth_datetime.strftime("%d-%m %H:%M:%S")
    h = birth_datetime.strftime("%d-%Y %H:%M:%S")
    i = birth_datetime.strftime("%d-%m %H:%M") 
    j = birth_datetime.strftime("%m-%Y %H:%M:%S")

    print(a, b, c, d, e, f, g, h, j)

format()