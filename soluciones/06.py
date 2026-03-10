import pandas as pd

# ============================================================
# CARGA DEL ARCHIVO YA LIMPIO
# ============================================================
df = pd.read_csv('data/personas_limpio.csv')

# ============================================================
# CONTEO DE REGISTROS - BOGOTÁ
# ============================================================
total_bogota = (df['ciudad'] == 'Bogota').sum()

print("=" * 60)
print("CONTEO DE REGISTROS - BOGOTÁ")
print("=" * 60)
print(f"\n✅ Total de registros con ciudad 'Bogotá': {total_bogota}")
print(f"   Del total de {len(df)} registros ({(total_bogota / len(df) * 100):.2f}%)")
print("=" * 60)