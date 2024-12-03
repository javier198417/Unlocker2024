from abc import ABC, abstractmethod  # Para implementar clases abstractas

# Clase base abstracta (Abstracción)
class Figura(ABC):
    def __init__(self, color):
        self.color = color  # Encapsulación: atributo protegido

    @abstractmethod
    def calcular_area(self):
        pass  # Método abstracto, debe ser implementado por las subclases

    def mostrar_color(self):
        return f"El color de la figura es {self.color}"

# Clase derivada: Círculo (Herencia)
class Circulo(Figura):
    def __init__(self, color, radio):
        super().__init__(color)
        self.radio = radio  # Encapsulación

    def calcular_area(self):
        return 3.1416 * self.radio ** 2

# Clase derivada: Rectángulo (Herencia y Polimorfismo)
class Rectangulo(Figura):
    def __init__(self, color, ancho, alto):
        super().__init__(color)
        self.ancho = ancho
        self.alto = alto

    def calcular_area(self):
        return self.ancho * self.alto

# Uso de las clases (Polimorfismo)
def mostrar_informacion(figura):
    print(figura.mostrar_color())
    print(f"El área es: {figura.calcular_area()}")

# Crear instancias
circulo = Circulo("Rojo", 5)
rectangulo = Rectangulo("Azul", 10, 20)

# Mostrar información usando polimorfismo
mostrar_informacion(circulo)
mostrar_informacion(rectangulo)