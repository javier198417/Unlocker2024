import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import Calendar

# Función para agregar un evento
def agregar_evento():
    fecha = calendar.get_date()
    hora = entry_hora.get()
    descripcion = entry_descripcion.get()
    if not (fecha and hora and descripcion):
        messagebox.showerror("Error", "Todos los campos son obligatorios")
        return
    tree.insert("", tk.END, values=(fecha, hora, descripcion))
    limpiar_campos()

# Función para eliminar un evento seleccionado
def eliminar_evento():
    seleccionado = tree.selection()
    if not seleccionado:
        messagebox.showerror("Error", "Selecciona un evento para eliminar")
        return
    respuesta = messagebox.askyesno("Confirmación", "¿Estás seguro de eliminar el evento?")
    if respuesta:
        for item in seleccionado:
            tree.delete(item)

# Función para limpiar campos de entrada
def limpiar_campos():
    entry_hora.delete(0, tk.END)
    entry_descripcion.delete(0, tk.END)

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Agenda Personal")

# Frame para la lista de eventos
frame_lista = ttk.Frame(ventana)
frame_lista.pack(pady=10)
tree = ttk.Treeview(frame_lista, columns=("Fecha", "Hora", "Descripción"), show="headings")
tree.heading("Fecha", text="Fecha")
tree.heading("Hora", text="Hora")
tree.heading("Descripción", text="Descripción")
tree.pack()

# Frame para entrada de datos
frame_entrada = ttk.Frame(ventana)
frame_entrada.pack(pady=10)

ttk.Label(frame_entrada, text="Fecha:").grid(row=0, column=0, padx=5, pady=5)
calendar = Calendar(frame_entrada, date_pattern="yyyy-mm-dd")
calendar.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(frame_entrada, text="Hora:").grid(row=1, column=0, padx=5, pady=5)
entry_hora = ttk.Entry(frame_entrada)
entry_hora.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(frame_entrada, text="Descripción:").grid(row=2, column=0, padx=5, pady=5)
entry_descripcion = ttk.Entry(frame_entrada)
entry_descripcion.grid(row=2, column=1, padx=5, pady=5)

# Frame para botones
frame_botones = ttk.Frame(ventana)
frame_botones.pack(pady=10)
ttk.Button(frame_botones, text="Agregar Evento", command=agregar_evento).grid(row=0, column=0, padx=5)
ttk.Button(frame_botones, text="Eliminar Evento Seleccionado", command=eliminar_evento).grid(row=0, column=1, padx=5)
ttk.Button(frame_botones, text="Salir", command=ventana.quit).grid(row=0, column=2, padx=5)

ventana.mainloop()
