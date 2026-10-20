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
 
# filtramos los productos con stock menor a 10
print(df[df["stock"] < 10])
 
