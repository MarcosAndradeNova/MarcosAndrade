class Nodo:
    def __init__(self, clave):
        self.clave = clave
        self.izquierda = None
        self.derecha = None
        self.altura = 1

class ArbolAVL:
    def __init__(self):
        self.raiz = None

    # Función para obtener la altura de un nodo
    def altura(self, nodo):
        if not nodo:
            return 0
        return nodo.altura

    # Función para obtener el factor de balanceo de un nodo
    def balance_factor(self, nodo):
        if not nodo:
            return 0
        return self.altura(nodo.izquierda) - self.altura(nodo.derecha)

    # Rotación simple a la derecha
    def rotacion_derecha(self, y):
        x = y.izquierda
        T2 = x.derecha

        # Realizar la rotación
        x.derecha = y
        y.izquierda = T2

        # Actualizar alturas
        y.altura = max(self.altura(y.izquierda), self.altura(y.derecha)) + 1
        x.altura = max(self.altura(x.izquierda), self.altura(x.derecha)) + 1

        # Devolver la nueva raíz
        return x

    # Rotación simple a la izquierda
    def rotacion_izquierda(self, x):
        y = x.derecha
        T2 = y.izquierda

        # Realizar la rotación
        y.izquierda = x
        x.derecha = T2

        # Actualizar alturas
        x.altura = max(self.altura(x.izquierda), self.altura(x.derecha)) + 1
        y.altura = max(self.altura(y.izquierda), self.altura(y.derecha)) + 1

        # Devolver la nueva raíz
        return y

    # Función para insertar un nuevo nodo
    def insertar(self, nodo, clave):
        # 1. Realizar la inserción normal de un árbol binario de búsqueda
        if not nodo:
            return Nodo(clave)

        if clave < nodo.clave:
            nodo.izquierda = self.insertar(nodo.izquierda, clave)
        else:
            nodo.derecha = self.insertar(nodo.derecha, clave)

        # 2. Actualizar la altura del nodo ancestro
        nodo.altura = 1 + max(self.altura(nodo.izquierda), self.altura(nodo.derecha))

        # 3. Obtener el factor de balanceo y balancear el árbol si es necesario
        balance = self.balance_factor(nodo)

        # Si el nodo se desbalancea, realizar las rotaciones apropiadas

        # Rotación a la derecha
        if balance > 1 and clave < nodo.izquierda.clave:
            return self.rotacion_derecha(nodo)

        # Rotación a la izquierda
        if balance < -1 and clave > nodo.derecha.clave:
            return self.rotacion_izquierda(nodo)

        # Rotación izquierda-derecha
        if balance > 1 and clave > nodo.izquierda.clave:
            nodo.izquierda = self.rotacion_izquierda(nodo.izquierda)
            return self.rotacion_derecha(nodo)

        # Rotación derecha-izquierda
        if balance < -1 and clave < nodo.derecha.clave:
            nodo.derecha = self.rotacion_derecha(nodo.derecha)
            return self.rotacion_izquierda(nodo)

        return nodo

    # Función de inserción que invoca el proceso desde la raíz
    def insertar_raiz(self, clave):
        self.raiz = self.insertar(self.raiz, clave)

    # Función para imprimir el árbol en orden (in-order)
    def imprimir_inorden(self, nodo):
        if nodo:
            self.imprimir_inorden(nodo.izquierda)
            print(nodo.clave, end=" ")
            self.imprimir_inorden(nodo.derecha)

# Ejemplo de uso:
if __name__ == "__main__":
    arbol = ArbolAVL()
    
    # Insertando valores en el árbol AVL
    arbol.insertar_raiz(10)
    arbol.insertar_raiz(20)
    arbol.insertar_raiz(30)
    arbol.insertar_raiz(15)
    arbol.insertar_raiz(25)
    
    # Imprimiendo el árbol en orden
    print("Árbol AVL en orden:")
    arbol.imprimir_inorden(arbol.raiz)
