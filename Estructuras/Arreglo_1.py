import random
import statistics

def llenarvector (lista):
    cantidad=int(input("Ingrese el tamaño del arreglo: "))
    for i in range (cantidad):
        lista.append(random.randint(1, 100))    
    return lista
def sumaLista (lista):
    total=0
    for numero in lista:
     total += numero
    return total
def promedioLista(lista):
   promedio=0
   promedio=sumaLista(lista)/len(lista)
   return promedio
def NumeroMayor (lista):
   mayor=0
   for numero in lista:
      if numero > mayor:
         mayor = numero
   return mayor
def NumeroMenor (lista):
   menor=lista[0]
   for numero in lista:
      if numero <menor:
         menor = numero
   return menor
def Ascendente (lista):
   lista.sort()
   return lista
def Descendente (lista):
   return sorted(lista, reverse=True)
def Moda (lista):
    return statistics.multimode(lista)
def Mediana (lista):
    return statistics.median(lista)
def Buscar (lista):
  BscNumero=int(input("Que numero desea buscar: "))
  if BscNumero in milista:
    print(f"El numero: {BscNumero} se encuentra en la lista")

    posicion = [i+1 for i, num in enumerate(lista) if num==BscNumero]
    print(f"Se encuentra en la posición {posicion} de la lista")

    repeticiones= milista.count(BscNumero)
    print(f"Se repite: {repeticiones} vez/veces")




milista=[]
llenarvector(milista)
print(milista)

print("1. Suma ")
print("2. Promedio")
print("3. Numero Mayor")
print("4. Numero Menor")
print("5. Ordenar de forma ascendente")
print("6. Ordenar de forma descendente")
print("7. Moda")
print("8. Mediana")
print("9. Buscar: numero, posicion, repeticion")
print("10. Resumen de las operaciones")
opcion=int(input("Escoja la accion que desea realizar: "))

if opcion==1:
 print(f"La suma de los numeros es: {sumaLista(milista)}")
elif opcion==2:
 print(f"El promedio de los datos es: {promedioLista(milista)}")
elif opcion==3:
 print(f"El numero mayor de la lista es : {NumeroMayor(milista)}")
elif opcion==4:
 print(f"El numero menor de la lista es : {NumeroMenor(milista)}")
elif opcion==5:
 print(f"La lista ordenada de forma Ascendente es: {Ascendente(milista)}")   
elif opcion==6:
 print(f"La lista ordenada de forma Descendente es: {Descendente(milista)}")
elif opcion==7:
 print(f"La moda es: {Moda(milista)}")   
elif opcion==8:
 print(f"La mediana es: {Mediana(milista)}")   
elif opcion==9:
 print(f" {Buscar(milista)}")  
elif opcion==10:
 print(f"La suma de los numeros es: {sumaLista(milista)}")
 print(f"El promedio de los datos es: {promedioLista(milista)}")
 print(f"El numero mayor de la lista es : {NumeroMayor(milista)}")
 print(f"El numero menor de la lista es : {NumeroMenor(milista)}")
 print(f"La lista ordenada de forma Ascendente es: {Ascendente(milista)}")
 print(f"La lista ordenada de forma Descendente es: {Descendente(milista)}")
 print(f"La moda es: {Moda(milista)}")
 print(f"La mediana es: {Mediana(milista)}") 
 print(f" {Buscar(milista)}") 
