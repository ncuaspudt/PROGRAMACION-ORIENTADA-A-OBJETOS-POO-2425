# Desarrollar una Aplicación GUI para Gestión de Tareas con Atajos de Teclado, Interfaz grafica, Manejo de eventos, atajos de teclado.

import tkinter as tk
from tkinter import messagebox


# Función para agregar una tarea
def añadir_tarea(event=None):
    tarea = entrada.get().strip()
    if tarea:
        lista.insert(tk.END, tarea)
        entrada.delete(0, tk.END)  # Limpiar la entrada después de agregar


# Función para marcar una tarea como completada
def tarea_completada():
    tarea_seleccionada = lista.curselection()
    if tarea_seleccionada:  # Verificamos que haya una tarea seleccionada
        tarea = lista.get(tarea_seleccionada)  # Obtenemos la tarea
        # Modificar la tarea para mostrarla como completada (agregar ✔ y cambiar color)
        lista.delete(tarea_seleccionada)  # Eliminar la tarea seleccionada
        lista.insert(tarea_seleccionada[0], f"✔ {tarea}")  # Insertamos la tarea con el símbolo ✔
        lista.itemconfig(tarea_seleccionada[0], {'fg': 'red', 'bg': 'lightgreen'})  # Cambiar color de texto y fondo

# Función para eliminar la tarea seleccionada
def eliminar_tarea():
    tarea_seleccionada = lista.curselection()
    if tarea_seleccionada:  # Verificamos que haya una tarea seleccionada
        lista.delete(tarea_seleccionada)  # Eliminar tarea
    else:
        messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para eliminar.")


# Función para cerrar la aplicación
def cerrar_app(event=None):
    root.quit()


# Creación de la ventana principal
root = tk.Tk()
root.title('Aplicación GUI de Lista de Tareas')
root.geometry('600x550')

# Cambiar el color de fondo de la ventana principal
root.configure(bg="beige")


# Etiqueta para el título
label_titulo = tk.Label(root, text="Gestión de Tareas", font=("KOBA", 20), fg="red", bg="white")
label_titulo.pack(pady=10)

# Etiqueta para la entrada de texto
label_entrada = tk.Label(root, text="Agregar una nueva tarea:")
label_entrada.pack(pady=5)

# Entrada de texto
entrada = tk.Entry(root)
entrada.pack(pady=20)
entrada.bind("<Return>", añadir_tarea)  # Permitir agregar tarea presionando Enter

# Lista de tareas visual
lista = tk.Listbox(root, height=15, width=40)
lista.pack(pady=20)

# Frame para los botones
frame_botones = tk.Frame(root)
frame_botones.pack(pady=10)

# Botón para agregar tarea
boton_añadir = tk.Button(frame_botones, text='AÑADIR', background="grey", command=añadir_tarea)
boton_añadir.pack(side=tk.LEFT, padx=10)

# Botón para eliminar tarea
boton_eliminar = tk.Button(frame_botones, text='ELIMINAR', background="grey", command=eliminar_tarea)
boton_eliminar.pack(side=tk.LEFT, padx=10)

# Botón para marcar tarea como completada
boton_completada = tk.Button(frame_botones, text='TAREA COMPLETADA', background="grey", command=tarea_completada)
boton_completada.pack(side=tk.LEFT, padx=10)
# Botón para marcar tarea como completada
boton_salir = tk.Button(frame_botones, text='SALIR', background="grey", command=cerrar_app)
boton_salir.pack(side=tk.LEFT, padx=10)

# Asignar atajos de teclado
root.bind("<Return>", añadir_tarea)  # Enter para añadir tarea
root.bind("<Delete>", lambda event: eliminar_tarea())  # Delete para eliminar tarea
root.bind("<d>", lambda event: eliminar_tarea())  # D para eliminar tarea
root.bind("<c>", lambda event: tarea_completada())  # C para marcar como completada
root.bind("<Escape>", lambda event: cerrar_app())  # Escape para cerrar la aplicación

# Ejecutar la aplicación
root.mainloop()
