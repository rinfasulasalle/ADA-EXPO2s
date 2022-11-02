import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from main import tiempos_bubble, tiempos_merge,TAM, listaTamanios
def guardarDatos():
    archivo_bubble = open("datos\ atiempo_bubble.txt", "a")
    for i in range(len(tiempos_bubble)):
        #print(tiempos_bubble[i])
        texto = str(tiempos_bubble[i]) + "\n"
        archivo_bubble.write (texto)
    archivo_bubble.close()

    archivo_merge = open("datos\ atiempo_merge.txt", "a")
    for i in range(len(tiempos_merge)):
        #print(tiempos_merge[i])
        texto = str(tiempos_merge[i]) + "\n"
        archivo_merge.write (texto)
    archivo_merge.close()

def string_a_float(opc):
    # si es 1 abre txt de bubble si es 2 abre txt merge 
    if opc == 1:
        txt = "datos\ atiempo_bubble.txt"
    elif opc == 2:
        txt = "datos\ atiempo_merge.txt"
    else:
        print("ERORR EN string_a_float(opc): opc no valida")
    lista_flotantes = []
    archivo =  open (txt, "r")
    lista_lineas = archivo.readlines()
    archivo.close()
    for i in lista_lineas:
        lista_flotantes.append(float(i))
    #print(lista_flotantes)
    return lista_flotantes
#--------------------------------------------------
# Graficos
def encontraIndice(num,lista):
    for i in range (len(lista)):
        if num in lista[i]:
            return i
def f(x):
    indice = encontraIndice(TAM,listaTamanios)
    for i in range(indice):
        for j in range(0,indice,3):   
            return x
def generarGrafico():   
    fx = lista_acum_bubble
    gx = lista_acum_merge
    #print(fx)
    #print(gx)
    
    print("GRAFICO GENERADO")
#-----------
#guardarDatos()
lista_acum_bubble = string_a_float(1)
lista_acum_merge = string_a_float(2)
generarGrafico()