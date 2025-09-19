# 2. Llenar dos arreglos de n elementos con números generados con la función random.
# Compararlos y decir:
# a. Cuál de los dos tiene la suma más alta
# b. Cuál de los dos tiene el número mayor
# c. Cuál de los dos tiene el número menor
# d. Cuál es el promedio conjunto (uniendo los dos arreglos)
# e. Sacar el promedio de cada uno y decir si está por encima o por debajo del
# promedio de las listas juntas
# f. Cuál de los dos tiene mayor cantidad de pares
# g. Cuál de los dos tiene mayor cantidad de impares
import random
def llenarvector1 (lista1):
    cantidad=random.randint(5,15)
    for i in range (cantidad):
        lista1.append(random.randint(1,100))
    return lista1
def llenarvector2 (lista2):
    cantidad=random.randint(5,15)
    for i in range (cantidad):
        lista2.append(random.randint(1,100))
    return lista2

def suma(lista1,lista2):
    total=0
    total2=0
    for numero1 in lista1:
        total+=numero1
    
    for numero2 in lista2:
        total2 += numero2
    
    if total>total2:
        return(f"El arreglo con mayor suma es el #1, con la suma total de: {total}")
    else:
        return(f"El arreglo con mayor suma es el #2, con la suma total de: {total2}") 

def NumeroMayor (lista1,lista2):
    Nmayor1=lista1[0]
    Nmayor2=lista2[0]
    for numero1 in lista1:
        if numero1>Nmayor1:
         Nmayor1=numero1
    for numero2 in lista2:
        if numero2>Nmayor2:
          Nmayor2=numero2
    if Nmayor1>Nmayor2:
        print("El numero mayor se encuentra en el arreglo #1")
    else:
        print("El numero mayor se encuentra en el arreglo #2")
    return Nmayor1,Nmayor2

def NumeroMenor (lista1,lista2):
    Nmenor1=lista1[0]
    Nmenor2=lista2[0]
    for numero1 in lista1:
        if numero1<Nmenor1:
         Nmenor1=numero1
    for numero2 in lista2:
        if numero2<Nmenor2:
          Nmenor2=numero2
    if Nmenor1<Nmenor2:
        print("El numero menor se encuentra en el arreglo #1")
    else:
        print("El numero menor se encuentra en el arreglo #2")
    return Nmenor1,Nmenor2

def PromedioConjunto(lista1,lista2):
    total1=sum(lista1)
    total2=sum(lista2)
    sumatotal=total1+total2
    cantidadtotal=len(lista1)+len(lista2)
    promedio=sumatotal/cantidadtotal
    print(f"El promedio es igual a: {promedio}")
    return promedio

def PromedioIndividual (lista1,lista2):
    promedio1=(sum(lista1)/len(lista1))
    print(f"El promedio del arreglo #1 es : {promedio1}")
    promedio2=(sum(lista2)/len(lista2))
    print(f"El promedio del arreglo #2 es : {promedio2}")
    promedio=PromedioConjunto(lista1,lista2)
    if promedio1 > promedio:
     print("EL promedio #1 está por encima del promedio en conjunto ")
    else:
     print("EL promedio #1 está por debajo del promedio en conjunto ")
    if promedio2>promedio:
     print("El promedio #2 esta por encima del promedio en conjunto")
    else:
     print("El promedio #2 esta por debajo del promedio en conjunto")  
    return promedio1,promedio2

milista1=[]
milista2=[]
llenarvector1(milista1)
print(f"Arreglo #1: {(milista1)}")
llenarvector2(milista2)
print(f"Arreglo #2: {(milista2)}")
print(suma(milista1,milista2))
NumeroMayor(milista1,milista2)
NumeroMenor(milista1,milista2)
PromedioConjunto(milista1,milista2)
PromedioIndividual(milista1,milista2)


    