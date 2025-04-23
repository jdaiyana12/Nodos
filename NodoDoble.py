class NodoDoble:
    def __init__(self, valor):
        self.valor = valor
        self.anterior = None
        self.siguiente = None

class ListaEnlazadaDoblemente:
    def __init__(self):
        self.cabeza = None

    # Inserta un nuevo nodo al principio de la lista
    def insertar_inicio(self, valor):
        nuevo_nodo = NodoDoble(valor)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            return
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza.anterior = nuevo_nodo
        self.cabeza = nuevo_nodo

    # Inserta un nuevo nodo al final de la lista
    def insertar_final(self, valor):
        nuevo_nodo = NodoDoble(valor)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            return
        ultimo = self.cabeza
        while ultimo.siguiente:
            ultimo = ultimo.siguiente
        ultimo.siguiente = nuevo_nodo
        nuevo_nodo.anterior = ultimo

    # Busca un nodo con el valor dado
    def buscar(self, valor):
        actual = self.cabeza
        while actual:
            if actual.valor == valor:
                return True
            actual = actual.siguiente
        return False

    # Método para imprimir la lista desde el principio (solo para visualización)
    def imprimir(self):
        actual = self.cabeza
        while actual:
            print(actual.valor, end=" <-> ")
            actual = actual.siguiente
        print("None")

# Uso de la lista doblemente enlazada
lista_doble = ListaEnlazadaDoblemente()
lista_doble.insertar_inicio(20)
lista_doble.insertar_inicio(10)
lista_doble.insertar_final(30)
lista_doble.imprimir()  # Salida: 10 <-> 20 <-> 30 <-> None
print(lista_doble.buscar(20))  # Salida: True
print(lista_doble.buscar(40))  # Salida: False
