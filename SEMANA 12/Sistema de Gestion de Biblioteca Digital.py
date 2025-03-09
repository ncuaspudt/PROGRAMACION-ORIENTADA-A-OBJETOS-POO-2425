# Utilizaremos las clases Libro, Usuario, Biblioteca con atributos y metodos correspondientes.

import json

# Clase Libro
class Libro:
    def __init__(self, isbn, titulo, autor, categoria, prestado=False):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.prestado = prestado
        self.historial_prestamos = []  # Historial de usuarios que han prestado el libro

    def to_dict(self):
        return {
            "isbn": self.isbn,
            "titulo": self.titulo,
            "autor": self.autor,
            "categoria": self.categoria,
            "prestado": self.prestado
        }

# Clase Usuario
class Usuario:
    def __init__(self, id_usuario, nombre):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.libros_prestados = []  # Lista para almacenar libros prestados
# Metodo prestar libro
    def prestar_libro(self, libro):
        if libro.prestado:
            print(f"El libro {libro.titulo} ya está prestado.")
        else:
            self.libros_prestados.append(libro)
            libro.prestado = True
            libro.historial_prestamos.append(self.nombre)  # Guardamos al usuario en el historial del libro
            print(f"El libro {libro.titulo} ha sido prestado a {self.nombre}.")
# Metodo devolver libro
    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)
            libro.prestado = False
            print(f"El libro {libro.titulo} ha sido devuelto por {self.nombre}.")
        else:
            print(f"El libro {libro.titulo} no está en los libros prestados a {self.nombre}.")
# Metodos mostrar libros prestados
    def mostrar_libros_prestados(self):
        if not self.libros_prestados:
            print(f"{self.nombre} no tiene libros prestados.")
        else:
            print(f"Libros prestados a {self.nombre}:")
            for libro in self.libros_prestados:
                print(f"- {libro.titulo}")
# Metodo mostrar historial prestamo
    def mostrar_historial_prestamos(self):
        print(f"Historial de préstamos de {self.nombre}:")
        for libro in self.libros_prestados:
            print(f"- {libro.titulo} (Historial de préstamos: {libro.historial_prestamos})")

# Clase Biblioteca
class Biblioteca:
    def __init__(self, archivo_json='biblioteca.json', archivo_usuarios='usuarios.json'):
        self.archivo_json = archivo_json
        self.archivo_usuarios = archivo_usuarios
        self.libros = self.cargar_libros()
        self.usuarios = self.cargar_usuarios()
#Metodo cargar libros
    def cargar_libros(self):
        try:
            with open(self.archivo_json, 'r') as archivo:
                datos_libros = json.load(archivo)
                return {isbn: Libro(**datos) for isbn, datos in datos_libros.items()}
        except FileNotFoundError:
            return {}
# Metodo guardar libros
    def guardar_libros(self):
        with open(self.archivo_json, 'w') as archivo:
            json.dump({isbn: libro.to_dict() for isbn, libro in self.libros.items()}, archivo, indent=4)
# Metodo cargar usuarios
    def cargar_usuarios(self):
        try:
            with open(self.archivo_usuarios, 'r') as archivo:
                return json.load(archivo)
        except FileNotFoundError:
            return {}
# Metodo guardar usuarios
    def guardar_usuarios(self):
        with open(self.archivo_usuarios, 'w') as archivo:
            json.dump(self.usuarios, archivo, indent=4)
# Metodo añadir libro
    def añadir_libro(self, libro):
        self.libros[libro.isbn] = libro
        self.guardar_libros()
# Metodo registrar usuario
    def registrar_usuario(self, id_usuario, nombre):
        if id_usuario in self.usuarios:
            print(f"El usuario con ID {id_usuario} ya está registrado.")
        else:
            self.usuarios[id_usuario] = {'nombre': nombre, 'libros_prestados': []}
            self.guardar_usuarios()
            print(f"Usuario {nombre} registrado exitosamente.")
