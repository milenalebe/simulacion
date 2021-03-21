import numpy as np
import matplotlib.pyplot as plt
import random


class Ruleta():
        
    def __init__(self, nMax = 36):
        self.ganadores = [] 
        self.nroMaximo = nMax

    def ganadoresArray(self):
        return np.array(self.ganadores)

    def firstGanadores(self,x):
        return np.array(self.ganadores[0:x])

    # genera n ganadores de la ruleta y los agrega a la lista de resultados
    def girar(self, n):
        tiradas = np.random.randint(0, self.nroMaximo+1, n)
        self.ganadores.extend(tiradas)

    # grafica la cantidad de veces que salio cada numero en la lista de resultados
    def graficarBarchartGanadores(self):
        fig = plt.figure()
        valores, cantidades = np.unique(self.ganadoresArray(), return_counts=True)
        bar = plt.bar(valores, cantidades) 
        plt.title("Jugadas totales: " + str(len(self.ganadores)))
        plt.show()

    # grafica la suma de los ganadores / total de tiradas en funcion de cantidad de tiradas
    # TODO: en realidad es graficar la cantidad de veces que sale un nro repecto del total de tiradas
    def graficarFrecuenciaRelativa(self, ):
        x = np.linspace(0, len(self.ganadores), len(self.ganadores))
        y = [sum(self.firstGanadores(x+1))/(x+1) for x in range(len(self.ganadores))]
        self.crearGrafico(x,y) 
 
    # grafica la media de los nros ganadores obtenidos en funcion de tiradas
    def graficarMedia(self):
        x = np.arange(len(self.ganadores))
        y = [np.mean(self.firstGanadores(x)) for x in range(len(self.ganadores))] 
        self.crearGrafico(x,y)


    #TODO: verificar que np.variance esta calculando bien
    def graficarVarianza(self):
        x = np.linspace(0, len(self.ganadores), len(self.ganadores))
        y = [np.variance(self.firstGanadores(x)) for x in range(len(self.ganadores))] 
        self.crearGrafico(x,y)

    #TODO: np.desvio??
    def graficarDesvio(self):
        x = np.linspace(0, len(self.ganadores), len(self.ganadores))
        y = [np.mean(self.firstGanadores(x)) for x in range (len(self.ganadores))] 
        self.crearGrafico(x,y)

    
     # crea todos los graficos pedidos
    def getGraficos(self):
    self.graficarBarchartGanadores()
    self.graficarFrecuenciaRelativa()
    self.graficarMedia()
    self.graficarVarianza()
    self.graficarDesvio()

    def crearGrafico(self, x, y):
        fig, ax = plt.subplots()  # Crea una figura y ejes
        ax.plot(x, y)  # Plotear datos en los ejes
        ax.set_xlabel('# jugadas')  # Titulo eje x
        ax.set_ylabel('Y LABEL')  # Titulo eje y
        ax.set_title("Titulo")  # Titulo
        ax.legend()  # Add a legend
        plt.show() 



ruleta = Ruleta()
ruleta.girar(200)
#ruleta.graficarBarchartGanadores()
ruleta.graficarFrecuenciaRelativa()
ruleta.graficarMedia()
ruleta.graficarVarianza()
ruleta.graficarDesvio()

