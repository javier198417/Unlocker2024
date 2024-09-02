# Definimos las dimensiones de la matriz
ciudades = ["Ciudad1", "Ciudad2", "Ciudad3"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semanas = 4

# Inicializamos la matriz 3D con valores de ejemplo
import random
temperaturas = [[[random.uniform(15, 35) for _ in dias] for _ in range(semanas)] for _ in ciudades]

# Calculamos el promedio de temperaturas para cada ciudad por semana
promedios = []

for i, ciudad in enumerate(ciudades):
    promedios_ciudad = []
    for semana in range(semanas):
        suma_temperaturas = sum(temperaturas[i][semana])
        promedio_semana = suma_temperaturas / len(dias)
        promedios_ciudad.append(promedio_semana)
    promedios.append(promedios_ciudad)

# Mostramos los promedios de temperaturas para cada ciudad y semana
for i, ciudad in enumerate(ciudades):
    print(f"Promedios de temperaturas para {ciudad}:")
    for semana in range(semanas):
        print(f"  Semana {semana + 1}: {promedios[i][semana]:.2f}°C")