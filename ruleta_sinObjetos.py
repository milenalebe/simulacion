import numpy as np
import matplotlib.pyplot as plt
import statistics



def generarTiradas(t):
    return np.random.randint(0,37,t)

def primerasXtiradas(tiradas, x)
    return tiradas[0:x]


# Recibe una lista de tiradas y devuelve una lista de la ESPERANZA, calculada hasta la i-esima tirada
def calcularEsperanza(tiradas, t):
    return [np.mean(primerasXtiradas(x)) for x in range(t)] # calcula la esperanza de las primeras x tiradas iterando x de 0 a t

# VARIANZA
def calcularVarianza(tiradas, t):
    return [np.var(primerasXtiradas(x)) for x in range(t)] 

# DESVIO
def calcularDesvio(tiradas, t):
    return [np.std(primerasXtiradas(x) for x in range(t))]

# FRECUENCIA RELATIVA: Diccionario con cada numero n (clave) del 0 al 36
# y su respectiva lista de la frecuencia en funcion del nro de tirada (valor)
def calcularFrecuenciaRelativa(tiradas, t):
    frecDict = {}
        for n in range(37): 
            cantidad_n = tiradas.count(n) # cuenta la cantidad de veces que aparece cada n en las tiradas
            frecDict.update({n:cantidad_n/t}) # agrega n al diccionario con valor cantidad_n/t (frecuencia relativa)  
    return frecDict


# FRECUENCIA ABSOLUTA : Diccionario con cada numero n
# y la cantidad de veces que aparece hasta la tirada n
def calcularFrecuenciaAbsoluta(tiradas, t):
    frecDict = {}
        for n in range(37): 
            cantidad_n = tiradas.count(n) # cuenta la cantidad de veces que aparece cada n en las tiradas
            frecDict.update({n:cantidad_n/t}) # agrega n al diccionario con valor cantidad_n/t (frecuencia relativa)  
    return frecAbsDict

def plotGrafico(x, y, x_label, y_label, g_label):
    fig,(ax6) = plt.subplots()
    ax6.axhline(10.67, 0, 1, label='Desvio Teórica', c='red', ls=':')
    ax6.plot(x, y, label=g_label)
    ax6.set_xlabel(x_label)
    ax6.set_ylabel(y_label)
    ax6.grid(axis = 'y')
    ax6.legend()
    plt.show()

def plotHistograma(dict)
    


# genera tiradas y calcula estadisticos
t = int(input("Ingrese numero de tiradas: "))
tiradas = generarTiradas(t)
print(tiradas)
esperanza = calcularEsperanza(tiradas, t)
varianza = calcularVarianza(tiradas, t)
desvio = calcularDesvio(tiradas, t)
frecuenciasDict = calcularFrecuenciaRelativa(tiradas, t)

# grafico media

# grafico varianza

# grafico desvio

# histogramas
