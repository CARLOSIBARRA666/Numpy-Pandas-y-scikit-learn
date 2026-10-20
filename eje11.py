# importamos las librerias
import pandas as pd
from sklearn.linear_model import LogisticRegression

# datos de los clientes
datos = {
    "edad": [18, 22, 25, 30, 35, 40, 45, 50, 55, 60],
    "ingreso": [1.2, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5],
    "compro": [0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
}

# creamos el dataframe y separamos x e y
df = pd.DataFrame(datos)
X = df[["edad", "ingreso"]]
y = df["compro"]

# entrenamos el modelo con todos los datos
modelo = LogisticRegression()
modelo.fit(X, y)

# dos clientes nuevos: 28 años con 2.2 millones y 52 años con 4.8 millones
nuevos = pd.DataFrame({"edad": [28, 52], "ingreso": [2.2, 4.8]})

# mostramos si compra o no para cada uno
for resultado in modelo.predict(nuevos):
    print("Sí compra" if resultado == 1 else "No compra")