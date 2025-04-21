# Polinomio usando estructura dinamica (lista enlazada)

class Termino:
    def __init__(self, coeficiente, exponente):
        self.coeficiente = coeficiente  # valor del coeficiente
        self.exponente = exponente      # valor del exponente
        self.siguiente = None           # enlace al siguiente termino

    def get_coeficiente(self):
        return self.coeficiente

    def get_exponente(self):
        return self.exponente

    def set_coeficiente(self, coef):
        self.coeficiente = coef

    def set_exponente(self, exp):
        self.exponente = exp


class PolinomioDinamico:
    def __init__(self):
        self.inicio = None  # inicio de la lista enlazada

    def agregar_termino(self, coef, exp):
        nuevo = Termino(coef, exp)
        # Insertar ordenado por exponente descendente
        if self.inicio is None or self.inicio.exponente < exp:
            nuevo.siguiente = self.inicio
            self.inicio = nuevo
        else:
            actual = self.inicio
            while actual.siguiente and actual.siguiente.exponente > exp:
                actual = actual.siguiente
            if actual.exponente == exp:
                actual.coeficiente += coef
            else:
                nuevo.siguiente = actual.siguiente
                actual.siguiente = nuevo

    def mostrar(self):
        actual = self.inicio
        if not actual:
            print("0")
            return
        pol = ""
        while actual:
            signo = "+" if actual.coeficiente > 0 and actual != self.inicio else ""
            pol += f"{signo}{actual.coeficiente}x^{actual.exponente} "
            actual = actual.siguiente
        print(pol.strip())


# Polinomio usando estructura estatica (lista fija)

class TerminoEstatico:
    def __init__(self, coef, exp):
        self.coef = coef
        self.exp = exp

    def get_coef(self):
        return self.coef

    def get_exp(self):
        return self.exp

    def set_coef(self, c):
        self.coef = c

    def set_exp(self, e):
        self.exp = e


class PolinomioEstatico:
    def __init__(self, max_grado=10):
        self.terminos = [None] * max_grado  # lista fija de terminos

    def agregar_termino(self, coef, exp):
        if exp < len(self.terminos):
            if self.terminos[exp] is None:
                self.terminos[exp] = TerminoEstatico(coef, exp)
            else:
                nuevo_coef = self.terminos[exp].get_coef() + coef
                self.terminos[exp].set_coef(nuevo_coef)
        else:
            print("Exponente fuera de rango")

    def mostrar(self):
        pol = ""
        for i in range(len(self.terminos) - 1, -1, -1):
            term = self.terminos[i]
            if term:
                signo = "+" if term.get_coef() > 0 and pol else ""
                pol += f"{signo}{term.get_coef()}x^{term.get_exp()} "
        print(pol.strip() if pol else "0")


# Ejemplo de uso

print("Polinomio Dinamico:")
pd = PolinomioDinamico()
pd.agregar_termino(3, 2)
pd.agregar_termino(2, 1)
pd.agregar_termino(-5, 0)
pd.mostrar()

print("\nPolinomio Estatico:")
pe = PolinomioEstatico()
pe.agregar_termino(4, 3)
pe.agregar_termino(1, 1)
pe.agregar_termino(-2, 0)
pe.mostrar()