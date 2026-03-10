import pandas as pd

# ============================================================
# CARGA DEL ARCHIVO YA LIMPIO
# ============================================================
df = pd.read_csv('data/personas_limpio.csv')

# ============================================================
# CIUDADES ÚNICAS
# ============================================================
ciudades_unicas = df['ciudad'].dropna().unique()
total_unicas    = len(ciudades_unicas)

print("=" * 60)
print("CIUDADES ÚNICAS EN EL DATASET")
print("=" * 60)
print(f"\n✅ Total de ciudades únicas: {total_unicas}")
print(f"\nListado completo de ciudades:")
print("-" * 40)
for i, ciudad in enumerate(sorted(ciudades_unicas), 1):
    print(f"  {i:>3}. {ciudad}")
print("-" * 40)

# Conteo de registros por ciudad (de mayor a menor)
print(f"\nRegistros por ciudad (mayor a menor):")
print("-" * 40)
conteo = df['ciudad'].value_counts()
for ciudad, cantidad in conteo.items():
    porcentaje = (cantidad / len(df)) * 100
    print(f"  {ciudad:<25} {cantidad:>7} registros ({porcentaje:.2f}%)")
print("-" * 40)
print(f"\n  Total registros: {len(df)}")
print("=" * 60)