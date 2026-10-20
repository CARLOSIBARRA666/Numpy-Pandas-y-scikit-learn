# importamos numpy
import numpy as np

# convertimos la lista de ventas en un array
ventas = np.array([120000, 95000, 150000, 80000, 200000, 175000, 110000])

# multiplicamos por 1.10 para subir 10% (sin bucles)
ventas_nuevas = ventas * 1.10

# mostramos las ventas nuevas y el total de la semana
print("Ventas con aumento:", ventas_nuevas)
print("Total de la semana:", ventas_nuevas.sum())