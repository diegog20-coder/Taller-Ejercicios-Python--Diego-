import pandas as pd

# ============================================================
# CARGA DEL ARCHIVO YA LIMPIO
# ============================================================
df = pd.read_csv('data/personas_limpio.csv')

# Filtrar registros con email que termina en 'gmail.com'
registros_gmail = df[df['email'].str.contains(r'@gmail\.com$', case=False, na=False)]

# Contar el número de registros
num_registros_gmail = len(registros_gmail)

print(f"Número de registros con email de dominio 'gmail.com': {num_registros_gmail}")