import pandas as pd

# ============================================================
# CARGA DEL ARCHIVO YA LIMPIO
# ============================================================
df = pd.read_csv('data/personas_limpio.csv')

# Definir la fecha límite para nacidos después de 1980
fecha_limite_1980 = pd.to_datetime('1980-12-31')

# Filtrar registros que cumplen las tres condiciones
registros_filtrados_barranquilla = df[
    (df['ciudad'] == 'Barranquilla') &
    (df['activo'] == True) &
    (df['fecha_nacimiento'] > fecha_limite_1980)
]

# Contar el número de registros
num_registros_barranquilla = len(registros_filtrados_barranquilla)

print(f"Número de registros con ciudad 'Barranquilla', activos y nacidos después de 1980: {num_registros_barranquilla}")