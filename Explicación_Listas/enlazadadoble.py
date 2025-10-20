class NodoDoble:
    def __init__(self,dato):
        self.dato=dato
        self.siguiente=None
        self.anterior=None

class ListaDoble:
    def __init__(self):
        self.cabeza=None
        self.cola=None
    def agregar(self,dato):
        nuevo=NodoDoble(dato)
        if not self.cabeza:
            self.cabeza=nuevo
            self.cola=nuevo
        else:
            self.cola.siguiente=nuevo
            nuevo.anterior=self.cola
            self.cola=nuevo
    
    def adelante(self):
        actual=self.cabeza
        while actual:
            print(actual.dato)
            actual=actual.siguiente
        print("None")
        
    def atras(self):
        actual=self.cola
        while actual:
            print(actual.dato)
            actual=actual.anterior
        print("None")

l1=ListaDoble()
l1.agregar(456)
l1.agregar(444)
l1.agregar(555)
l1.agregar(678)

l1.adelante()
l1.atras()