class NodoDoble:#clse Nodo
    def __init__(self,dato):
        self.dato=dato
        self.siguiente=None
        self.anterior=None# dato anterior 

class ListaDoble:#clase de la lista
    def __init__(self):
        self.cabeza=None#inicio
        self.cola=None#ultimo
        self.cont=0#contador
    def agregar(self,dato):#funcion agregar
        nuevo=NodoDoble(dato)
        if not self.cabeza:# si la cabeza esta vacia , el primer dato agrgado sera el primero
            self.cabeza=nuevo
            self.cola=nuevo
        else:# entoces 
            self.cola.siguiente=nuevo
            nuevo.anterior=self.cola
            self.cola=nuevo
        self.cola.siguiente=self.cabeza
        self.cabeza.anterior=self.cola
        self.cont+=1
    
    def adelante(self):#funcion adelate
        actual=self.cabeza
        i=0
        while actual and i<self.cont:#mientras el dato actual y el contador i sea menor al contador iniscial
            print(actual.dato)#se imprime los datos actuales 
            actual=actual.siguiente#cadavez que se agregue un numero actual , se abrira un nuevo nodo
            i+=1
        
        
    def atras(self):#funcion atras(Comienza desde la cola (el último nodo).Imprime los datos de atrás hacia adelante.)
        actual=self.cola
        i=0
        while actual and i<self.cont:
            print(actual.dato)
            actual=actual.anterior
            i+=1
        

l1=ListaDoble()
l1.agregar(456)
l1.agregar(444)
l1.agregar(555)
l1.agregar(678)

l1.adelante()
print("="*50)
l1.atras()