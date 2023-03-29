import numpy as np
import generacionPoblacion as gP
import funcionesGenetico as fG
import matplotlib.pyplot as plt
import time

if __name__ == '__main__':
    '''inicio = time.time()
    listaEv, listaPun, reinicios, listaCromosomas = fG.genetico_CHC(baseDatos=1, nPoblacion=30, numeroElite=2,
                                                                    distanciaHinicial=5, prueba=False)
    fin = time.time()
    tiempo = fin - inicio
    print(f"Tiempo ejecucion: {tiempo}")
    # Pinto en el fichero
    dirFichero = './Zalando.txt'

    mejorCromosoma = fG.arrayLimpio(listaCromosomas[-1])
    fG.escribeFichero(dirFichero=dirFichero, listaEv=listaEv, listaPun=listaPun, reinicios=reinicios,
                      mejorCromosoma=mejorCromosoma)

    fG.pintarGrafica(listaEv, listaPun, True, "Genetico CHC Zalando")'''
    vector = [2, 2, 2, 1, 1, 1, 1, 4, 1, 1, 1, 4, 1, 1, 1, 4, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2, 3, 1, 4, 5, 6, 7, 1, 1, 2, 6, 4, 1, 1, 1, 4, 1, 1, 1, 4, 1, 1, 1, 1, 2, 1, 1, 1, 3, 6]



    print(fG.traducirConfiguracion(vector))