# Metodo dar de baja a usuario
    def dar_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            self.guardar_usuarios()
            print(f"Usuario con ID {id_usuario} dado de baja.")
        else:
            print(f"El usuario con ID {id_usuario} no existe.")
# Metodo prestar libro
    def prestar_libro(self, isbn, id_usuario):
        libro = self.libros.get(isbn)
        if libro:
            usuario_data = self.usuarios.get(id_usuario)
            if usuario_data:
                usuario = Usuario(id_usuario, usuario_data['nombre'])
                usuario.prestar_libro(libro)
                self.usuarios[id_usuario]['libros_prestados'].append(libro.isbn)
                self.guardar_usuarios()
                self.guardar_libros()
            else:
                print(f"Usuario con ID {id_usuario} no encontrado.")
        else:
            print(f"Libro con ISBN {isbn} no disponible.")
# Metodo devolver libro
    def devolver_libro(self, isbn, id_usuario):
        libro = self.libros.get(isbn)
        if libro:
            usuario_data = self.usuarios.get(id_usuario)
            if usuario_data and isbn in usuario_data['libros_prestados']:
                usuario = Usuario(id_usuario, usuario_data['nombre'])
                usuario.devolver_libro(libro)
                self.usuarios[id_usuario]['libros_prestados'].remove(isbn)
                self.guardar_usuarios()
                self.guardar_libros()
            else:
                print(f"Usuario con ID {id_usuario} no tiene este libro prestado.")
        else:
            print(f"Libro con ISBN {isbn} no disponible.")
# Metodo mostrar libros
    def mostrar_libros(self):
        for libro in self.libros.values():
            estado = "Prestado" if libro.prestado else "Disponible"
            print(f"{libro.isbn}: {libro.titulo} por {libro.autor} - {estado}")

# Menú de interacción
def menu():
    biblioteca = Biblioteca()
    while True:
        print("\n1. Añadir Libro\n2. Mostrar Libros\n3. Registrar Usuario\n4. Dar Baja Usuario\n5. Prestar Libro\n6. Devolver Libro\n7. Listar Libros Prestados de Usuario\n8. Mostrar Historial de Préstamos\n9. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            isbn = input("ISBN: ")
            titulo = input("Título: ")
            autor = input("Autor: ")
            categoria = input("Categoría: ")
            libro = Libro(isbn, titulo, autor, categoria)
            biblioteca.añadir_libro(libro)
        elif opcion == '2':
            biblioteca.mostrar_libros()
        elif opcion == '3':
            id_usuario = input("ID del usuario: ")
            nombre = input("Nombre del usuario: ")
            biblioteca.registrar_usuario(id_usuario, nombre)
        elif opcion == '4':
            id_usuario = input("ID del usuario a dar de baja: ")
            biblioteca.dar_baja_usuario(id_usuario)
        elif opcion == '5':
            isbn = input("ISBN del libro a prestar: ")
            id_usuario = input("ID del usuario que lo pedirá prestado: ")
            biblioteca.prestar_libro(isbn, id_usuario)
        elif opcion == '6':
            isbn = input("ISBN del libro a devolver: ")
            id_usuario = input("ID del usuario que lo devolverá: ")
            biblioteca.devolver_libro(isbn, id_usuario)
        elif opcion == '7':
            id_usuario = input("ID del usuario: ")
            if id_usuario in biblioteca.usuarios:
                print(f"Libros prestados a {biblioteca.usuarios[id_usuario]['nombre']}:")
                for isbn in biblioteca.usuarios[id_usuario]['libros_prestados']:
                    print(f"- {isbn}")
            else:
                print("Usuario no encontrado.")
        elif opcion == '8':
            id_usuario = input("ID del usuario: ")
            if id_usuario in biblioteca.usuarios:
                usuario_data = biblioteca.usuarios[id_usuario]
                usuario = Usuario(id_usuario, usuario_data['nombre'])
                usuario.mostrar_historial_prestamos()
            else:
                print("Usuario no encontrado.")
        elif opcion == '9':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
