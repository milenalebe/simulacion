import numpy as np
import matplotlib.pyplot as plt
import random


class Ruleta():
        
    def __init__(self, nMax = 36):
        self.ganadores = [] 
        self.nroMaximo = nMax

    # gira la ruleta nVeces y guarda los resultado
    def girarRuleta(self, nVeces):
        numero = np.random.randint(0, self.nroMaximo, nVeces)
        self.ganadores.append(numero)

    def graficarFrecuenciaRelativa(self, nro):
        # Cantidad de veces que salio nro / total de tiradas, hasta la tirada X
        x = np.linspace(0, 2, 100)
        frecuencia = self.ganadores[0:x].count(nro)
        y = frecuencia / x
        self.crearGrafico(x,y)
 
    def graficarMedia(self):
        x = np.linspace(0, 2, 100)
        y = np.mean(self.ganadores[0:x]) # calcula la media hasta el ganador X de la ruleta

        fig, ax = plt.subplots()  # Crea una figura y ejes
        ax.plot(x, y)  # Plotear datos en los ejes
        ax.set_xlabel('# jugadas')  # Titulo eje x
        ax.set_ylabel('Media')  # Titulo eje y
        ax.set_title("Media en funcion de cantidad de tiros")  # Titulo
        ax.legend()  # Add a legend
        plt.show() 
        
    def graficarVarianza(self):
        self.graficarFrecuenciaRelativa()

    def graficarDesvio(self):
        self.graficarFrecuenciaRelativa()
        
    
     # crea todos los graficos pedidos
    def getGraficos(self):
        self.graficarFrecuenciaRelativa()

     def crearGrafico(x, y):
        fig, ax = plt.subplots()  # Crea una figura y ejes
        ax.plot(x, y)  # Plotear datos en los ejes
        ax.set_xlabel('# jugadas')  # Titulo eje x
        ax.set_ylabel('Media')  # Titulo eje y
        ax.set_title("Media en funcion de cantidad de tiros")  # Titulo
        ax.legend()  # Add a legend
        plt.show() 








