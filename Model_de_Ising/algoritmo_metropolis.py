import numpy as np
import matplotlib.pyplot as plt
import random

# Parámetros del sistema
L = 20  # Lado de la malla
N = L * L  # Total de espines
J = 1.0  # Constante de acoplamiento

num_pasos = 100000  # Número de pasos de Monte Carlo

def magnetizacion():
    """Calcula la magnetización del sistema."""
    return np.sum(malla)/N

def energia_total():
    """Calcula la energía total del sistema."""
    # Interacciones con el vecino de arriba
    interacciones_arriba = malla * np.roll(malla, 1, axis=0)
    # Interacciones con el vecino de abajo
    interacciones_abajo = malla * np.roll(malla, -1, axis=0)
    # Interacciones con el vecino de la izquierda
    interacciones_izquierda = malla * np.roll(malla, 1, axis=1)
    # Interacciones con el vecino de la derecha
    interacciones_derecha = malla * np.roll(malla, -1, axis=1)
    
    # Sumar todas las interacciones
    interacciones_totales = interacciones_arriba + interacciones_abajo + interacciones_izquierda + interacciones_derecha
    
    # Dividir por 2 para corregir el doble conteo de cada interacción
    return -J * np.sum(interacciones_totales) / 2

def paso_metropolis():
    """Realiza un paso de Metropolis."""
    i, j = np.random.randint(0, L, size=2)
    delta_E = delta_energia(i, j)
    if delta_E < 0 or np.random.rand() < np.exp(-delta_E /T):
        malla[i, j] *= -1

def delta_energia(i, j):
    """Calcula el cambio en la energía al invertir el espin (i, j)."""
    vecinos = malla[(i+1) % L, j] + malla[(i-1) % L, j] + malla[i, (j+1) % L] + malla[i, (j-1) % L]
    return 2 * J * malla[i, j] * vecinos

def simulacion_metropolis(T):
    """Ejecuta la simulación de Metropolis para una temperatura dada."""
    global malla  # Definir malla como global para que pueda ser accedida por otras funciones
    malla = np.random.choice([-1, 1], size=(L, L))
    
    # Lista para almacenar los valores de energía
    energias = []
    # Lista para almacenar los valores de magnetización
    magnetizaciones = []

    # Simulación
    for paso in range(num_pasos):
        paso_metropolis()
        # Almacenar la energía y la magnetización en cada paso
        energias.append(energia_total())
        magnetizaciones.append(magnetizacion())

    return energias, magnetizaciones  # Devolver la lista de energías y magnetizaciones

# Diccionarios para almacenar las series de energías y magnetizaciones para cada temperatura
series_energias = {}
series_magnetizaciones = {}

# Rango de temperaturas
temperaturas = np.linspace(1, 3.5, 70) 

# Ejecutar la simulación para cada temperatura
for T in temperaturas:
    energias, magnetizaciones = simulacion_metropolis(T)
    series_energias[T] = energias
    series_magnetizaciones[T] = magnetizaciones

# Graficar las series de energías
plt.figure()
for T, energias in series_energias.items():
    plt.plot(range(num_pasos), energias, label=f'T = {T}')
plt.xlabel('Tiempo de Simulación (pasos)')
plt.ylabel('Energía')
plt.title('Energía del Sistema en Función del Tiempo de Simulación')
# plt.legend()
plt.show()

# Graficar la magnetización en función de la temperatura
plt.figure()
magnetizacion_promedio = [np.mean(series_magnetizaciones[T]) for T in temperaturas]
plt.scatter(temperaturas, magnetizacion_promedio, marker='o')
plt.xlabel('Temperatura')
plt.ylabel('Magnetización Promedio')
plt.title('Magnetización Promedio en Función de la Temperatura')
plt.grid(True)
plt.show()
