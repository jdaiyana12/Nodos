class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazadaSimple:
    def __init__(self):
        self.cabeza = None

    # Inserta un nuevo nodo al principio de la lista
    def insertar_inicio(self, valor):
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    # Inserta un nuevo nodo al final de la lista
    def insertar_final(self, valor):
        nuevo_nodo = Nodo(valor)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            return
        ultimo = self.cabeza
        while ultimo.siguiente:
            ultimo = ultimo.siguiente
        ultimo.siguiente = nuevo_nodo

    # Busca un nodo con el valor dado
    def buscar(self, valor):
        actual = self.cabeza
        while actual:
            if actual.valor == valor:
                return True
            actual = actual.siguiente
        return False

    # Método para imprimir la lista (solo para visualización)
    def imprimir(self):
        actual = self.cabeza
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")

# Uso de la lista enlazada simple
lista_simple = ListaEnlazadaSimple()
lista_simple.insertar_inicio(10)
lista_simple.insertar_inicio(5)
lista_simple.insertar_final(15)
lista_simple.imprimir()  # Salida: 5 -> 10 -> 15 -> None
print(lista_simple.buscar(10))  # Salida: True
print(lista_simple.buscar(20))  # Salida: False
