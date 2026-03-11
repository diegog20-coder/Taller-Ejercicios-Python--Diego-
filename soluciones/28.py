import pandas as pd

# ============================================================
# CARGA DEL ARCHIVO YA LIMPIO
# ============================================================
df = pd.read_csv('data/personas_limpio.csv')

# Agrupar por profesión y calcular el salario promedio
salario_promedio_por_profesion = df.groupby('profesion')['salario'].mean()

# Encontrar la profesión con el salario promedio más alto
profesion_salario_mas_alto = salario_promedio_por_profesion.idxmax()
valor_salario_mas_alto = salario_promedio_por_profesion.max()

print(f"La profesión con el salario promedio más alto es '{profesion_salario_mas_alto}' con un promedio de {valor_salario_mas_alto:.2f}.")