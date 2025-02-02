import threading
import time

def contador(nombre, maximo):
    for i in range(1, maximo + 1):
        print(f"{nombre}: {i}")
        time.sleep(1)  # Simula trabajo

if __name__ == "__main__":
    hilo1 = threading.Thread(target=contador, args=("Hilo 1", 5))
    hilo2 = threading.Thread(target=contador, args=("Hilo 2", 10))

    hilo1.start()
    hilo2.start()

    hilo1.join()  # Espera a que el hilo 1 termine
    hilo2.join()  # Espera a que el hilo 2 termine

    print("¡Tarea completada!")