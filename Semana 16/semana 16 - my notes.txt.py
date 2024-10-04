# Escritura de Archivo de Texto

# Abre o crea un archivo llamado 'my_notes.txt' en modo escritura ('w').
# Si el archivo ya existe, se sobrescribirá el contenido anterior.
with open('my_notes.txt', 'w') as file:
    # Escribe tres líneas de notas personales en el archivo
    file.write("Primera nota: Estudiar Python todos los días.\n")
    file.write("Segunda nota: Practicar la escritura de código.\n")
    file.write("Tercera nota: Revisar ejemplos y documentación.\n")
# El archivo se cierra automáticamente al salir del bloque 'with'

# Lectura de Archivo de Texto

# Abre el archivo 'my_notes.txt' en modo lectura ('r').
with open('my_notes.txt', 'r') as file:
    # Lee el contenido del archivo línea por línea utilizando readline()
    line = file.readline()

    # Itera a través de cada línea y la imprime en la consola
    while line:
        print(line.strip())  # strip() elimina los saltos de línea adicionales
        line = file.readline()  # Lee la siguiente línea

# Al salir del bloque 'with', el archivo se cierra automáticamente

print("¡Hemos terminado de leer y escribir en el archivo!")
