import os
import time
import zipfile
from urllib.request import urlretrieve  # Import más específico
from datetime import datetime  # Import para obtener la hora y la fecha actuales

# Función para banner animado
def banner_animado(texto):
    for letra in texto:
        print(letra, end='', flush=True)
        time.sleep(0.1)
    print("\n")

# Función para mostrar el banner de ALDAZUNLOCK con Android en verde
def display_banner():
    # Obtener la hora y la fecha actuales
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")

    print("\033[1;31m")
    print("       ╲ ▁▂▂▂▁ ╱            \033[0;32m" + current_time + "\033[1;31m")
    print("       ▄███████▄")
    print("      ███ \033[0;32mANDROID\033[1;31m ███")
    print("     ▄███████████▄     \033[1;31m\033[47m ALDAZUNLOCK \033[00m - \033[1;33mversión 1.0\033[1;31m")
    print("  ▄█ ▄▄▄▄▄▄▄▄▄▄▄▄▄ █▄  \033[00m\033[2;37m--------------------------\033[00m\033[1;31m")
    print("  ██ █████████████ ██  \033[00muna herramienta para explotar Android\033[1;31m")
    print("  ██ ██ \033[0;32mANDROID\033[1;31m ██ ██  \033[00musando adb y fastboot.\033[1;31m")
    print("  ██ █████████████ ██  \033[00mcodificado por \033[1;31m@ALDAZUNLOCK\033[1;31m")
    print("  ██ █████████████ ██")
    print("     █████████████")
    print("      ███████████")
    print("       ██     ██")
    print("       ██     ██")
    print("\033[00m")

# Descarga y configuración de platform-tools si no están presentes
def configurar_platform_tools():
    if not os.path.exists("platform-tools"):
        print("Descargando Android Platform Tools...")
        url = 'https://dl.google.com/android/repository/platform-tools-latest-windows.zip'
        try:
            urlretrieve(url, 'platform-tools.zip')
            print("Descomprimiendo Platform Tools...")
            with zipfile.ZipFile('platform-tools.zip', 'r') as zip_ref:
                zip_ref.extractall('.')
            os.remove('platform-tools.zip')
            print("Platform Tools descargado y descomprimido correctamente.")
        except Exception as e:  # Capturar errores de descarga o descompresión
            print(f"Error: {e}")
            print("Descarga o descompresión fallida. Verifique su conexión a internet.")

# Menú principal
def mostrar_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    display_banner()
    banner_animado("ALDAZUNLOCK")
    print("================================")
    print("    ALDAZUNLOCK TOOL FASTBOOT  ")
    print("================================")
    print("[1] Flash AP (boot, recovery, system, etc.)")
    print("[2] Flash BP (radio, modem, fsg, etc.)")
    print("[3] Flash BL (bootloader)")
    print("[4] Flash imagen de recovery")
    print("[5] Flashear firmware completo (con Factory Reset)")
    print("[6] Flashear firmware completo (sin Factory Reset)")
    print("[7] Borrar Baseband (modemst, nvdata, etc.)")
    print("[8] Convertir XML a BAT")
    print("[a] Opciones de Reinicio")
    print("[9] Quitar Protección FRP de Google")
    print("[b] Factory Reset (Borrar Datos + Cache)")
    print("[0] Obtener información del dispositivo")
    print("[C] AUTOINSTALL CUSTOM ROM")
    print("[x] Salir")
    print("================================")
    return input("Selecciona una opción: ")

# Ejecutar comandos shell con manejo de errores
def ejecutar_comando(comando):
    try:
        result = os.system(comando)
        if result != 0:  # Comprobar código de salida no cero (error)
            print(f"Error: Comando '{comando}' falló.")
    except OSError as e:
        print(f"Error: {e}")

# Función para autoinstalar ROM personalizada (pendiente de implementación)
def autoinstall_custom_rom():
    print("Función para autoinstalar Custom ROM (pendiente de implementación)")

# Programa principal
def main():
    configurar_platform_tools()
    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            ejecutar_comando("fastboot flash boot boot.img")
        elif opcion == "2":
            ejecutar_comando("fastboot flash radio radio.img")
        # ... lógica similar para otras opciones ...
        elif opcion.lower() == "c":
            autoinstall_custom_rom()  # Llamada a función placeholder
        elif opcion.lower() == "x":
            print("Saliendo...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    main()
