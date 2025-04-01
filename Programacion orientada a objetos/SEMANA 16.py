import tkinter as tk

class GestorTareas:
    def __init__(self, ventana):
        self.ventana = ventana
        ventana.title("Gestor de Tareas")

        self.tareas = []

        self.entrada_tarea = tk.Entry(ventana, width=40)
        self.entrada_tarea.pack(pady=10)

        self.lista_tareas = tk.Listbox(ventana, width=50)
        self.lista_tareas.pack(pady=10)

        self.boton_anadir = tk.Button(ventana, text="Añadir", command=self.anadir_tarea)
        self.boton_anadir.pack(side=tk.LEFT, padx=5)

        self.boton_completar = tk.Button(ventana, text="Completar", command=self.completar_tarea)
        self.boton_completar.pack(side=tk.LEFT, padx=5)

        self.boton_eliminar = tk.Button(ventana, text="Eliminar", command=self.eliminar_tarea)
        self.boton_eliminar.pack(side=tk.LEFT, padx=5)

        ventana.bind("<Return>", lambda event: self.anadir_tarea())
        ventana.bind("c", lambda event: self.completar_tarea())
        ventana.bind("<Delete>", lambda event: self.eliminar_tarea())
        ventana.bind("d", lambda event: self.eliminar_tarea())
        ventana.bind("<Escape>", lambda event: ventana.destroy())

    def anadir_tarea(self):
        tarea = self.entrada_tarea.get()
        if tarea:
            self.tareas.append({"tarea": tarea, "completada": False})
            self.actualizar_lista()
            self.entrada_tarea.delete(0, tk.END)

    def completar_tarea(self):
        seleccion = self.lista_tareas.curselection()
        if seleccion:
            indice = seleccion[0]
            self.tareas[indice]["completada"] = True
            self.actualizar_lista()

    def eliminar_tarea(self):
        seleccion = self.lista_tareas.curselection()
        if seleccion:
            indice = seleccion[0]
            del self.tareas[indice]
            self.actualizar_lista()

    def actualizar_lista(self):
        self.lista_tareas.delete(0, tk.END)
        for tarea in self.tareas:
            estado = "[Completada]" if tarea["completada"] else "[Pendiente]"
            self.lista_tareas.insert(tk.END, f"{estado} {tarea['tarea']}")

if __name__ == "__main__":
    ventana = tk.Tk()
    app = GestorTareas(ventana)
    ventana.mainloop()