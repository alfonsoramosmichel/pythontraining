'''Agenda python
con SQLITE'''

# Importa módulos
from tkinter import *

#Variables
ancho = 560
alto = 540
pos_x = 400
pos_y = 400
ancho_alto = (str(ancho) + "x" + str(alto))
posicion_x = "+" + str(pos_x)
posicion_y = "+" + str(pos_y)
color_ventana = "blue"
color_fondo = "blue"
color_letra = "white"

# Función de prueba
def mostrar_mensaje():
    print("Pruebas")

# Ventana
ventana = Tk()
ventana.config(bg=color_ventana)
ventana.geometry(ancho_alto+posicion_x+posicion_y)
ventana.title("Agenda mia")

# Variables cajas
ID = IntVar()
nombre = StringVar()
apellidos = StringVar()
telefono = StringVar()
email = StringVar()

# Widgets
etiqueta_ID = Label(ventana,text="ID").place(x=50,y=50)
caja_ID = Entry(ventana,textvariable=ID).place(x=130, y=50)
etiqueta_nombre = Label(ventana, text="Nombre:").place(x=50,y=90)
caja_nombre = Entry(ventana,textvariable=nombre).place(x=130,y=90)
etiqueta_apellidos = Label(ventana,text="Apellidos:").place(x=50,y=130)
caja_apellidos = Entry(ventana,textvariable=apellidos).place(
