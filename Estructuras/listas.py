#DICCIONARIO
var={"letra":"a",
     "numero":100}
#SET O CONJUNTO
var1={1,2,3}
print(type(var1))
#TUPLA
var2=("a",567,"asa")
#LISTAS SIMILARES A LOS ARREGLOS DE JAVA
# O A LOS ARRAYLIST O LINKEDLIST DE JAVA
listas=[1,"udec",3.8]
listas.append("estructuras")
print(listas)
for i in range (len(listas)):
    print(listas[i])

for elemento in listas:
    print(elemento)

#GENERA NUMEROS ALAEATORIOS ENTRE EL RANGO ESTABLECIDO
import random
cantidad=random.randint(5, 15)
print (f"cantidad= {cantidad}")
vector= []
for i in range(cantidad):
    vector.append(random.randint(1, 100))
print (vector)
