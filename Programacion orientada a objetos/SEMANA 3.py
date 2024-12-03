# Clase que representa la información diaria del clima
class ClimaSemanal:
    def __init__(self):
        # Atributo encapsulado para las temperaturas
        self.__temperaturas = []

    # Método para ingresar temperaturas diarias
    def ingresar_temperaturas(self):
        for i in range(7):
            temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
            self.__temperaturas.append(temp)

    # Método para calcular el promedio semanal
    def calcular_promedio(self):
        if len(self.__temperaturas) == 0:
            return 0
        return sum(self.__temperaturas) / len(self.__temperaturas)

    # Método para mostrar las temperaturas ingresadas
    def mostrar_temperaturas(self):
        return self.__temperaturas

# Programa principal
def main():
    print("Programa de cálculo del promedio semanal de temperaturas (POO)")
    clima = ClimaSemanal()
    clima.ingresar_temperaturas()
    promedio = clima.calcular_promedio()
    print(f"Las temperaturas ingresadas son: {clima.mostrar_temperaturas()}")
    print(f"El promedio semanal es: {promedio:.2f}°C")

# Llamada al programa principal
if __name__ == "__main__":
    main()