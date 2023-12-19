from logging import exception
import math
from tkinter import *
from tkinter import ttk

from sqlalchemy import Index




class Window():
    def __init__(self, window):
        self.gui = window
        self.gui.title('Hola Mundo')
        self.frame = ttk.Frame(self.gui)
        self.frame.grid(row=1, column=0)
        ttk.Button(self.frame, text='Calculadora de Ecuaciones\nForma: ax + b = c', command= lambda:  self.template(self.ecPrimerGWind)).grid(row=1, column=0, columnspan=2, sticky=W + E, pady=10, padx=10)
        ttk.Button(self.frame, text='Calculadora de Ecuaciones\nForma: ax + b = c', command= lambda:  self.template(self.ecSegundoGWind)).grid(row=1, column=2, columnspan=2, sticky=E+W, pady=10, padx=10)


    def template(self, func):
        self.c = Tk()
        func(self.c)
        self.c.mainloop()
        

    def ecPrimerGWind(self, wind):
        from modules.operations import ecPG
        window = wind
        window.title('Hola')

        frame = ttk.Frame(window)
        frame.grid(row=0, column=0)

        # Labels y Inputs
        ttk.Label(frame, text='Calcula Ecuaciones de Primer Grado').grid(row = 1, column = 1, columnspan=5, padx=10, pady=10, sticky=W+E)
        
        a = ttk.Entry(frame)
        a.grid(row=3, column=1)
        ttk.Label(frame, text='x + ').grid(row=3,column=2) 
        b = ttk.Entry(frame)
        b.grid(row=3, column=3)
        ttk.Label(frame, text=' = ').grid(row=3, column=4)
        c = ttk.Entry(frame)
        c.grid(row=3, column=5)

        ttk.Button(frame, text='Calcular', command = lambda: calcular(a,b,c)).grid(row=4, column=2, columnspan=2, sticky=W+E, padx=10, pady=10)


        resultado = Label(frame)
        resultado.grid(row=4, column=5, columnspan= 3,sticky=W+E, padx=10, pady=10)

        def calcular(a,b,c):
            a = float(int(a.get()))
            b = float(int(b.get()))
            c  = float(int(c.get()))
            resultados = ecPG(a, b, c)
            res = f'{resultados[0]}\n{resultados[1]}\n{resultados[2]}\n\nX = {resultados[3]}'
            
            resultado['text'] = res

    def ecSegundoGWind(self, wind):
        from modules.operations import ecSG

        window = wind
        window.title('Ecuaciones de Segundo Grado')

        frame = ttk.Frame(window)
        frame.grid(row=0, column=0)

        # Labels y Inputs
        ttk.Label(frame, text='Calcula Ecuaciones de Segundo Grado').grid(row = 1, column = 1, columnspan=5, padx=10, pady=10, sticky=W+E)
        
        a = ttk.Entry(frame)
        a.grid(row=3, column=1)
        ttk.Label(frame, text='x² + ').grid(row=3,column=2) 
        b = ttk.Entry(frame)
        b.grid(row=3, column=3)
        ttk.Label(frame, text='x + ').grid(row=3, column=4)
        c = ttk.Entry(frame)
        c.grid(row=3, column=5)
        ttk.Label(frame, text=' = 0').grid(row=3,column=6)

        ttk.Button(frame, text='Calcular', command = lambda: calcular(a,b,c)).grid(row=4, column=2, columnspan=2, sticky=W+E, padx=10, pady=10)


        resultado = Label(frame)
        resultado.grid(row=4, column=5, columnspan= 3,sticky=W+E, padx=10, pady=10)

        def calcular(a,b,c):
            a = float(int(a.get()))
            b = float(int(b.get()))
            c  = float(int(c.get()))
            resultados = ecSG(a,b,c)
            if len(resultados) == '':
                print('No se pudo XD')
                return  


            
            print(resultados, len(resultados))
        

    


if __name__ == '__main__':
    root = Tk()
    Calculadora = Window(root)
    root.mainloop()
