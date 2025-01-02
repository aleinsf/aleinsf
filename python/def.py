import random 

num = random.randint(1,28)

def crear_contraseña_random(num):
     chars = "abcdefghijklmnñopqrstuvwxyz"
     num_entero = str(num)
     c1 = num - 2
     c2 = num
     c3 = num - 5 
     contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}{num**12}"
     print(contraseña)

crear_contraseña_random(num)