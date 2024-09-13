def calcular_temperatura_promedio(datos_temperaturas):
    """
    Calcula la temperatura promedio de cada ciudad.

    :param datos_temperaturas: Diccionario con los nombres de las ciudades como claves y listas de temperaturas semanales como valores.
    :return: Diccionario con los nombres de las ciudades como claves y sus temperaturas promedio como valores.
    """
    promedios = {}
    for ciudad, temperaturas in datos_temperaturas.items():
        promedio = sum(temperaturas) / len(temperaturas)
        promedios[ciudad] = promedio
    return promedios

# Ejemplo de uso
datos_temperaturas = {
    "Ciudad1": [30, 32, 31, 29],
    "Ciudad2": [25, 26, 27, 28],
    "Ciudad3": [20, 21, 19, 22]
}

promedios = calcular_temperatura_promedio(datos_temperaturas)
for ciudad, promedio in promedios.items():
    print(f"La temperatura promedio en {ciudad} es {promedio:.2f}°C")