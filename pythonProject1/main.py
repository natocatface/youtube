from tkinter import *

from pytube import YouTube

def descargar_video():
    # Obtenemos la URL del video del campo de entrada
    url = url_entry.get()

    # Creamos una instancia de la clase YouTube con la URL
    yt = YouTube(url)

    # Obtenemos la resolución seleccionada en el menú desplegable
    resolucion = resolucion_var.get()

    # Descargamos el video con la resolución seleccionada
    stream = yt.streams.filter(res=resolucion).first()
    stream.download()

    # Mostramos un mensaje de descarga exitosa
    mensaje_label.config(text="El video se ha descargado exitosamente.")

# Creamos la ventana principal
ventana = Tk()
ventana.title("Descargador de videos de YouTube")

# Creamos un marco para la entrada de la URL
url_frame = Frame(ventana)
url_frame.pack(padx=10, pady=10)

# Creamos una etiqueta y un campo de entrada para la URL del video
url_label = Label(url_frame, text="URL del video:")
url_label.pack(side=LEFT)

url_entry = Entry(url_frame, width=50)
url_entry.pack(side=LEFT)

# Creamos un marco para la selección de la resolución
resolucion_frame = Frame(ventana)
resolucion_frame.pack(padx=10, pady=10)

# Creamos una etiqueta y un menú desplegable para la selección de la resolución
resolucion_label = Label(resolucion_frame, text="Resolución:")
resolucion_label.pack(side=LEFT)

resolucion_var = StringVar(resolucion_frame)
resolucion_var.set("")

resolucion_menu = OptionMenu(resolucion_frame, resolucion_var, "1080p", "720p", "480p", "360p")
resolucion_menu.pack(side=LEFT)

# Creamos un botón para iniciar la descarga
descargar_boton = Button(ventana, text="Descargar", command=descargar_video)
descargar_boton.pack(pady=10)

# Creamos una etiqueta para mostrar el mensaje de descarga exitosa
mensaje_label = Label(ventana, text="")
mensaje_label.pack(pady=10)

# Iniciamos el bucle de la ventana principal
ventana.mainloop()
