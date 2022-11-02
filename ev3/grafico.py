import matplotlib
import matplotlib.pyplot as plt
from manejo_datos_txt import lista_acum_bubble,lista_acum_merge
#print(lista_acum_bubble)
x = lista_acum_bubble
y = lista_acum_merge

# usa las listas noma par el grafico
#ya estan en flotantes

plt.title("Tiempo Bubble")
plt.xlabel('Tiempo')
plt.ylabel('datos')
plt.yticks(x)
plt.plot(y, y, marker = 'o', c = 'g')

plt.show()
plt.savefig("graficos\ g1.png")