import numpy as np
import matplotlib.pyplot as plt
import random


class Ruleta():
        
    def __init__(self, nMax = 36):
        self.ganadores = [] 
        self.nroMaximo = nMax

    # gira la ruleta nVeces y guarda los resultado
    def girarRuleta(self, nVeces):
        i=1
        while i < n:
            numero = np.random.randint(0,nMax)
            self.ganadores.append(numero)
            i += 1

    def graficarFrecuenciaRelativa(self):
        #por lo que entiendo es graficar cuantas veces salio un número hasta la tirada X
        x = np.linspace(0, 2, 100)
        frecuencia = ganadores[0:x].count(ganador)
        y = frecuencia / x

 
    def graficarMedia(self):
        x = np.linspace(0, 2, 100)
        y = numpy.mean(self.ganadores[0:x]) # calcula la media hasta el ganador X de la ruleta

        fig, ax = plt.subplots()  # Crea una figura y ejes
        ax.plot(x, y)  # Plotear datos en los ejes
        ax.set_xlabel('# jugadas')  # Titulo eje x
        ax.set_ylabel('Media')  # Titulo eje y
        ax.set_title("Media en funcion de cantidad de tiros")  # Titulo
        ax.legend()  # Add a legend
        plt.show() 


    def graficarVarianza(self):
        i=0

    def graficarDesvio(self):
        self.graficarMedia()
        
    ## list seria la lista q obtenemos de GIRARRULETA()
    # yo decia ir guardando esas listas dentro de la clase (en un array, ganadores o el nombre que pinte)

    def getGraficos():
        self.graficarMedia()
        #...
     # que haga todos los graficos y los muestre








