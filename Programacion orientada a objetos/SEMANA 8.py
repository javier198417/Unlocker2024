import os

def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
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
        '1': 'Unidad 1/1.5. Estadistica/1.2.5.1 Ejemplo de Estadistica.py',
        '2': 'Unidad 1/2.5. Calculo de probabilidades para la distribucion normal /2.5-1. Ejemplo Calculo de probabilidades .py',
        '3': 'Unidad 1/3.5. Tablas estadisticas /2.3-1. Ejemplo de tablas estadisticas .py',
        # Agrega aquí el resto de las rutas de los scripts
    }

    while True:
        print("\n********Dashboard*************")
        # Imprime las opciones del menú
        for key in opciones:
            print(f"{key} - {opciones[key]}")
        print("9 - Salir")

        eleccion = input("Elige un script para ver su código o '9' para salir: ")
        if eleccion == '9':
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