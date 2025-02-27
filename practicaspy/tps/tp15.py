"""
/*
 * EJERCICIO:
 * Utilizando tu lenguaje, crea un programa capaz de ejecutar de manera
 * asíncrona una función que tardará en finalizar un número concreto de
 * segundos parametrizables. También debes poder asignarle un nombre.
 * La función imprime su nombre, cuándo empieza, el tiempo que durará
 * su ejecución y cuando finaliza.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utilizando el concepto de asincronía y la función anterior, crea
 * el siguiente programa que ejecuta en este orden:
 * - Una función C que dura 3 segundos.
 * - Una función B que dura 2 segundos.
 * - Una función A que dura 1 segundo.
 * - Una función D que dura 1 segundo.
 * - Las funciones C, B y A se ejecutan en paralelo.
 * - La función D comienza su ejecución cuando las 3 anteriores han
 *   finalizado.
 */
"""

import asyncio

async def tarea_1():
    print("Iniciando tarea 1")
    await asyncio.sleep(2)  # Simula una tarea de espera (como una llamada de red)
    print("Tarea 1 completada")

async def tarea_2():
    print("Iniciando tarea 2")
    await asyncio.sleep(1)  # Simula otra tarea de espera
    print("Tarea 2 completada")

# Función principal que ejecuta tareas asíncronas
async def main():
    # Ejecutar las tareas asíncronas
    await asyncio.gather(tarea_1(), tarea_2())

# Ejecutar el programa
asyncio.run(main())





##############


async def C():
    print("Iniciando tarea C")
    await asyncio.sleep(3)
    print("Tarea C completada")


async def B():
    print("Iniciando tarea B")
    await asyncio.sleep(2)
    print("Tarea B completada")


async def A():
    print("Iniciando tarea A")
    await asyncio.sleep(1)
    print("Tarea A completada")


async def D():
    print("Iniciando tarea D")
    await asyncio.sleep(1)
    print("Tarea D completada")
    
async def main():
    # Ejecutar las tareas asíncronas
    await asyncio.gather(C(), B(), A())
    await D()

asyncio.run(main())

