import pandas as pd

# ============================================================
# CARGA DEL ARCHIVO YA LIMPIO
# ============================================================
df = pd.read_csv('data/personas_limpio.csv')

# Filtrar registros por profesión 'Ingeniero'
ingenieros = df[df['profesion'] == 'Ingeniero']

# Agrupar por ciudad y contar el número de ingenieros en cada ciudad
conteo_ingenieros_por_ciudad = ingenieros['ciudad'].value_counts()

# Obtener la ciudad con el mayor número de ingenieros
ciudad_con_mas_ingenieros = conteo_ingenieros_por_ciudad.idxmax()
num_ingenieros_en_esa_ciudad = conteo_ingenieros_por_ciudad.max()

print(f"La ciudad con más Ingenieros es '{ciudad_con_mas_ingenieros}' con {num_ingenieros_en_esa_ciudad} registros.")