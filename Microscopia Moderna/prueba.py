import numpy as np
import matplotlib.pyplot as plt

# Se leen archivos con extension .txt usando numpy y su contenido se guarda en un array

# Se leen los archivos de intensidad
intensidad_1 = np.loadtxt('intensidad1.txt', delimiter = ',')
intensidad_10 = np.loadtxt('intensidad10.txt', delimiter = ',')
intensidad_11 = np.loadtxt('intensidad11.txt', delimiter = ',')
intensidad_12 = np.loadtxt('intensidad12.txt', delimiter = ',')
intensidad_13 = np.loadtxt('intensidad13.txt', delimiter = ',')
intensidad_14 = np.loadtxt('intensidad14.txt', delimiter = ',')
intensidad_15 = np.loadtxt('intensidad15.txt', delimiter = ',')
intensidad_16 = np.loadtxt('intensidad16.txt', delimiter = ',')
intensidad_17 = np.loadtxt('intensidad17.txt', delimiter = ',')

# Se promedian los valores de cada archivo y se almacenan en un array

intensidad_promedio = np.array([np.mean(intensidad_1), np.mean(intensidad_10), np.mean(intensidad_11), np.mean(intensidad_12), np.mean(intensidad_13), np.mean(intensidad_14), np.mean(intensidad_15), np.mean(intensidad_16), np.mean(intensidad_17)])

maximo = np.max(intensidad_promedio)
intensidad_promedio = intensidad_promedio/maximo
# Etiqeutas para el eje x
etiquetas = ['T1', 'T10', 'T11', 'T12', 'T13','T14', 'T15', 'T16','T17']

# Se grafican los valores promedio de intensidad en funcion del tiempo
plt.plot(etiquetas, intensidad_promedio, 'o-')
plt.xlabel('Archivo .tiff')
plt.ylabel('Intensidad promedio')
plt.title('Intensidad promedio de T2 a T11')
plt.show()
