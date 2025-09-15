#GENERA NUMEROS ALAEATORIOS ENTRE EL RANGO ESTABLECIDO
import random
cantidad=random.randint(5, 15)
print (f"cantidad= {cantidad}")
vector= []
for i in range(cantidad):
    vector.append(random.randint(1, 100))
print (vector)
Buscar = int(input("Digite el numero que desea buscar: "))

if Buscar in vector:
    print (f"El numero: {Buscar} si esta en la lista")

    indice = vector.index(Buscar)
    print(f"Se encuentra en el indice: {indice} de la tabla")

    repeticiones= vector.count(Buscar)
    print(f"Se repite: {repeticiones} vez/veces")

    posicion = [i+1 for i, num in enumerate(vector) if num==Buscar]
    print(f"Se encuentra en la posición {posicion} de la lista")
else:
    print("El numero no se encuentra dentro de la lista")

