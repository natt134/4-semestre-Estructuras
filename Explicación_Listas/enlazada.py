class Nodo():                                     # Clase Nodo
    def __init__(self,dato):   
        self.dato=dato                            #Atributo q almacena el dato
        self.siguiente=None                       #Atributo-puntero al siguiente nodo


class Lista:                                      # Clase Lista
    def __init__(self):                           # Constructor de la clase lista que contiene
        self.primero=None                         # la variable primero que almacena el primer dato (nodo) una vez que entra al if del método agregar y está enlazada 
                                                  # a none en un principio
        
    def agregar(self,dato):                       # Funcion agregar que:                                                  
        nuevo=Nodo(dato)                          # Instancia una variable "nuevo" de la clase Nodo donde se almacenan los datos que se van a gregando
        if not self.primero:                      # Una vez que ingresa el dato y se almacena en nuevo se evalúa el if donde se pregunta si no existe valor primero, lo 
            self.primero=nuevo                    # cual es verdadero, entonces; el valor primero ahora es el dato nuevo q ingresamos 
            
        else:                                     # Se evalúa a partir del segundo dato que se añade 
            actual=self.primero                   # Aparece otra variable llamada actual y esta va a ser igual al valor del primer dato que se guardo en la linea 14
            while actual.siguiente:               # Se evalúa a partir del tercer dato que se añade, donde si actual tiene un enlace siguiente a otro dato, entonces:
                actual=actual.siguiente           # la variable actual se actualiza y va a ser igual al siguiente dato que está enlazado (si actual es dato 1, ahora actual 
                                                  # es el dato 2, al recorrer nuevamente el ciclo si actual es dato 2, ahora va a ser dato 3....)
            actual.siguiente=nuevo                # Una vez que se agrega el segundo dato, actual se enlaza al dato nuevo 
        return 1                                  # Retorna un valor
    
    def eliminar(self,dato):                      # Función eliminar que:
        actual=self.primero                       # Actual apunta al primer nodo existente
        anterior=None                             # Se crea la variable anterior q guarda el nodo anterior al q esta evaluando
        while actual and actual.dato!=dato:       # Mientras exista un nodo actual y su dato no sea el q queremos eliminar
            anterior=actual                       # Guarda el nodo actual en la avriable anterior
            actual=actual.siguiente               # y actual se actualiza por el valor del siguiente nodo
        if not actual:                            # Si actual no tiene valor o no existe para el dato que ingresamos
            return                                # no retorna nada osea termina
        if not anterior:                          # Si anterior no tiene valor, significa q se quiere eliminar el primer nodo
            self.primero=actual.siguiente         # entonces ahora primero sera el sigueinte nodo del q se esta evaluando
        else:                                     # si anterior tiene un valor asignado (nodo anterior)
            anterior.siguiente=actual.siguiente   # entonces el nodo anterior del dato q queremos eliminar se enlaza con el siguiente nodo disponible 
            
    
    def imprimir(self):                           # Función imprimir que:
        actual=self.primero                       # esta variable alamacena el primer nodo de la lista                
        while actual:                             # mientras exista un valor para actual
            print(actual.dato)                    # imprime el dato que se encuentra almacenada en la variable actual (vuelta por vuelta del ciclo)
            actual=actual.siguiente               # se va actualizando la variable actual por el siguiente nodo (cuelta por vuelta del ciclo)

lili=Lista()                                      # Se cra la variable lili donde se almacena la lista
#print(type(lili))
lili.agregar('k')                                 # se llama la lista con su nombre (lili) y se llama la función agregar, seguido del dato (k) para que
                                                  # recorra todo el proceso de la función
lili.agregar(999)                                 # se llama la lista con su nombre (lili) y se llama la función agregar, seguido del dato (999) para que
                                                  # recorra todo el proceso de la función
lili.agregar(1000)                                # se llama la lista con su nombre (lili) y se llama la función agregar, seguido del dato (1000) para que
                                                  # recorra todo el proceso de la función
lili.imprimir ()                                  # Se llama la lista con su nombre (lili) y se llama la función imprimir para que muestre los nodos existentes
# l1.agregar(111)
# l1.eliminar(1112)
# l1.imprimir()
# l1.agregar(111)
# l1.agregar(333)
# l1.agregar(444)
# l1.imprimir()
# print("="*50)
# l1.eliminar(111)
# l1.imprimir()

                               
        


# a=Nodo(1)
# a=None
# if a:
#     print('hay nodo')
# else:

#     print('no nodo')
#class ListaEnlazada:
    
#lista=[1,2,3,2,5]
# print(lista)
# lista.remove(12)
# print(lista)
    