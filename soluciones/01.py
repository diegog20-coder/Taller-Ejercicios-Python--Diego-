import pandas as pd
import codecs

datos = pd.read_csv('data/personas.csv')

print(datos.sample(10))


# Convertir la columna 'id' a string para poder buscar caracteres no numéricos
id_str = df['id'].astype(str)

# Crear una máscara booleana para identificar los IDs con caracteres no numéricos
# r'[^0-9]' busca cualquier carácter que NO sea un dígito del 0 al 9
mask_id_no_numerico = id_str.str.contains(r'[^0-9]', na=False)

# Contar el número de registros que cumplen con la condición
num_id_no_numerico = mask_id_no_numerico.sum()

print(f"Número de filas con el campo 'id' que contienen caracteres no numéricos: {num_id_no_numerico}")
