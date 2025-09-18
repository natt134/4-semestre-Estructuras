
import random
#función para llenar un vector
#Reto: En lugar de salir de la función en la validación, 
#haga que el programa pida dos nuevos valores
#Hasta que se cumpla que estos valores esten en el rango
#de minimo 2 y máximo 50
# def llenarVector(lista,min,max):
#     if min<1 or max>50:
#         lista.append("desborda la capacidad de proceso")
#         return lista[0]
#     else:
#         cantidad=random.randint(min, max)
#         for i in range(cantidad):
#             lista.append(random.randint(1, 100))    
#         return lista

def llenarVector(lista):
    cantidad=random.randint(5, 15)
    for i in range(cantidad):
        lista.append(random.randint(1, 100))    
    return lista

def sumaLista(lista):
    suma=0
    for num in lista:
        suma+=num
    return suma

def promedioLista(lista):
    suma=sumaLista(lista)
    return suma/len(lista)    
    
milista=[]
llenarVector(milista)
print(milista)
print(sumaLista(milista))
print(promedioLista(milista))
