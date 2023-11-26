import pyodbc
import pandas as pd
import tkinter as tk

from tkinter import *
from tkinter import ttk #Importamos todas las funciones que contiene tkinter
from tkinter.ttk import *
from tkinter import messagebox

class General:
	def __init__(self, raiz):
		self.genero = StringVar()
		self.label_genero = Label(raiz, text = "Género")
		self.label_genero.grid(column=0, row=0)
		self.genero = Combobox(raiz, values=('F', 'M'), width=5)
		self.genero.grid(column=0, row=1)

		self.estado = StringVar()
		self.label_estado = Label(raiz, text = "Estado Civil")
		self.label_estado.grid(column=0, row=5)
		self.estado = Spinbox(raiz, values=("Married", "Single", "Divorced", "Widow", "NULL"), width=10)
		self.estado.grid(column=0,row=6)

		#Creamos los botones
		#Con command le decimos cual función queremos que lleve a cabo
		self.boton_buscar= Button(raiz, text="Buscar", command=self.buscar)
		self.boton_buscar.grid(column=0, row=20)

		self.boton_borrar=Button(raiz, text="Borrar", command=self.borrar)
		self.boton_borrar.grid(column=0, row=30)

		#Tabla
		self.tabla=ttk.Treeview(raiz, column=("c1", "c2", "c3"), show='headings', height=8)
		self.tabla.column("# 1",anchor=CENTER, stretch=NO, width=100)
		self.tabla.heading("# 1", text="Nombre")
		self.tabla.column("# 2", anchor=CENTER, stretch=NO)
		self.tabla.heading("# 2", text="Género")
		self.tabla.column("# 3", anchor=CENTER, stretch=NO)
		self.tabla.heading("# 3", text="Estado Civil")
		self.tabla.grid(column=0, row=40)

	def buscar(self):
		server = 'FERABARCA'
		bd = 'DB_Python'
		genero_valor = "'" + self.genero.get() + "'"
		print(genero_valor)

		estado = "'" + self.estado.get() + "'"
		print(estado)

		try:
				conexion = pyodbc.connect(driver='{SQL server}', host = server, database = bd)
				print('Conexión exitosa')
		except:
				print('La conexión no fué exitosa')

		#Creamos un cursor para almacenar la información en memoria
		cursor = conexion.cursor()

		cursor.execute("SELECT Nombre, Genero, Estado_Civil FROM Datos_Personales_Python WHERE genero= " + genero_valor + "AND Estado_Civil = " + estado)

		datos_clientes = cursor.fetchall()
		print(datos_clientes)
		conexion.commit()


		#Nos aseguramos de cerrar la conexión
		conexion.close()

		messagebox.showinfo("Resultados", datos_clientes)

	#def desplegar_resultados(self):

	def borrar(self):
		self.genero.set("")
		self.estado.set("")





#Creamos el objeto que será la raiz de la aplicación
raiz = Tk()
#Le agregamos un título
raiz.title("Filtrando Información")
#Determinamos si se podrá cambiar su tamaño
raiz.resizable(1,1)
#Asignamos un logotipo
raiz.iconbitmap('objetos.ico')
#Asignamos un tipo de cursor, un color de background y un borde a la raiz
raiz.config(bd=8)
raiz.config(relief="ridge")
estructura = General(raiz)

raiz.mainloop()