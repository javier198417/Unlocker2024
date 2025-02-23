import json

class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.inventario = {}
        self.archivo = archivo
        self.cargar_inventario()

    def cargar_inventario(self):
        try:
            with open(self.archivo, 'r') as file:
                self.inventario = json.load(file)
            print("Inventario cargado exitosamente.")
        except FileNotFoundError:
            print("Archivo de inventario no encontrado. Creando uno nuevo.")
            self.guardar_inventario()  # Crea un archivo vacío si no existe
        except json.JSONDecodeError:
            print("Error al decodificar el archivo JSON. El archivo podría estar vacío o corrupto.")
            self.inventario = {}  # Inicializa el inventario como vacío

    def guardar_inventario(self):
        try:
            with open(self.archivo, 'w') as file:
                json.dump(self.inventario, file, indent=4)
            print("Inventario guardado exitosamente.")
        except PermissionError:
            print("Error: No tienes permiso para escribir en el archivo.")

    def agregar_producto(self, nombre, cantidad):
        if nombre in self.inventario:
            self.inventario[nombre] += cantidad
        else:
            self.inventario[nombre] = cantidad
        self.guardar_inventario()
        print(f"Producto '{nombre}' agregado exitosamente.")

    def actualizar_producto(self, nombre, cantidad):
        if nombre in self.inventario:
            self.inventario[nombre] = cantidad
            self.guardar_inventario()
            print(f"Producto '{nombre}' actualizado exitosamente.")
        else:
            print(f"Error: Producto '{nombre}' no encontrado.")

    def eliminar_producto(self, nombre):
        if nombre in self.inventario:
            del self.inventario[nombre]
            self.guardar_inventario()
            print(f"Producto '{nombre}' eliminado exitosamente.")
        else:
            print(f"Error: Producto '{nombre}' no encontrado.")

    def mostrar_inventario(self):
        if self.inventario:
            print("Inventario:")
            for nombre, cantidad in self.inventario.items():
                print(f"- {nombre}: {cantidad}")
        else:
            print("El inventario está vacío.")

def main():

        inventario = Inventario()

        while True:
            print("\nOpciones:")
            print("1. Agregar producto")
            print("2. Actualizar producto")
            print("3. Eliminar producto")
            print("4. Mostrar inventario")
            print("5. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                nombre = input("Nombre del producto: ")
                cantidad = int(input("Cantidad: "))
                inventario.agregar_producto(nombre, cantidad)
            elif opcion == '2':
                nombre = input("Nombre del producto: ")
                cantidad = int(input("Nueva cantidad: "))
                inventario.actualizar_producto(nombre, cantidad)
            elif opcion == '3':
                nombre = input("Nombre del producto: ")
                inventario.eliminar_producto(nombre)
            elif opcion == '4':
                inventario.mostrar_inventario()
            elif opcion == '5':
                break
            else:
                print("Opción no válida.")

if __name__ == "__main__":
        main()