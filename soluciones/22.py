import pandas as pd

# ============================================================
# CARGA DEL ARCHIVO YA LIMPIO
# ============================================================
df = pd.read_csv('data/personas_limpio.csv')

# Personas con más de 50 años
fecha_actual = pd.to_datetime('2026-02-26')

# Calcular la fecha de nacimiento límite (50 años antes de la fecha actual)
fecha_limite_50_anios = fecha_actual - pd.DateOffset(years=50)

# Filtrar las personas que nacieron antes de la fecha límite (es decir, tienen más de 50 años)
personas_mas_50_anios = df[df['fecha_nacimiento'] < fecha_limite_50_anios]

# Contar el número de personas
num_personas_mas_50_anios = len(personas_mas_50_anios)

print(f"Número de personas con más de 50 años (a la fecha {fecha_actual.strftime('%Y-%m-%d')}): {num_personas_mas_50_anios}")