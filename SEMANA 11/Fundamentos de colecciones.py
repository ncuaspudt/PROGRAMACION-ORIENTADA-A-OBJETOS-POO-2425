# Clase

import json
import os

# Clase Producto
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Métodos para actualizar el precio y la cantidad de un producto
    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    def actualizar_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad

    # Metodo para convertir un producto a diccionario, facilitando la serialización
    def to_dict(self):
        return {"id_producto": self.id_producto, "nombre": self.nombre, "cantidad": self.cantidad,
                "precio": self.precio}

    # Metodo para representar el producto como cadena
    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

# Clase Inventario
class Inventario:
    def __init__(self, archivo="inventario.json"):
        self.archivo = archivo
        self.productos = {}
        self.cargar_inventario()  # Al iniciar, se carga el inventario desde el archivo

    # Cargar inventario desde el archivo
    def cargar_inventario(self):
        if not os.path.exists(self.archivo):  # Verifica si el archivo no existe
            print(f"Archivo {self.archivo} no encontrado, creando uno nuevo.")
            self.crear_archivo_vacio()  # Si no existe, crea un archivo vacío
        else:
            try:
                with open(self.archivo, 'r') as file:
                    data = json.load(file)
                    self.productos = {int(k): Producto(**v) for k, v in data.items()}
            except json.JSONDecodeError:
                print(f"Error al decodificar el archivo {self.archivo}, creando uno nuevo.")
                self.crear_archivo_vacio()  # Si no se puede decodificar, crea un archivo vacío
            except Exception as e:
                print(f"Se produjo un error al cargar el inventario: {e}")

    # Metodo para crear un archivo vacío de JSON
    def crear_archivo_vacio(self):
        try:
            with open(self.archivo, 'w') as file:
                json.dump({}, file, indent=4)
            print(f"Archivo {self.archivo} creado correctamente.")
        except Exception as e:
            print(f"Se produjo un error al crear el archivo: {e}")

    # Guardar inventario al archivo
    def guardar_inventario(self):
        try:
            with open(self.archivo, 'w') as file:
                json.dump({k: v.to_dict() for k, v in self.productos.items()}, file, indent=4)
            print("Inventario guardado exitosamente.")
        except PermissionError:
            print(f"Error de permisos al intentar guardar el archivo {self.archivo}.")
        except Exception as e:
            print(f"Se produjo un error al guardar el inventario: {e}")

    # Metodo agregar producto
    def agregar_producto(self, producto):
        if producto.id_producto in self.productos:
            print("Error: Producto con ese ID ya existe.")
        else:
            self.productos[producto.id_producto] = producto
            self.guardar_inventario()  # Guardar cambios en el archivo
            print("Producto agregado correctamente.")

    # Metodo eliminar producto
    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_inventario()  # Guardar cambios en el archivo
            print("Producto eliminado.")
        else:
            print("Error: Producto no encontrado.")

    # Metodo actualizar precio
    def actualizar_precio(self, id_producto, nuevo_precio):
        if id_producto in self.productos:
            self.productos[id_producto].actualizar_precio(nuevo_precio)
            self.guardar_inventario()  # Guardar cambios en el archivo
            print("Precio actualizado correctamente.")
        else:
            print("Error: Producto no encontrado.")

    # Metodo actualizar cantidad
    def actualizar_cantidad(self, id_producto, nueva_cantidad):
        if id_producto in self.productos:
            self.productos[id_producto].actualizar_cantidad(nueva_cantidad)
            self.guardar_inventario()  # Guardar cambios en el archivo
            print("Cantidad actualizada correctamente.")
        else:
            print("Error: Producto no encontrado.")

    # Buscar producto por nombre (no importa mayúsculas o minúsculas)
    def buscar_producto_nombre(self, nombre):
        resultado = [p for p in self.productos.values() if p.nombre.lower() == nombre.lower()]
        return resultado if resultado else "Producto no encontrado."

    # Metodo mostrar inventario
    def mostrar_inventario(self):
        if self.productos:
            for producto in self.productos.values():
                print(producto)
        else:
            print("El inventario está vacío.")

# Menú interactivo
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
            id_producto = int(input("Ingrese el ID del producto: "))
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad: "))
            precio = float(input("Ingrese el precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)
        elif opcion == '2':
            # Eliminar producto
            id_producto = int(input("Ingrese el ID del producto a eliminar: "))
            inventario.eliminar_producto(id_producto)
        elif opcion == '3':
            # Actualizar producto
            id_producto = int(input("Ingrese el ID del producto a actualizar: "))
            cantidad = input("Ingrese la nueva cantidad (deje en blanco para no cambiar): ")
            precio = input("Ingrese el nuevo precio (deje en blanco para no cambiar): ")

            if cantidad:  # Solo actualizar si el usuario ingresa un valor
                cantidad = int(cantidad)
                inventario.actualizar_cantidad(id_producto, cantidad)
            if precio:
                precio = float(precio)
                inventario.actualizar_precio(id_producto, precio)
        elif opcion == '4':
            # Buscar producto
            nombre = input("Ingrese el nombre del producto a buscar: ")
            resultado = inventario.buscar_producto_nombre(nombre)
            if isinstance(resultado, list):
                for p in resultado:
                    print(p)
            else:
                print(resultado)
        elif opcion == '5':
            # Mostrar inventario
            inventario.mostrar_inventario()
        else:
            print("Opción inválida, intente de nuevo.")

# Punto de entrada principal
if __name__ == "__main__":
    menu()