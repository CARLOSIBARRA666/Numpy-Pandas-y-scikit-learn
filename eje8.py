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

# ordenamos del mas caro al mas barato
print(df.sort_values("precio", ascending=False))

# precio promedio de todos los productos
print("Precio promedio:", df["precio"].mean())