import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import StringVar
import sqlite3
import webbrowser
import dbcontroller

class program:

    def __init__(self, window):

        self.wind = window
        self.wind.title('Roads')

        #creating frame
        frame = LabelFrame(self.wind, text = 'Rutas')
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)

        ttk.Button(frame,text = 'Agregar nueva ruta',command = self.add_rute).grid(row = 2, column = 0)
        ttk.Button(frame,text = 'Eliminar ruta').grid(row = 2, column = 1)

        Label(frame, text = 'Name: ').grid(row = 1, column = 0)
        self.name = Entry(frame)
        self.name.grid(row = 1, column = 1)

        #Combobox comienzo
        self.box_value = StringVar()
        self.box = ttk.Combobox(self.wind, textvariable=self.box_value, state='readonly')
        self.box['values'] = self.obtener_combobox()
        self.box.current(0)
        self.box.grid(row = 3, columnspan = 2)

       
        #Combobox destino
        self.box_value2 = StringVar()
        self.box = ttk.Combobox(self.wind, textvariable=self.box_value2, state='readonly')
        self.box['values'] = self.obtener_combobox()
        self.box.current(0)
        self.box.grid(row = 3,column = 4, columnspan = 2)

        ttk.Button(text = 'Ver ruta', command = self.ver_ruta).grid(row = 5, column = 0)
        ttk.Button(text = 'modificar ruta').grid(row = 5, column = 1)

    
    def run_query(self, query, parameters = ()):
        with sqlite3.connect('database.db') as conn:
            c = conn.cursor()
            result = c.execute(query, parameters)
            conn.commit()
        return result
 
    def obtener_combobox(self):
        query = 'SELECT name FROM places ORDER BY name DESC'
        db_rows = self.run_query(query)
        
        valores = []

        for row in db_rows:
            valores.append(row[0])

        return tuple(valores)

    def ver_ruta(self):
        var = self.box_value.get()
        var2 = self.box_value2.get()


        var = var.replace(" ","+")
        var2 = var.replace(" ","+")

        cadena = "https://www.google.com.mx/maps/dir/"+var+"/"+var2

        
        webbrowser.open(cadena, new=2, autoraise=True)
    
    def validation(self):
        return len(self.name.get()) != 0 
    
    def add_rute(self):
        if self.validation():
            query = 'INSERT INTO places VALUES(NULL, ?)'
            parameters = (self.name.get(),)
            self.run_query(query, parameters)
            self.get_products()
            print('data saved')
        

  
    

if __name__ == '__main__':
    window = Tk()
    application = program(window)
    window.mainloop()

        