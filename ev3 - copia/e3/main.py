import random
from time import time

from bubble import bubbleSort
from merge import mergeSort
#-------------------------------
def generarArr(tam):
    lista = []
    for i in range(0,tam):
        lista.append(random.randrange(0,tam))
    return lista
def contarTiempos(lista):
    for i in range (len(lista)):
        #print(list1[i])
        print(titulos[i],"\tcreado correctamente")
        start_time = time()
        bubbleSort(lista[i])
        t_bubble = (time() - start_time)

        start_time = time()
        mergeSort(lista[i])
        t_merge = (time() - start_time)

        # 1 segundo = 1000000 milisegundos (ms)
        tiempos_bubble.append(t_bubble*1000000)
        tiempos_merge.append(t_merge*1000000)
def guardarDatos():
    archivo_bubble = open("tiempo_bubble.txt", "a")
    for i in range(len(tiempos_bubble)):
        #print(tiempos_bubble[i])
        texto = str(tiempos_bubble[i]) + "\n"
        archivo_bubble.write (texto)
    archivo_bubble.close()

    archivo_merge = open("tiempo_merge.txt", "a")
    for i in range(len(tiempos_merge)):
        #print(tiempos_merge[i])
        texto = str(tiempos_merge[i]) + "\n"
        archivo_merge.write (texto)
    archivo_merge.close()
def string_a_float(opc):
    # si es 1 abre txt de bubble si es 2 abre txt merge 
    if opc == 1:
        txt = "tiempo_bubble.txt"
    elif opc == 2:
        txt = "tiempo_merge.txt"
    else:
        print("ERORR EN string_a_float(opc): ",opc," no valido")
    lista_flotantes = []
    archivo =  open (txt, "r")
    lista_lineas = archivo.readlines()
    archivo.close()
    for i in lista_lineas:
        lista_flotantes.append(float(i))
    return lista_flotantes
# Graficos
def f(x):     	
    indice = listaTamanios.index(x)
    print("indice: ",indice)
    for i in range(1,indice):
        for j in range(1,indice,3):   
            x = lista_acum_bubble[j]
    return x
def g(x):
    indice = listaTamanios.index(x)
    for i in range(indice):
        for j in range(0,indice,3):   
            x = lista_acum_merge[i]
    return x
def generarGrafico():   
    fx = lista_acum_bubble
    gx = lista_acum_merge
    #print(fx)
    #print(gx)
    
    print("GRAFICO GENERADO")
#-----------
# -------------------
# VARS
listaTamanios = [1000, 10000, 50000, 150000, random.randrange(400000  ,1000000)]
TAM = listaTamanios[0]
# ENTRADAS
arrAleatorio = generarArr(TAM)
arrCreciente = sorted(arrAleatorio)
arrDecreciente = sorted(arrAleatorio, reverse =True)

listArrays =  [arrAleatorio,arrCreciente,arrDecreciente]
titulos = ['arrAleatorio', 'arrCreciente', 'arrDecreciente']
tiempos_bubble = []
tiempos_merge = [] 
lista_acum_bubble = string_a_float(1)
lista_acum_merge = string_a_float(2)
def main():
    pass