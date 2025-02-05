"""
/*
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
 */
 """



def imprimir_numeros(n: int) -> None:
    if n < 0:
        return
    print(n)
    imprimir_numeros(n - 1)
imprimir_numeros(10)


def factorial(n: int):
    if n < 0:
        print("Numero invalido(negativo)")
    elif n == 0:
        return 1
    else:
        return n * (factorial(n - 1))

factorial(-2) 


def fibo(num: int) -> int:
    if num < 0:
        print("Numero no valido (negativo)") 
    elif num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibo(num + 1) + fibo(num - 2)

fibo(2)
