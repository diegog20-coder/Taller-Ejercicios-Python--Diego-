import pandas as pd

df = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/personas_limpio.csv')

print("Primeras 5 filas del DataFrame 'df':")
print(df.head())

print(f"\nForma del DataFrame 'df': {df.shape}")

## Detectar el tipo de la columna activo

print(f"Tipo de dato de la columna 'activo': {df['activo'].dtype}")

## detectar valores únicos de la columna activo

print(f"\nValores únicos en la columna 'activo':")
print(df['activo'].value_counts())
print(f"\nNúmero de valores únicos: {df['activo'].nunique()}")

print("\n--- Muestra de valores problemáticos en 'activo' ---")

# Identificar valores problemáticos únicos (cualquier cosa que no sea exactamente "Verdadero" o "Falso")
problematic_unique_values = df['activo'].loc[~df['activo'].isin(['True', 'False'])].unique()

if len(problematic_unique_values) > 0:
    print(f"Valores problemáticos únicos (muestra, {len(problematic_unique_values)} encontrados):")
    for val in problematic_unique_values[:10]: # Display up to 10 unique problematic values
        print(f"- '{val}'")
else:
    print("No se encontraron valores problemáticos más allá de 'True' o 'False'.")
print("---------------------------------------------------")

## Limpieza de la columna activo estandarización a minúsculas y eliminación de espacios en blanco

df['activo'] = df['activo'].astype(str).str.strip().str.lower()

print("Valores únicos en la columna 'activo' después de estandarizar a minúsculas y limpiar espacios:")
print(df['activo'].value_counts())
print(f"\nNúmero de valores únicos: {df['activo'].nunique()}")

## Reemplazar los valores '0' y '1' por 'false' y 'true' respectivamente
df['activo'] = df['activo'].str.replace('0', 'false', regex=False)
df['activo'] = df['activo'].str.replace('1', 'true', regex=False)

print("Valores únicos en la columna 'activo' después de mapear '0' a 'false' y '1' a 'true':")
print(df['activo'].value_counts())
print(f"\nNúmero de valores únicos: {df['activo'].nunique()}")

## convertir valores lingüísticos comunes a booleanos estándar
df['activo'] = df['activo'].str.replace('si', 'true', regex=False)
df['activo'] = df['activo'].str.replace('no', 'false', regex=False)
df['activo'] = df['activo'].str.replace('yes', 'true', regex=False)

print("Valores únicos en la columna 'activo' después de mapear valores lingüísticos:")
print(df['activo'].value_counts())
print(f"\nNúmero de valores únicos: {df['activo'].nunique()}")

## Finalmente, convertir la columna 'activo' a tipo booleano
df['activo'] = df['activo'].str.replace(r'[^a-z]', '', regex=True)

print("Valores únicos en la columna 'activo' después de eliminar caracteres especiales:")
print(df['activo'].value_counts())
print(f"\nNúmero de valores únicos: {df['activo'].nunique()}")