from tkinter import *

raiz=Tk() #raiz para la interfaz
raiz.title("Ventana de pruebas")
raiz.resizable(False, False) #(ancho, alto) Determina un False(0) para redimensionar
#raiz.iconbitmap("icon.ico")
raiz.geometry("650x350")
raiz.config(bg="gray")
raiz.mainloop() #Bucle infinito para estar recargando raiz
