# importamos pandas
import pandas as pd

# datos del inventario
inventario = {
    "producto": ["Camisa", "Gorra", "Pantalón", "Medias", "Zapatos"],
    "precio": [45000, 30000, 89000, 8000, 150000],
    "stock": [20, 5, 12, 40, 3],
}

# creamos el dataframe
df = pd.DataFrame(inventario)

# guardamos en csv (index=false evita guardar la columna de numeros)
df.to_csv("inventario.csv", index=False)

# leemos el archivo de nuevo
df2 = pd.read_csv("inventario.csv")

print(df2)

# verificamos que los datos sean iguales
print("¿Son iguales?", df.equals(df2))