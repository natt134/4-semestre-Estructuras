class Nodo:                                              # Clase Nodo
    def __init__(self, dato):
        self.dato=dato                                   #Atributo q almacena el dato
        self.siguiente=None                              #Atributo-puntero q apunta al siguiente nodo


class Circular:                                          # Clase Circular
    def __init__(self):                                  # Constructor de la clase lista que contiene:
        self.primero=None                                # Variable self primero donde se guarda el primer nodo de la lista
        self.cont=0                                      # contador que va incrementando segun ingresan los nodos
    
    def agregar(self,dato):                              # Metodo agregar que:
        nuevo=Nodo(dato)                                 # Instancia una variable "nuevo" de la clase Nodo donde se almacenan los datos que se van a gregando
        if not self.primero:                             # Si no existe self primero, es decir esta vacío (cuando recién se va a ingresar el primer dato)
            self.primero=nuevo                           # Entonces self primero ahora es el nuevo dato que se esta añadiendo
            nuevo.siguiente=self.primero                 # y el puntero siguiente del nodo nuevo se apunta a si mismo (es el mismo nodo) para mantener la circularidad
        else:                                            # Si existe dato en self primero, entonces: (cuando se ingresa el segundo dato)
            actual=self.primero                          # self primero se guarda en la variable actual
            while actual.siguiente !=self.primero:       # Mientras el nodo siguiente sea distinto del nodo self primero, entonces:
               actual=actual.siguiente                   # actual ahora pasa a ser el siguiente nodo (si actual era el nodo1 entonces ahora actual es el nodo2 ....)
               self.cont+=1                              # se incrementa el contador para saber el numero de vueltas q se ha dado con el ciclo          
            actual.siguiente=nuevo                       # El siguiente nodo del actual, es el nuevo nodo q se ha ingresado (si actual es el dato 1, el siguiente es el dato
                                                         # 2, si actual es el dato 2 su siguiente es el dato 3 ...)
            nuevo.siguiente=self.primero                 # para que se respete la circularidad, entonces el siguiente del ultimo y nuevo dato que se ha ingresado es self
                                                         # primero (si se ingresa el nodo 2: el primer nodo apunta al nodo2 (nuevo) y este apunta nuevamente al primer nodo
                                                         # (self primero)
            self.cont+=1                                 # A medida q se van ingresando los nodos, el contador va incrementando de 1 en 1
               
    def mostrar(self):                                   # Función mostrar que:
        actual=self.primero                              # actual es el primer nodo de la lista
        #while actual and actual!=self.primero:
        i=0                                              # Contador que se inicializa en 0 para recorrer la lista
        while actual and i< self.cont:                   # Mientras exista actual y el contador sea menor al total de nodos existentes
            print(actual.dato)                           # se imprime el dato del nodo actual
            actual=actual.siguiente                      # actual va cambiando de valor sucesivamente por el nodo siguiente
            i+=1                                         # Se va incrementado el contador cada vez q recorra el while
            
            
k=Circular()                                             # Se le asigna un nombre (k) a la lista circular
k.agregar(12)                                            # se llama la lista (k) con la función agregar y el dato (12) para que recorra todo el proceso
k.agregar(9)                                             # se llama la lista (k) con la función agregar y el dato (9) para que recorra todo el proceso
k.agregar(88)                                            # se llama la lista (k) con la función agregar y el dato (88) para que recorra todo el proceso
k.agregar(8800)                                          # se llama la lista (k) con la función agregar y el dato (8800) para que recorra todo el proceso
k.agregar(9988)                                          # se llama la lista (k) con la función agregar y el dato (9988) para que recorra todo el proceso
k.mostrar()                                              # se llama la lista (k) con la función mostrar para que imprima los nodos existentes