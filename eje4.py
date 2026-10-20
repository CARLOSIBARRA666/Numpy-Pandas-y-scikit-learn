# importamos numpy
import numpy as np

# matriz de 3 estudiantes (filas) por 4 materias (columnas)
calificaciones = np.array([
    [8.5, 7.0, 9.0, 8.0],  # carlos
    [6.0, 7.5, 8.0, 7.0],  # ana
    [9.0, 8.5, 9.5, 9.0],  # luis
])

# axis=1 promedia por fila (cada estudiante)
print("Promedio por estudiante:", calificaciones.mean(axis=1))

# axis=0 promedia por columna (cada materia)
print("Promedio por materia:", calificaciones.mean(axis=0))