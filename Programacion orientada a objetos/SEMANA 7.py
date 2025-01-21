# Implementación de Constructores y Destructores en Python

class GestorRecurso:
    def __init__(self, recurso):
        """
        Constructor: Inicializa el objeto con el recurso especificado y lo "abre".
        :param recurso: Nombre del recurso a gestionar.
        """
        self.recurso = recurso
        print(f"Constructor: Recurso '{self.recurso}' inicializado y preparado.")

    def usar_recurso(self):
        """
        Método que simula el uso del recurso.
        """
        print(f"Usando el recurso '{self.recurso}'.")

    def __del__(self):
        """
        Destructor: Libera el recurso al destruir el objeto.
        """
        print(f"Destructor: Recurso '{self.recurso}' liberado correctamente.")

# Clase extendida para demostrar herencia y destructores adicionales
class GestorAvanzado(GestorRecurso):
    def __init__(self, recurso, nivel):
        """
        Constructor: Inicializa el recurso y un nivel adicional.
        :param recurso: Nombre del recurso.
        :param nivel: Nivel avanzado del gestor.
        """
        super().__init__(recurso)
        self.nivel = nivel
        print(f"Constructor: Gestor avanzado creado con nivel {self.nivel}.")

    def usar_recurso_avanzado(self):
        """
        Método adicional para usar el recurso en modo avanzado.
        """
        print(f"Usando el recurso '{self.recurso}' en modo avanzado con nivel {self.nivel}.")

    def __del__(self):
        """
        Destructor: Libera recursos específicos del gestor avanzado.
        """
        print(f"Destructor: Recurso avanzado '{self.recurso}' con nivel {self.nivel} liberado.")
        super().__del__()  # Llama al destructor de la clase base

# Ejemplo de uso de las clases
def main():
    print("Creando objeto de GestorRecurso...")
    recurso_simple = GestorRecurso("RecursoSimple")
    recurso_simple.usar_recurso()

    print("\nCreando objeto de GestorAvanzado...")
    recurso_avanzado = GestorAvanzado("RecursoAvanzado", nivel=5)
    recurso_avanzado.usar_recurso()
    recurso_avanzado.usar_recurso_avanzado()

    print("\nEliminando objetos...")
    del recurso_simple  # Elimina explicitamente el objeto para ver el destructor en acción
    del recurso_avanzado

if __name__ == "__main__":
    main()