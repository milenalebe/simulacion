import numpy as np
import random

# esta clase recibe un numero y calcula sus atributos (color, paridad, etc)
class Numero():
    def __init__(self, n):
        self.valor = n
        self.par = self.calcularPar() #true si es par o false si es impar
        self.color = self.calcularColor() # "rojo" o "negro"
        self.fila = self.calcularFila() # 1, 2, o 3
        self.subconjunto = self.calcularSubconjunto() # 1,2 o 3 : 1er docena, 2da docena o 3ra docena

    def calcularColor(self):
        if(self.valor == 0):
            return None

        rojos = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]  # numeros usualmente rojos en las ruletas

        if self.valor in rojos:
            return "rojo"
        else:
            return "negro"


    def calcularPar(self):
        if(self.valor == 0):
            return None

        return ((self.valor%2) == 0) #true si es par y false si es impar
    
    def calcularFila(self):
        if(self.valor == 0):
            return None

        return (self.valor % 3) + 1 # fila 1, 2 o 3
    
    def calcularSubconjunto(self):
        if(self.valor == 0):
            return None

        return self.valor//12 # division por docenas, devuelven 1 hasta 12 2 hasta 24 y 3 los demas


class Ruleta():
    def __init__(self, nMax = 36):
        self.ganadores = [] 
        self.nroMaximo = nMax

    # genera n ganadores de la ruleta y los agrega a la lista de resultados
    def girar(self, n = 1):
        tiradas = np.random.randint(0, self.nroMaximo+1, n) # genera np.array de nros aleatorios
        self.ganadores.extend(tiradas) #convierte el arreglo a LISTA para que sea mas eficiente guardar y acceder

    # devuelve el ganador de la n-esima tirada
    def getNumeroGanador(self, n = -1): # por defecto se pasa -1 ya que devuelve el ultimo valor de la lista
        if(len(self.ganadores) == 1):
            return Numero(self.ganadores[0])

        if( n>0 and len(self.ganadores) > n) or (n<0 and len(self.ganadores) > -n):
            ganadorN = self.ganadores[n]
            return Numero(ganadorN)
        else:
            return None



class Apuesta():
    # Inicializa una apuesta, 
    # recibe listas de valores apostados (ya que puede apostar por ejemplo a varias filas o tanto a par como a impar)
    def __init__(self, nros = [],  pares = [], clrs =[], fi = [], sbcjs = [], cantidad = 100, desc = ""): 
        self.numeros = nros # lista de numeros apostados
        self.paridades = pares # lista que puede contener "par", "impar"
        self.colores = clrs # etc
        self.filas = fi 
        self.docenas = sbcjs
        self.cantidad = cantidad # por ahora, una cantidad unica apostada a cada uno de los valores elegidos
        self.desc = desc # breve descripcion de la estrategia empleada

# guarda su dinero, ganancia y perdida total, y se le pueden cargar distintas apuestas
class Jugador():
    def __init__(self, dineroInicial = 1000):
        self.dinero = dineroInicial
        self.ganancias = [] #guarda un historico de las ganancias
        self.perdidas = [] # idem de las perdidas
        self.apostado = []
        self.apuesta = None
        self.perdio = False

    def cargarApuesta(self, apuesta: Apuesta = Apuesta()):
        dineroApostado = 0

        # calcula cuanto dinero perdería con esa apuesta:
        dineroApostado += apuesta.cantidad * len(apuesta.numeros)
        dineroApostado += apuesta.cantidad * len(apuesta.paridades)
        dineroApostado += apuesta.cantidad * len(apuesta.colores)
        dineroApostado += apuesta.cantidad * len(apuesta.filas)
        dineroApostado += apuesta.cantidad * len(apuesta.docenas)

        self.apostado.append(dineroApostado) # histórico de dinero apostado
        self.apuesta = apuesta # guarda la apuesta actual
        print("Dinero apostado: ", dineroApostado)
        self.dinero -= dineroApostado


    # compara su apuesta actual con un numero ganador
    def calcularGanancias(self, ganador: Numero):
        gananciaJugada = 0

        # verifica si los valores ganadores se encuentran en alguna de las listas de valores apostados
        if(ganador.valor in self.apuesta.numeros):
            gananciaJugada += 36 * self.apuesta.cantidad 
        
        if(ganador.par in self.apuesta.paridades):
            gananciaJugada += self.apuesta.cantidad

        if(ganador.color in self.apuesta.colores):
            gananciaJugada += self.apuesta.cantidad
            
        if(ganador.subconjunto in self.apuesta.docenas):
            gananciaJugada += 3 * self.apuesta.cantidad

        if(ganador.fila in self.apuesta.filas):
            gananciaJugada += 3 * self.apuesta.cantidad

        self.dinero +=gananciaJugada
        
        perdidaJugada = self.apostado[-1] - gananciaJugada
        if(perdidaJugada < 0):
            perdidaJugada = 0 

        self.ganancias.append(gananciaJugada) # histórco de ganancias por jugada
        self.perdidas.append(perdidaJugada) # histórico de perdidas por jugada (si ganó mas dinero del que aspoto es 0)

        if self.dinero <= 0:
            self.perdio = True 

        print("ganancias: ", gananciaJugada)
        print("perdidas: ", perdidaJugada)

    def isPerdedor(self):
        return self.perdio # devuelve True si se quedo sin dinero

    

