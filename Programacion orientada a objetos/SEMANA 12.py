# Clase Libro
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.titulo} por {self.autor} (Categoría: {self.categoria}, ISBN: {self.isbn})"

# Clase Usuario
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.id_usuario})"

# Clase Biblioteca
class Biblioteca:
    def __init__(self):
        self.libros_disponibles = {}  # ISBN -> Libro
        self.usuarios_registrados = set()  # IDs únicos de usuarios
        self.historial_prestamos = {}  # Usuario -> Libros prestados

    # Añadir un libro a la biblioteca
    def agregar_libro(self, libro):
        if libro.isbn not in self.libros_disponibles:
            self.libros_disponibles[libro.isbn] = libro
            print(f"Libro agregado: {libro}")
        else:
            print("El libro ya está en la biblioteca.")

    # Quitar un libro de la biblioteca
    def quitar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            del self.libros_disponibles[isbn]
            print(f"Libro con ISBN {isbn} eliminado.")
        else:
            print("El libro no está en la biblioteca.")

    # Registrar un usuario
    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.usuarios_registrados:
            self.usuarios_registrados.add(usuario.id_usuario)
            self.historial_prestamos[usuario] = []
            print(f"Usuario registrado: {usuario}")
        else:
            print("El usuario ya está registrado.")

    # Dar de baja a un usuario
    def dar_baja_usuario(self, id_usuario):
        for usuario in list(self.historial_prestamos.keys()):
            if usuario.id_usuario == id_usuario:
                self.usuarios_registrados.remove(id_usuario)
                del self.historial_prestamos[usuario]
                print(f"Usuario con ID {id_usuario} dado de baja.")
                return
        print("Usuario no encontrado.")

    # Prestar un libro
    def prestar_libro(self, id_usuario, isbn):
        for usuario in self.historial_prestamos.keys():
            if usuario.id_usuario == id_usuario:
                if isbn in self.libros_disponibles:
                    libro = self.libros_disponibles.pop(isbn)
                    usuario.libros_prestados.append(libro)
                    print(f"Libro prestado: {libro}")
                else:
                    print("El libro no está disponible.")
                return
        print("Usuario no registrado.")

    # Devolver un libro
    def devolver_libro(self, id_usuario, isbn):
        for usuario in self.historial_prestamos.keys():
            if usuario.id_usuario == id_usuario:
                for libro in usuario.libros_prestados:
                    if libro.isbn == isbn:
                        usuario.libros_prestados.remove(libro)
                        self.libros_disponibles[isbn] = libro
                        print(f"Libro devuelto: {libro}")
                        return
                print("El usuario no tiene ese libro.")
                return
        print("Usuario no registrado.")

    # Buscar libros
    def buscar_libros(self, criterio, valor):
        resultados = [libro for libro in self.libros_disponibles.values() if getattr(libro, criterio, None) == valor]
        print("Resultados de la búsqueda:")
        for libro in resultados:
            print(libro)

    # Listar libros prestados por un usuario
    def listar_libros_prestados(self, id_usuario):
        for usuario in self.historial_prestamos.keys():
            if usuario.id_usuario == id_usuario:
                print(f"Libros prestados por {usuario.nombre}:")
                for libro in usuario.libros_prestados:
                    print(libro)
                return
        print("Usuario no registrado.")

# Ejemplo de uso
libro1 = Libro("1984", "George Orwell", "Ficción", "1234567890")
libro2 = Libro("El Principito", "Antoine de Saint-Exupéry", "Clásico", "0987654321")

usuario1 = Usuario("Juan", "U001")

biblioteca = Biblioteca()

# Operaciones
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.registrar_usuario(usuario1)
biblioteca.prestar_libro("U001", "1234567890")
biblioteca.listar_libros_prestados("U001")
biblioteca.devolver_libro("U001", "1234567890")
