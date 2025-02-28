import json

# Clase Producto
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def obtener_id(self):
        return self.id_producto

    def obtener_nombre(self):
        return self.nombre

    def obtener_cantidad(self):
        return self.cantidad

    def obtener_precio(self):
        return self.precio

    def establecer_cantidad(self, cantidad):
        self.cantidad = cantidad

    def establecer_precio(self, precio):
        self.precio = precio

    def to_dict(self):
        return {
            'id': self.id_producto,
            'nombre': self.nombre,
            'cantidad': self.cantidad,
            'precio': self.precio
        }

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

    class Inventario:
        def __init__(self, archivo='inventario.json'):
            self.archivo = archivo
            self.productos = {}
            self.cargar_inventario()

        # Cargar inventario desde el archivo
        def cargar_inventario(self):
            try:
                with open(self.archivo, 'r') as file:
                    productos_serializados = json.load(file)
                    for producto_data in productos_serializados.values():
                        producto = Producto(
                            producto_data['id'],
                            producto_data['nombre'],
                            producto_data['cantidad'],
                            producto_data['precio']
                        )
                        self.productos[producto.obtener_id()] = producto
            except FileNotFoundError:
                print(f"Archivo {self.archivo} no encontrado, creando uno nuevo.")
            except json.JSONDecodeError:
                print(f"Error al decodificar el archivo {self.archivo}, creando uno nuevo.")
            except Exception as e:
                print(f"Se produjo un error al cargar el inventario: {e}")

        # Guardar inventario al archivo
        def guardar_inventario(self):
            try:
                with open(self.archivo, 'w') as file:
                    productos_serializados = {id_producto: producto.to_dict() for id_producto, producto in
                                              self.productos.items()}
                    json.dump(productos_serializados, file, indent=4)
                print("Inventario guardado exitosamente.")
            except PermissionError:
                print(f"Error de permisos al intentar guardar el archivo {self.archivo}.")
            except Exception as e:
                print(f"Se produjo un error al guardar el inventario: {e}")

        # Metodo agregar producto
        def agregar_producto(self, producto):
            if producto.obtener_id() in self.productos:
                print("Error: Producto con ese ID ya existe.")
            else:
                self.productos[producto.obtener_id()] = producto
                self.guardar_inventario()  # Guardar cambios en el archivo
                print(f"Producto {producto.obtener_nombre()} agregado correctamente.")

        # Metodo eliminar producto
        def eliminar_producto(self, id_producto):
            if id_producto in self.productos:
                del self.productos[id_producto]
                self.guardar_inventario()  # Guardar cambios en el archivo
                print(f"Producto con ID {id_producto} eliminado.")
            else:
                print("Error: Producto no encontrado.")

        # Metodo actualizar producto
        def actualizar_producto(self, id_producto, cantidad=None, precio=None):
            if id_producto in self.productos:
                producto = self.productos[id_producto]
                if cantidad is not None:
                    producto.establecer_cantidad(cantidad)
                if precio is not None:
                    producto.establecer_precio(precio)
                self.guardar_inventario()  # Guardar cambios en el archivo
                print(f"Producto con ID {id_producto} actualizado.")
            else:
                print("Error: Producto no encontrado.")

        # Metodo buscar producto
        def buscar_producto(self, nombre):
            found = False
            for producto in self.productos.values():
                if nombre.lower() in producto.obtener_nombre().lower():
                    print(producto)
                    found = True
            if not found:
                print("No se encontró ningún producto con ese nombre.")

        # Metodo mostrar inventario
        def mostrar_inventario(self):
            if not self.productos:
                print("Inventario vacío.")
            else:
                for producto in self.productos.values():
                    print(producto)
def menu():
    inventario = Inventario()  # Al crear el inventario, se cargan los productos desde el archivo

    while True:
        print("\n1. Agregar Producto")
        print("2. Eliminar Producto")
        print("3. Actualizar Producto")
        print("4. Buscar Producto")
        print("5. Mostrar Inventario")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '6':
            break
        elif opcion == '1':
            # Agregar producto
            id_producto = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad: "))
            precio = float(input("Ingrese el precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)
        elif opcion == '2':
            # Eliminar producto
            id_producto = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)
        elif opcion == '3':
            # Actualizar producto
            id_producto = input("Ingrese el ID del producto a actualizar: ")
            cantidad = input("Ingrese la nueva cantidad (deje en blanco para no cambiar): ")
            precio = input("Ingrese el nuevo precio (deje en blanco para no cambiar): ")

            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None

            inventario.actualizar_producto(id_producto, cantidad, precio)
        elif opcion == '4':
            # Buscar producto
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)
        elif opcion == '5':
            # Mostrar inventario
            inventario.mostrar_inventario()
        else:
            print("Opción inválida, intente de nuevo.")

# Punto de entrada principal
if __name__ == "__main__":
    menu()