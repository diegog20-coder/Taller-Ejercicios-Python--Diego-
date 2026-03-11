import pandas as pd

# ============================================================
# CARGA DEL ARCHIVO YA LIMPIO
# ============================================================
df = pd.read_csv('data/personas_limpio.csv')

#Contar y mostrar registros problemátios

print("\nMuestra de registros de 'fecha_nacimiento' con formato incorrecto (primeros 30):")
print("----------------------------------------------------------------------------------")
for val in df.loc[mask_formato_incorrecto, 'fecha_nacimiento'].head(30):
    print(f"  '{val}'")
print("----------------------------------------------------------------------------------")

# normalizar el formato de fecha a 'YYYY-MM-DD'
df['fecha_nacimiento'] = df['fecha_nacimiento'].astype(str) # Ensure string type
df['fecha_nacimiento'] = df['fecha_nacimiento'].str.strip() # Remove leading/trailing spaces
df['fecha_nacimiento'] = df['fecha_nacimiento'].str.replace(r'[^0-9./-]', '', regex=True) # Remove all characters not digits, ., / or -

print("Valores únicos en la columna 'fecha_nacimiento' después de limpiar caracteres especiales y espacios (muestra):")
print(df['fecha_nacimiento'].value_counts().head(10))

#Estandarizar separadores 
df['fecha_nacimiento'] = df['fecha_nacimiento'].str.replace('.', '-', regex=False)
df['fecha_nacimiento'] = df['fecha_nacimiento'].str.replace('/', '-', regex=False)

print("Valores únicos en la columna 'fecha_nacimiento' después de estandarizar separadores (muestra):")
print(df['fecha_nacimiento'].value_counts().head(10))

## Normalizacion
df['fecha_nacimiento'] = pd.to_datetime(df['fecha_nacimiento'], errors='coerce')

print("\nPrimeros 10 registros de 'fecha_nacimiento' después de la normalización:")
print(df['fecha_nacimiento'].head(10))
print(f"\nTipo de dato de la columna 'fecha_nacimiento': {df['fecha_nacimiento'].dtype}")

# Contar y mostrar el número de valores NaT
nat_count = df['fecha_nacimiento'].isnull().sum()
print(f"\nNúmero de valores NaT en 'fecha_nacimiento' después de la conversión: {nat_count}")
