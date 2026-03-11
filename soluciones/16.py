import pandas as pd

# ============================================================
# CARGA DEL ARCHIVO YA LIMPIO
# ============================================================
df = pd.read_csv('data/personas_limpio.csv')

# Salario mínimo
min_salario = df['salario'].min()
print(f"El valor mínimo en la columna 'salario' (después de la limpieza) es: {min_salario}")