class NodoDoble:
    def __init__(self,dato):
        self.dato=dato
        self.siguiente=None
        self.anterior=None

class ListaDoble:
    def __init__(self):
        self.cabeza=None
        self.cola=None
        self.cont=0
    def agregar(self,dato):
        nuevo=NodoDoble(dato)
        if not self.cabeza:
            self.cabeza=nuevo
            self.cola=nuevo
        else:
            self.cola.siguiente=nuevo
            nuevo.anterior=self.cola
            self.cola=nuevo
        self.cola.siguiente=self.cabeza
        self.cabeza.anterior=self.cola
        self.cont+=1
    
    def adelante(self):
        actual=self.cabeza
        i=0
        while actual and i<self.cont:
            print(actual.dato)
            actual=actual.siguiente
            i+=1
        
        
    def atras(self):
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