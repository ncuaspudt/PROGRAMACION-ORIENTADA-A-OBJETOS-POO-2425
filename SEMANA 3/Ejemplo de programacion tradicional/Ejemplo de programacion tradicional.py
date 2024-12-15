#Programacion tradicional
#la programación se estructuraba principalmente de manera procedural, centrándose en la ejecución secuencial de .
#Calculo promedio semanal del clima de ciudad 1, Ciudad 2, Ciudad 3

# Definición de variables globales: temperaturas de cada ciudad para 7 días
temperatures_city1 = [18.0, 20.0, 22.0, 19.0, 21.0, 23.0, 20.0]  # Ciudad 1
temperatures_city2 = [15.0, 17.5, 16.0, 18.0, 19.5, 17.0, 18.5]  # Ciudad 2
temperatures_city3 = [25.0, 27.0, 26.5, 28.0, 29.0, 30.0, 28.5]  # Ciudad 3

# Variables globales para almacenar los promedios
average_city1 = 0
average_city2 = 0
average_city3 = 0


# Función para calcular el promedio de temperaturas de una ciudad
def calculate_average(city_temperatures, city_number):
    global average_city1, average_city2, average_city3

    total_temperature = sum(city_temperatures)  # Suma de todas las temperaturas
    average = total_temperature / len(city_temperatures)  # Promedio de las temperaturas

    # Asignar el promedio a la ciudad correspondiente
    if city_number == 1:
        average_city1 = average
    elif city_number == 2:
        average_city2 = average
    elif city_number == 3:
        average_city3 = average


# Función para mostrar los promedios de temperaturas por ciudad
def display_results():
    calculate_average(temperatures_city1, 1)
    calculate_average(temperatures_city2, 2)
    calculate_average(temperatures_city3, 3)

    # Mostrar los promedios
    print(f"Promedio de temperaturas en Ciudad 1: {average_city1:.2f}°C")
    print(f"Promedio de temperaturas en Ciudad 2: {average_city2:.2f}°C")
    print(f"Promedio de temperaturas en Ciudad 3: {average_city3:.2f}°C")


# Uso de las funciones en la programación tradicional
display_results()  # Llamamos a la función para mostrar los resultados
