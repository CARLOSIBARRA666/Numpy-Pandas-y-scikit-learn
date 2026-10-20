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
 
# columna con el valor total de cada producto
df["valor_inventario"] = df["precio"] * df["stock"]
 
# columna que dice si hay que reponer (true o false)
df["reponer"] = df["stock"] < 10
 
print(df)
 
