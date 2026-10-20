# importamos las librerias
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

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

# probamos tres tamaños de prueba: 20%, 30% y 50%
for tamano in [0.2, 0.3, 0.5]:
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=tamano, random_state=42)
    modelo = LogisticRegression()
    modelo.fit(X_train, y_train)
    precision = accuracy_score(y_test, modelo.predict(X_test))
    print("test_size =", tamano, "-> precisión:", precision)

# explicacion:
# son solo 10 datos. al cambiar test_size cambia cuales clientes quedan
# en entrenamiento y cuales en prueba. con tan pocos datos, un solo cliente
# mal clasificado cambia mucho la precision.
# aqui los datos son muy ordenados (a mayor edad e ingreso, compra), por eso
# la precision puede salir igual (100%), pero si cambias random_state o los
# datos, la precision puede variar bastante. con test_size=0.5 el modelo
# aprende con solo 5 clientes y el resultado es menos confiable.