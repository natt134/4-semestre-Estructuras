##definicion de la clase, los datos y los apuntadores adelante y attras
class NodoDoble:
    def __init__(self,dato):
        self.dato=dato
        self.siguiente=None
        self.anterior=None

# Definición de la clase ListaDoble: representa una lista doblemente enlazada.
class ListaDoble:
    def __init__(self):
        # Al crear la lista, inicialmente no hay nodos.
        # Por eso, tanto la cabeza (inicio) como la cola (final) están vacías.
        self.cabeza = None
        self.cola = None

    # Método para agregar un nuevo elemento (nodo) al final de la lista.
    def agregar(self, dato):
        # Se crea un nuevo nodo con el valor 'dato'.
        # Este nodo tendrá punteros a su nodo anterior y siguiente (al inicio son None).
        nuevo = NodoDoble(dato)

        # Si la lista está vacía (no hay cabeza todavía):
        if not self.cabeza:
            # El nuevo nodo se convierte tanto en la cabeza como en la cola de la lista,
            # ya que es el único elemento.
            self.cabeza = nuevo
            self.cola = nuevo

        else:
            # Si la lista ya tiene al menos un elemento:

            #La cola actual (último nodo) apunta hacia el nuevo nodo como su siguiente.
            self.cola.siguiente = nuevo

            #El nuevo nodo apunta hacia atrás (anterior) al nodo que antes era la cola.
            nuevo.anterior = self.cola

            #Finalmente, el nuevo nodo pasa a ser la nueva cola (último elemento).
            self.cola = nuevo

    # Método para recorrer la lista desde el inicio (cabeza) hasta el final (cola).
    def adelante(self):
        # Se empieza desde la cabeza.
        actual = self.cabeza

        # Mientras haya un nodo actual, se imprime su dato.
        while actual:
            print(actual.dato)
            # Luego se avanza al siguiente nodo.
            actual = actual.siguiente

        # Cuando se llega al final (actual = None), se imprime "None" para indicar el fin.
        print("None")

    # Método para recorrer la lista desde el final (cola) hacia el inicio (cabeza).
    def atras(self):
        # Se empieza desde la cola.
        actual = self.cola

        # Mientras haya un nodo actual, se imprime su dato.
        while actual:
            print(actual.dato)
            # Luego se retrocede al nodo anterior.
            actual = actual.anterior

        # Cuando se llega al inicio (actual = None), se imprime "None" para indicar el fin.
        print("None")

#se agregan los nodos a la lista
l1=ListaDoble()
#se agrega el primer elemento
l1.agregar(10)
#se agrega el segundo elemento
l1.agregar(20)
#se agrega el tercer elemento
l1.agregar(30)
#se agrega el cuarto elemento
l1.agregar(40)
#se llama la funcion adelante para recorrer la lista desde la cabeza es decir el primer elemento hasta la cola que es el ultimo elemento.
l1.adelante()
#se llama la funcion atras para recorrer la lista desde la cola es decir el ultimo elemento hasta la cabeza que es el primer elemento.
l1.atras()