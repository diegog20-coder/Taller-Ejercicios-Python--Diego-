import pandas as pd

# ============================================================
# CARGA DEL ARCHIVO YA LIMPIO
# ============================================================
df = pd.read_csv('data/personas_limpio.csv')

# ============================================================
# CONTEO DE REGISTROS - INGENIERO
# ============================================================
total_ingeniero = (df['profesion'] == 'Ingeniero').sum()

print("=" * 60)
print("CONTEO DE REGISTROS - INGENIERO")
print("=" * 60)
print(f"\n✅ Total de registros con profesión 'Ingeniero': {total_ingeniero}")
print(f"   Del total de {len(df)} registros ({(total_ingeniero / len(df) * 100):.2f}%)")
print("=" * 60)