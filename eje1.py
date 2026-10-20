# importamos numpy
import numpy as np

# creamos el array con las notas
notas = np.array([7.5, 8.0, 6.5, 9.0, 5.5, 8.5])

# calculamos y mostramos cada estadistica
print("Promedio:", notas.mean())
print("Máximo:", notas.max())
print("Mínimo:", notas.min())
print("Desviación estándar:", notas.std())