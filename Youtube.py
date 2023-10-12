from pytube import YouTube
from tkinter import *

def accion():
    enlace = videos.get()
    video = YouTube(enlace)
    descargar = video.streams.get_highest_resolution()
    descargar.download()

root = Tk()
root.config(bd=15)
root.title("Descargar videos de YouTube")

instrucciones = Label(root, text="Programa desarrollado en Python para descargar videos de YouTube")
instrucciones.grid(row=0, column=0, columnspan=2)

videos = Entry(root)
videos.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

imagen = PhotoImage(file="Youtube_logo.png")
foto = Label(root, image=imagen, bd=0)
foto.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

boton = Button(root, text="Descargar", command=accion)
boton.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

menubar = Menu(root)
root.config(menu=menubar)

menubar.add_command(label="Salir", command=root.destroy)

root.mainloop()