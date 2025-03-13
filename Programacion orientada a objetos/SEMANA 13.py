import tkinter as tk
from tkinter import messagebox

# Función para agregar texto a la lista
def agregar_texto():
    texto = campo_texto.get()
    if texto.strip():  # Verifica que no esté vacío
        lista.insert(tk.END, texto)
        campo_texto.delete(0, tk.END)  # Limpia el campo de texto
    else:
        messagebox.showwarning("Advertencia", "El campo de texto está vacío.")

# Función para limpiar la lista
def limpiar_lista():
    lista.delete(0, tk.END)  # Elimina todos los elementos de la lista

# Ventana principal
ventana = tk.Tk()
ventana.title("Gestor de Datos Básico")

# Etiqueta
etiqueta = tk.Label(ventana, text="Ingrese un dato:")
etiqueta.pack(pady=5)

# Campo de texto
campo_texto = tk.Entry(ventana, width=30)
campo_texto.pack(pady=5)

# Botón "Agregar"
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_texto)
boton_agregar.pack(pady=5)

# Lista para mostrar datos
lista = tk.Listbox(ventana, width=50, height=10)
lista.pack(pady=10)

# Botón "Limpiar"
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_lista)
boton_limpiar.pack(pady=5)

# Inicia el bucle principal de la aplicación
ventana.mainloop()