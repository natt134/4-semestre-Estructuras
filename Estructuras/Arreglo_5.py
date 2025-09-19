# Llenar un arreglo de n elementos con números generados con la función random. Cada
# número siguiente debe ser mayor que el anterior, pero no puede exceder el valor de la
# siguiente decena.

import random

n = int(input("¿Cuántos números quieres en el arreglo? "))
lista = []

num = random.randint(1, 9)
lista.append(num)

for i in range(1, n):
    
    siguiente_decena = ((num // 10) + 1) * 10
    
    num = random.randint(num + 1, siguiente_decena)
    lista.append(num)

print("Arreglo final:", lista)
