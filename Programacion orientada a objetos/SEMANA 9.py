class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        """Constructor de la clase Producto"""
        self.id_producto = id_producto  # ID único del producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Getters
    def get_id(self):
        return self.id_producto

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    # Setters
    def set_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad

    def set_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    def __str__(self):
        """Devuelve una representación en texto del producto"""
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"

class Inventario:
    def __init__(self):
        """Inicializa un inventario vacío"""
        self.productos = []

    def agregar_producto(self, id_producto, nombre, cantidad, precio):
        """Añade un producto si el ID es único"""
        for producto in self.productos:
            if producto.get_id() == id_producto:
                print("❌ Error: El ID ya existe en el inventario.")
                return
        nuevo_producto = Producto(id_producto, nombre, cantidad, precio)
        self.productos.append(nuevo_producto)
        print("✅ Producto agregado con éxito.")

    def eliminar_producto(self, id_producto):
        """Elimina un producto por ID"""
        for producto in self.productos:
            if producto.get_id() == id_producto:
                self.productos.remove(producto)
                print("✅ Producto eliminado correctamente.")
                return
        print("❌ Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        """Actualiza la cantidad o el precio de un producto"""
        for producto in self.productos:
            if producto.get_id() == id_producto:
                if nueva_cantidad is not None:
                    producto.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    producto.set_precio(nuevo_precio)
                print("✅ Producto actualizado correctamente.")
                return
        print("❌ Error: Producto no encontrado.")

    def buscar_producto(self, nombre):
        """Busca productos por nombre"""
        resultados = [producto for producto in self.productos if nombre.lower() in producto.get_nombre().lower()]
        if resultados:
            print("\n🔍 Productos encontrados:")
            for producto in resultados:
                print(producto)
        else:
            print("❌ No se encontraron productos con ese nombre.")

    def mostrar_productos(self):
        """Muestra todos los productos"""
        if not self.productos:
            print("📭 El inventario está vacío.")
        else:
            print("\n📦 Productos en el inventario:")
            for producto in self.productos:
                print(producto)



def menu():
    inventario = Inventario()

    while True:
        print("\n📌 MENÚ DE GESTIÓN DE INVENTARIO 📌")
        print("1️⃣ Agregar producto")
        print("2️⃣ Eliminar producto")
        print("3️⃣ Actualizar producto")
        print("4️⃣ Buscar producto por nombre")
        print("5️⃣ Mostrar todos los productos")
        print("6️⃣ Salir")

        opcion = input("🔹 Selecciona una opción: ")

        if opcion == "1":
            id_producto = input("🔹 ID del producto: ")
            nombre = input("🔹 Nombre del producto: ")
            cantidad = int(input("🔹 Cantidad: "))
            precio = float(input("🔹 Precio: "))
            inventario.agregar_producto(id_producto, nombre, cantidad, precio)

        elif opcion == "2":
            id_producto = input("🔹 ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("🔹 ID del producto a actualizar: ")
            nueva_cantidad = input("🔹 Nueva cantidad (dejar en blanco para no cambiar): ")
            nuevo_precio = input("🔹 Nuevo precio (dejar en blanco para no cambiar): ")

            nueva_cantidad = int(nueva_cantidad) if nueva_cantidad else None
            nuevo_precio = float(nuevo_precio) if nuevo_precio else None

            inventario.actualizar_producto(id_producto, nueva_cantidad, nuevo_precio)

        elif opcion == "4":
            nombre = input("🔹 Nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == "5":
            inventario.mostrar_productos()

        elif opcion == "6":
            print("👋 ¡Gracias por usar el sistema de inventario!")
            break

        else:
            print("❌ Opción inválida. Inténtalo de nuevo.")

if __name__ == "__main__":
    menu()
