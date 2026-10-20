# importamos numpy
import numpy as np

# array de temperaturas en celsius
celsius = np.array([18, 22, 25, 19, 30])

# convertimos todo a fahrenheit en una sola linea
fahrenheit = celsius * 9 / 5 + 32

print("Fahrenheit:", fahrenheit)