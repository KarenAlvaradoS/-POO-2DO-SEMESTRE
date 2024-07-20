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

def ejecutar_script(ruta_script):
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Ejecutando {ruta_script} ---\n")
            exec(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al ejecutar el archivo: {e}")

def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

    # Opciones del menú con rutas relativas a los scripts
    opciones = {
        '1': 'Unidad 1/PROGRAMACIÓN TRADICIONAL.py',
        '2': 'Unidad 1/Programación Orientada a Objetos (POO).py',
        '3': 'Unidad 1/Programación Orientada a Objetos (POO).py',
        '4': 'Unidad 2/TAREA_SEMANA_6.py'
    }

    while True:
        print("\nMenu Principal - Dashboard")
        # Imprime las opciones del menú
        for key in opciones:
            print(f"{key} - {opciones[key]}")
        print("0 - Salir")

        eleccion = input("Elige un script para ver su código o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            print("\n1 - Ver código")
            print("2 - Ejecutar script")
            sub_eleccion = input("Elige una acción: ")
            if sub_eleccion == '1':
                mostrar_codigo(ruta_script)
            elif sub_eleccion == '2':
                ejecutar_script(ruta_script)
            else:
                print("Opción no válida. Por favor, intenta de nuevo.")
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()
