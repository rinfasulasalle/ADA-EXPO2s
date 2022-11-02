import random
from time import time

from bubble import bubbleSort
from merge import mergeSort

#-----------------------------------
def generarArr(tam):
    lista = []
    for i in range(0,tam):
        lista.append(random.randrange(0,tam))
    return lista
def contarTiempos(list1):
    for i in range (len(list1)):
        #print(list1[i])
        print(titulos[i],"\tcreado correctamente")
        start_time = time()
        bubbleSort(list1[i])
        t_bubble = (time() - start_time)

        start_time = time()
        mergeSort(list1[i])
        t_merge = (time() - start_time)

        # 1 segundo = 1000000 milisegundos (ms)
        tiempos_bubble.append(t_bubble*1000000)
        tiempos_merge.append(t_merge*1000000)
#-----------------------------------
# VARS USADAS
listaTamanios = [1000, 10000, 50000, 150000, random.randrange(400000  ,1000000)]
TAM = listaTamanios[1]
# ENTRADAS
arrAleatorio = generarArr(TAM)
arrCreciente = sorted(arrAleatorio)
arrDecreciente = sorted(arrAleatorio, reverse =True)

listArrays =  [arrAleatorio,arrCreciente,arrDecreciente]
titulos = ['arrAleatorio', 'arrCreciente', 'arrDecreciente']
tiempos_bubble = []
tiempos_merge = [] 
#-----------------------------------
# Imprimiendo  la tabla
contarTiempos(listArrays)
print("Tabla generada con n =", TAM)
for i in range(len(titulos)):
    print("************** Tiempo con",titulos[i],"(ms) *********")
    print("\t tiempo_bubble\t\t tiempo_merge")
    print("\t", tiempos_bubble[i],"\t",tiempos_merge[i],"\n")
#print(tiempos_bubble,'\n',tiempos_merge)