# controla el juego. instancia la ruleta y tantos jugadores como estrategias se quieran probar
class Mesa():
    def __init__(self, estrategias):
        self.ruleta = Ruleta()
        self.estrategias = estrategias #lista de FUNCIONES
        self.jugadores = [Jugador() for n in range(len(estrategias))]
        self.t = 0

    def jugar(self): 
        self.t+=1
        print("RONDA NRO: ", self.t)

        self.ruleta.girar()
        ganador = self.ruleta.getNumeroGanador()
        
        print("GANADOR: ", ganador.valor)

        # itera la lista de jugadores y de estrategias al mismo tiempo para asigarle una a c/u
        for i in range(len(self.jugadores)):
            jugador = self.jugadores[i]
            print("Jugador ", i)
            
            apuesta = self.estrategias[i](self.ruleta) # instancia una apuesta segun el estado de la ruleta y la estrategia
            print(apuesta.desc)
            jugador.cargarApuesta(apuesta)
            jugador.calcularGanancias(ganador)
            print("total: ", jugador.dinero)

        # elimina los jugadores que perdieron
        for jugador in self.jugadores:
            if jugador.isPerdedor():
                self.jugadores.remove(jugador)
                            
        print(self.ruleta.ganadores) # muestra todos los numeros que ganaron
        print("----------------------------------------------")
        


""" ESTRATEGIAS: DEBEN DEVOLVER UNA APUESTA PARA CARGARSELA A LOS JUGADORES"""

# devuelve una apuesta que contiene 3 numeros random
def estrategiaRandomNro(ruleta, n = 20):
    numeros = np.random.randint(0, 36, 3)
    print("apostando: numeros random ", numeros)
    return Apuesta(nros=numeros, desc = "estrategia RANDOM")


# devuelve una apuesta que le apuesta a rojo o negro / par o impar, si toco el valor opuesto
#  durante al menos una determinada catidadJugadas seguidas (por defecto 3)
def estrategiaRepetidos(ruleta, cantidadJugadas = 3):
    colores = ["rojo", "negro"]
    pares = [True, False]
    # le va a apostar a los que queden en la lista
    for i in range(1,cantidadJugadas+1):
        ganador = ruleta.getNumeroGanador(-i) # recorre la lista de atras para adelante
        if(ganador is None): 
            return Apuesta(desc = "estrategia REPETIDOS") # si no existe historia, no apuesta


        if ganador.color == "rojo" and "rojo" in colores:
            colores.remove("rojo")
        elif "negro" in colores:
            colores.remove("negro")
        if ganador.par and True in pares:
            pares.remove(True)
        elif False in pares:
            pares.remove(False)
    print("apostando colores: ", colores)
    print("apostando par/impar: ", pares)
    return Apuesta(clrs=colores, pares = pares, desc = "estrategia REPETIDOS")
    

estrategias = [estrategiaRandomNro, estrategiaRepetidos]
print(estrategias)

mesaDosJugadores = Mesa(estrategias)
    
for i in range(10):
    mesaDosJugadores.jugar()
