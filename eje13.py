# importamos las librerias
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# datos de los estudiantes
estudiantes = {
    "horas_estudio": [2, 4, 5, 6, 8, 10, 3, 7, 9, 1],
    "asistencia": [60, 70, 75, 80, 90, 95, 65, 85, 92, 50],
    "aprobo": [0, 0, 1, 1, 1, 1, 0, 1, 1, 0],
}

# parte pandas: creamos el dataframe y mostramos las estadisticas
df = pd.DataFrame(estudiantes)
print(df.describe())

# nueva columna con las horas de estudio divididas entre 7
df["promedio_semanal"] = df["horas_estudio"] / 7

# filtramos los que aprobaron con menos de 6 horas
print("\nAprobaron con menos de 6 horas:")
print(df[(df["aprobo"] == 1) & (df["horas_estudio"] < 6)])

# parte numpy: promedio y desviacion estandar de la asistencia
print("\nPromedio asistencia:", np.mean(df["asistencia"]))
print("Desviación estándar asistencia:", np.std(df["asistencia"]))

# parte scikit-learn: x son las entradas y y es lo que queremos predecir
X = df[["horas_estudio", "asistencia"]]
y = df["aprobo"]

# dividimos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# entrenamos el modelo
modelo = LogisticRegression()
modelo.fit(X_train, y_train)

# evaluamos la precision
print("\nPrecisión:", accuracy_score(y_test, modelo.predict(X_test)))

# predecimos para un aprendiz de 5 horas y 78% de asistencia
nuevo = pd.DataFrame({"horas_estudio": [5], "asistencia": [78]})
resultado = modelo.predict(nuevo)[0]
print("Aprendiz de 5 horas y 78% asistencia:", "Aprueba" if resultado == 1 else "No aprueba")