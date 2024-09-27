# Crear un Diccionario con información ficticia
informacion_personal = {
    "nombre": "Aroon Lhesster",
    "edad": 32,
    "ciudad": "Canada",
    "profesion": "Ingeniero"
}

# Acceder y modificar el valor de la clave "ciudad"
informacion_personal["ciudad"] = "Alaska"

# Agregar una nueva clave-valor para la profesión de la persona
# (Aunque ya está la clave "profesion", la tarea lo menciona así que vamos a cambiar el valor por otro)
informacion_personal["profesion"] = "Desarrollador de software"

# Verificar si la clave "telefono" existe, si no, agregarla con un número ficticio
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "123-456-789"

# Eliminar la clave "edad"
informacion_personal.pop("edad")

# Imprimir el diccionario final
print("Diccionario final:")
print(informacion_personal)
