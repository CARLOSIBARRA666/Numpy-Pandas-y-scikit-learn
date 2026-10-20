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

# creamos el dataframe
df = pd.DataFrame(datos)

# x son las entradas y y es lo que queremos predecir
X = df[["edad", "ingreso"]]
y = df["compro"]

# dividimos en 80% entrenamiento y 20% prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# creamos y entrenamos el modelo
modelo = LogisticRegression()
modelo.fit(X_train, y_train)

# predecimos con los datos de prueba y medimos la precision
predicciones = modelo.predict(X_test)
print("Precisión:", accuracy_score(y_test, predicciones))