import pandas as pd

# ============================================================
# CARGA DEL ARCHIVO YA LIMPIO
# ============================================================
df = pd.read_csv('data/personas_limpio.csv')

# ============================================================
# CONTEO DE REGISTROS - PROGRAMADOR
# ============================================================
total_programador = (df['profesion'] == 'Programador').sum()

print("=" * 60)
print("CONTEO DE REGISTROS - PROGRAMADOR")
print("=" * 60)
print(f"\n✅ Total de registros con profesión 'Programador': {total_programador}")
print(f"   Del total de {len(df)} registros ({(total_programador / len(df) * 100):.2f}%)")