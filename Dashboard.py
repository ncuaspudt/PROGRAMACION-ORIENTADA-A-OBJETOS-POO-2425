
# Mi proyecto con tareas del Bloque I
import os

def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r', encoding='utf-8') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")



def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

    opciones = {
        '1': 'SEMANA 2/Abstraccion/1.2.1. Abstraccion_Ejemplo.py',
        '2': 'SEMANA 2/Encapsulación/Encapsulación_Ejemplo.py',
        '3': 'SEMANA 2/Herencia/Herencia_Ejemplo.py',
        '4': 'SEMANA 2/Polimorfismo/Polimorfismo_Ejemplo.py',
        '5': 'SEMANA 3/Ejemplo de POO/Ejemplo de programacion orientada a objetos.py',
        '6': 'SEMANA 3/Ejemplo de programacion tradicional/Ejemplo de programacion tradicional.py',
        '7': 'SEMANA 4/EjemplosMundoReal_POO.py',
        '8': 'SEMANA 5/Semana 5_Tipos de datos identificadores.py',
        '9': 'SEMANA 6/Programa_clases_objetos_herencia_encapsulación_polimorfismo..py',
        '10': 'SEMANA 7/Uso de Constructores y Destructores.py',





        #  Rutas de los scripts
    }

    while True:
        print("\n********Menu Principal - Dashboard*************")
        # Imprime las opciones del menú
        for key in opciones:
            print(f"{key} - {opciones[key]}")
        print("0 - Salir")

        eleccion = input("Elige un script para ver su código o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            # Asegura que el path sea absoluto
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()