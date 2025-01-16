# Clase Base: Animal
class Animal:
    def __init__(self, nombre, especie):
        self.__nombre = nombre  # Encapsulación: atributo privado
        self.__especie = especie  # Encapsulación: atributo privado

    def hacer_sonido(self):
        pass  # Método abstracto que será sobrescrito en las clases derivadas

    def obtener_nombre(self):
        return self.__nombre

    def obtener_especie(self):
        return self.__especie


# Clase Derivada: Perro (Herencia de Animal)
class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre, "Perro")  # Llamada al constructor de la clase base
        self.__raza = raza  # Atributo privado específico de Perro

    def hacer_sonido(self):  # Polimorfismo: Sobrescritura de método
        return f"{self.obtener_nombre()} dice: ¡Guau!"

    def obtener_raza(self):
        return self.__raza


# Clase Derivada: Gato (Herencia de Animal)
class Gato(Animal):
    def __init__(self, nombre, color):
        super().__init__(nombre, "Gato")  # Llamada al constructor de la clase base
        self.__color = color  # Atributo privado específico de Gato

    def hacer_sonido(self):  # Polimorfismo: Sobrescritura de método
        return f"{self.obtener_nombre()} dice: ¡Miau!"

    def obtener_color(self):
        return self.__color
# Creando instancias de las clases derivadas
perro = Perro("Max", "Golden Retriever")
gato = Gato("Felix", "Negro")

# Demostrando polimorfismo: Llamada al mismo método en objetos diferentes
print(perro.hacer_sonido())  # Salida: Max dice: ¡Guau!
print(gato.hacer_sonido())  # Salida: Felix dice: ¡Miau!

# Accediendo a atributos encapsulados mediante métodos públicos
print(f"El nombre del perro es {perro.obtener_nombre()} y su especie es {perro.obtener_especie()}.")
print(f"El gato es de color {gato.obtener_color()} y su especie es {gato.obtener_especie()}.")