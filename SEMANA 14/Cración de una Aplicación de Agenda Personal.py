# Creación de una Aplicación de Agenda Personal.
# Mediante el código ejecutado mostrara una ventana principal con una lista (TreeView) de eventos, se podra introducir fecha, hora y descripción del nuevo evento.

import tkinter as tk
from tkinter import ttk, messagebox


# Funciones
def agregar_evento():
    fecha = entry_fecha.get()
    hora = entry_hora.get()
    descripcion = entry_descripcion.get()

    if fecha and hora and descripcion:  # Asegurarse de que todos los campos estén completos
        tree.insert('', 'end', values=(fecha, hora, descripcion))
        # Limpiar las entradas después de agregar
        entry_fecha.delete(0, tk.END)
        entry_hora.delete(0, tk.END)
        entry_descripcion.delete(0, tk.END)


def eliminar_evento():
    # Verificar si se ha seleccionado un evento
    selected_item = tree.selection()
    if selected_item:
        confirm = messagebox.askyesno("Confirmación", "¿Estás seguro de eliminar este evento?")
        if confirm:
            tree.delete(selected_item)



def salir():
    root.quit()  # Cerrar la aplicación


# Creación de la ventana principal
root = tk.Tk()
root.title('Agenda Personal')
root.geometry('600x500')

# Crear la lista de eventos (Treeview)
tree = ttk.Treeview(root, columns=("Fecha", "Hora", "Descripción"), show="headings")
tree.heading('Fecha', text="Fecha")
tree.heading('Hora', text="Hora")
tree.heading('Descripción', text="Descripción")
tree.pack(pady=20, fill="both", expand=True)

# Crear un frame para los campos de entrada
frame_entry = tk.Frame(root)
frame_entry.pack(pady=10)

# labels y data entry (identificadores y cuadros de texto)
tk.Label(frame_entry, text="Fecha").grid(row=0, column=0)
entry_fecha = tk.Entry(frame_entry)  # Usar el DatePicker para seleccionar la fecha
entry_fecha.grid(row=0, column=1)

tk.Label(frame_entry, text="Hora").grid(row=1, column=0)
entry_hora = tk.Entry(frame_entry)
entry_hora.grid(row=1, column=1)

tk.Label(frame_entry, text="Descripción").grid(row=2, column=0)
entry_descripcion = tk.Entry(frame_entry)
entry_descripcion.grid(row=2, column=1)

# Crear un frame para los botones
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=20)

# Botones
btn_agregar = tk.Button(frame_buttons, text="Agregar Evento", command=agregar_evento, background="sky blue")
btn_agregar.grid(row=0, column=0, padx=5, pady=5)

btn_eliminar = tk.Button(frame_buttons, text="Eliminar Evento Seleccionado", command=eliminar_evento, background="sky blue")
btn_eliminar.grid(row=0, column=1, padx=5, pady=5)

btn_salir = tk.Button(frame_buttons, text="Salir", command=salir,background="sky blue")
btn_salir.grid(row=0, column=2, padx=5, pady=5)

# Iniciar la aplicación
root.mainloop()
