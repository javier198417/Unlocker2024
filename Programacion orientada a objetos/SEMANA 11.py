
class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_cantidad(self):
        return self.cantidad

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def get_precio(self):
        return self.precio

    def set_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"

class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        self.productos[producto.get_id()] = producto

    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]

    def actualizar_cantidad(self, id, cantidad):
        if id in self.productos:
            self.productos[id].set_cantidad(cantidad)

    def actualizar_precio(self, id, precio):
        if id in self.productos:
            self.productos[id].set_precio(precio)

    def buscar_producto_por_nombre(self, nombre):
        resultados = []
        for producto in self.productos.values():
            if nombre.lower() in producto.get_nombre().lower():
                resultados.append(producto)
        return resultados

    def mostrar_inventario(self):
        for producto in self.productos.values():
            print(producto)

    def guardar_inventario(self, archivo):
        datos = {id: producto.__dict__ for id, producto in self.productos.items()}
        with open(archivo, 'w') as f:
            json.dump(datos, f, indent=4)

    def cargar_inventario(self, archivo):
        try:
            with open(archivo, 'r') as f:
                datos = json.load(f)
                for id, datos_producto in datos.items():
                    producto = Producto(**datos_producto)
                    self.productos[int(id)] = producto
        except FileNotFoundError:
            print("Archivo de inventario no encontrado. Se creará uno nuevo.")

def menu():
    inventario = Inventario()
    inventario.cargar_inventario("inventario.json")

    while True:
        print("\n--- Menú de Inventario ---")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar cantidad")
        print("4. Actualizar precio")
        print("5. Buscar producto por nombre")
        print("6. Mostrar inventario")
        print("7. Guardar inventario")
        print("8. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            id = int(input("ID: "))
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.agregar_producto(producto)
        elif opcion == '2':
            id = int(input("ID del producto a eliminar: "))
            inventario.eliminar_producto(id)
        elif opcion == '3':
            id = int(input("ID del producto a actualizar: "))
            cantidad = int(input("Nueva cantidad: "))
            inventario.actualizar_cantidad(id, cantidad)
        elif opcion == '4':
            id = int(input("ID del producto a actualizar: "))
            precio = float(input("Nuevo precio: "))
            inventario.actualizar_precio(id, precio)
        elif opcion == '5':
            nombre = input("Nombre del producto a buscar: ")
            resultados = inventario.buscar_producto_por_nombre(nombre)
            for producto in resultados:
                print(producto)
        elif opcion == '6':
            inventario.mostrar_inventario()
        elif opcion == '7':
            inventario.guardar_inventario("inventario.json")
            print("Inventario guardado.")
        elif opcion == '8':
            inventario.guardar_inventario("inventario.json")
            print("Inventario guardado. ¡Hasta luego!")
            break
        else:
            print("Opción inválida.")
if __name__ == "__main__":
    menu()