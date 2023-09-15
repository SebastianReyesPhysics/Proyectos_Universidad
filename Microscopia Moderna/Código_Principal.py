# Arreglos
import numpy as np
import pandas as pd

# Directorios
import os

# Graficas
import matplotlib.pylab as plt

# Procesamiento de imagenes (mirar con cual libreria quedarse)
from PIL import Image, ImageSequence
from skimage.morphology import opening, disk, reconstruction, local_minima , closing,  square,   white_tophat
from skimage.filters import  rank, threshold_triangle, threshold_otsu, sobel, threshold_local,sobel,  threshold_sauvola, threshold_niblack
from skimage.color import label2rgb
from skimage import exposure
from skimage import filters

#Tiempo
import time


import libreria_MM as lib

# Libreria para paralelizar el procesamiento de imagenes    
from joblib import Parallel, delayed    
import multiprocessing


# Obtiene el directorio de trabajo actual y lo guarda en la variable directorio
directorio_trabajo = os.getcwd()

# Une el directorio con el nombre de la carpeta 'stacks' y lo guarda en la variable path_crecimiento
path_crecimiento = os.path.join(directorio_trabajo, "stacks")

# Crea una lista de nombres de archivos que terminan en '.tif' en la carpeta 'stacks'
nombresCR = [os.path.join(path_crecimiento,file) for file in os.listdir(path_crecimiento) if (file.endswith('.tif') )]
nombres = sorted(nombresCR)


n_jobs = -1 # usa todos los núcleos disponibles
Parallel(n_jobs=n_jobs)(delayed(lib.analisis_imagenes(15, nombres))(nombre) for nombre in nombres)


