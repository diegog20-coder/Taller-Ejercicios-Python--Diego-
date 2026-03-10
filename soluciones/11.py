import pandas as pd

# ============================================================
# CARGA DEL ARCHIVO YA LIMPIO
# ============================================================
df = pd.read_csv('data/personas_limpio.csv')

# ============================================================
# PROFESIONES ÚNICAS
# ============================================================
profesiones_unicas = df['profesion'].dropna().unique()
total_unicas       = len(profesiones_unicas)

print("=" * 60)
print("PROFESIONES ÚNICAS EN EL DATASET")
print("=" * 60)
print(f"\n✅ Total de profesiones únicas: {total_unicas}")

print(f"\nListado completo de profesiones:")
print("-" * 45)
for i, prof in enumerate(sorted(profesiones_unicas), 1):
    print(f"  {i:>3}. {prof}")
print("-" * 45)

# Conteo de registros por profesión (de mayor a menor)
print(f"\nRegistros por profesión (mayor a menor):")
print("-" * 45)
conteo = df['profesion'].value_counts()
for prof, cantidad in conteo.items():
    porcentaje = (cantidad / len(df)) * 100
    print(f"  {prof:<30} {cantidad:>7} registros ({porcentaje:.2f}%)")
print("-" * 45)
print(f"\n  Total registros: {len(df)}")
print("=" * 60)