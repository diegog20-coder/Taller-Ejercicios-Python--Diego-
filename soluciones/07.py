import pandas as pd

# ============================================================
# CARGA DEL ARCHIVO YA LIMPIO
# ============================================================
df = pd.read_csv('data/personas_limpio.csv')

# ============================================================
# CONTEO DE REGISTROS - MEDELLÍN
# ============================================================
total_medellin = (df['ciudad'] == 'Medellin').sum()

print("=" * 60)
print("CONTEO DE REGISTROS - MEDELLÍN")
print("=" * 60)
print(f"\n✅ Total de registros con ciudad 'Medellín': {total_medellin}")
print(f"   Del total de {len(df)} registros ({(total_medellin / len(df) * 100):.2f}%)")
print("=" * 60)