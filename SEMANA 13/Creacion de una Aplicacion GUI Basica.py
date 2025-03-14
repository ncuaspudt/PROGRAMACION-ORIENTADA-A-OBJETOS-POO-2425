# Aplicación GUI basica, utilizacion de etiquetas (labels), botones, campos de texto y una lista para mostrar datos.
# importamos la libreria tkinter, que permitira crear una interfaz gráfica.
import tkinter
import tkinter as aplicacion

def agregar_dato():
    dato = entrada.get().strip()
    if dato:
        lista.insert(tkinter.END, dato)

# Funcion que permite eliminar el ultimo elemento de la lista
def delet():
    lista.delete(tkinter.END)

#Configuracion de la ventana
root = tkinter.Tk()
root.title('Tienda Digital Cosméticos')
root.geometry('400x450')

# Etiqueta para el título
label_titulo = tkinter.Label(root, text="Maquillaje y cosmética", font=("KOBA", 16), fg="purple", bg="white")
label_titulo.pack(pady=10)

# Etiqueta para la entrada de texto
label_entrada = tkinter.Label(root, text="Agregar un nuevo producto:")
label_entrada.pack(pady=5)

#Entrada de texto
entrada = tkinter.Entry(root)
entrada.pack(pady=20)

#Agregar boton
boton = tkinter.Button(root, text='AGREGAR',background="sky blue", command=agregar_dato)
boton.pack(pady=15)
boton = tkinter.Button(root, text='LIMPIAR',background="sky blue", command=delet)
boton.pack(pady=15)

#Lista
lista = aplicacion.Listbox(root)
lista.pack(pady=20)




root.mainloop()



