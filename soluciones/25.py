import pandas as pd

# ============================================================
# CARGA DEL ARCHIVO YA LIMPIO
# ============================================================
df = pd.read_csv('data/personas_limpio.csv')

# Filtrar registros con profesión 'Abogado' y salario mayor a 10,000,000
registros_abogado_salario_alto = df[(df['profesion'] == 'Abogado') & (df['salario'] > 10000000)]

# Contar el número de registros que cumplen ambas condiciones
num_abogado_salario_alto = len(registros_abogado_salario_alto)

print(f"Número de registros con profesión 'Abogado' y salario > 10,000,000: {num_abogado_salario_alto}")