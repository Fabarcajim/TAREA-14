import pyodbc
import pandas as pd

from tkinter import *  #Importamos todas las funciones que contiene tkinter

#Creamos el objeto que será la raiz de la aplicación
raiz = Tk()
#Le agregamos un título
raiz.title("Filtrando Información")
#Determinamos si se podrá cambiar su tamaño
raiz.resizable(1,1)
#Asignamos un logotipo
raiz.iconbitmap('objetos.ico')

#Asignamos un tipo de cursor, un color de background y un borde a la raiz
raiz.config(cursor="circle")
raiz.config(bd=8)
raiz.config(relief="ridge")

Id_num = StringVar()
nombre = StringVar()
genero = StringVar()
ciudad = StringVar()
correo = StringVar()
estado_civil = StringVar()


Label(raiz, text="Id_num").pack()
Entry(raiz, justify="center", textvariable=Id_num, width=10).pack()

Label(raiz, text="Nombre").pack()
Entry(raiz, justify="center", textvariable=nombre, state="disabled", width=15).pack() # primer numero

Label(raiz, text="Género").pack()
Entry(raiz, justify="center", textvariable=genero, state="disabled", width=5).pack()

Label(raiz, text="Ciudad").pack()
Entry(raiz, justify="center", textvariable=ciudad, state="disabled", width=20).pack()

Label(raiz, text="Correo").pack()
Entry(raiz, justify="center", textvariable=correo, state="disabled", width=30).pack()

Label(raiz, text="Estado Civil").pack()
Entry(raiz, justify="center", textvariable=estado_civil, state="disabled", width=10).pack()

Label(raiz, text="").pack()

def buscar():

	server = 'FERABARCA'
	bd = 'DB_Python'

	try:
			conexion = pyodbc.connect(driver='{SQL server}', host = server, database = bd)
			print('Conexión exitosa')
	except:
		   print('La conexión no fué exitosa')

	#Creamos un cursor para almacenar la información en memoria
	cursor = conexion.cursor()
	cursor.execute("SELECT * FROM Datos_Personales_Python WHERE Id_num= " + Id_num.get())

	datos_cliente = cursor.fetchall()

	#Recorremos el array datos_cliente
	for cliente in datos_cliente:
		nombre.set(cliente[1])
		genero.set(cliente[6])
		ciudad.set(cliente[4])
		correo.set(cliente[2])
		estado_civil.set(cliente[7])

	conexion.commit()

	#Nos aseguramos de cerrar la conexión
	conexion.close()


def borrar():
	Id_num.set("")
	nombre.set("")
	genero.set("")
	ciudad.set("")
	correo.set("")
	estado_civil.set("")

#Creamos los botones
#Con command le decimos cual función queremos que lleve a cabo
Button(raiz, text="Buscar", command=buscar).pack(side="left")
Button(raiz, text="Borrar", command=borrar).pack(side="left")
raiz.mainloop()