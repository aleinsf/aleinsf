"""
/*
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 */
 """

# por valor

a = 5
b = a
b = 10
print(a) # 5
print(b) # 10

int0 = 5
def por_valor(int1: int):
    int1 = 10
    print(int1) # 10

# por referencia

a = [1,2,3]
b = a
b[0] = 10
print(a) # [10,2,3]
print(b) # [10,2,3]


def por_ref(list1: list):
    list1.append(4)
    list2 = list1
    list2.append(5)
    print(list1) 
    print(list2)

list0 = [1,2,3]    
por_ref(list0) # [1,2,3,4]



def por_valor(a: int, b: int) -> tuple:
    temp = a
    a = b
    b = temp
    return a, b

a = 5
b = 10
por_valor(a, b)


def por_referencia(a: list, b: list) -> tuple:
    temp = a
    a = b
    b = temp
    a.append(11)
    return a, b

a = [1,2,3] 
b = [4,5,6]
por_referencia(a, b)
print(a) # [4,5,6]
print(b) # [1,2,3]


# git add 
# git commit -m "message"
# git push origin master
# git pull origin master
# git checkout -b "branch_name"
# git checkout master
# git merge branch_name
# git branch -d branch_name
# git origin -d branch_name
    