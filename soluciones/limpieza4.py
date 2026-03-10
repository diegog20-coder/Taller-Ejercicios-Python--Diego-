import pandas as pd

# ============================================================
# CARGA DEL ARCHIVO YA LIMPIO
# ============================================================
df = pd.read_csv('data/personas_limpio.csv')

print("=" * 60)
print("VERIFICACIÓN ANTES DE LA SEGUNDA LIMPIEZA - PROFESIÓN")
print("=" * 60)
print(f"Total de registros: {len(df)}")
print(f"\nProfesiones únicas ANTES: {df['profesion'].nunique()}")

# ============================================================
# DICCIONARIO DE CORRECCIONES
# ============================================================
correcciones = {
    'Abogdo'        : 'Abogado',
    'Administrdor'  : 'Administrador',
    'Contdor'       : 'Contador',
    'Crpintero'     : 'Carpintero',
    'Disendor'      : 'Disenador',
    'Economist'     : 'Economista',
    'Electricist'   : 'Electricista',
    'Mecnico'       : 'Mecanico',
    'Periodist'     : 'Periodista',
    'Progrmdor'     : 'Programador',
    'Trductor'      : 'Traductor',
    'Veterinrio'    : 'Veterinario',
}

# ============================================================
# APLICAR CORRECCIONES (coincidencia exacta)
# ============================================================
df['profesion'] = df['profesion'].replace(correcciones)

# ============================================================
# VERIFICACIÓN DESPUÉS DE LA SEGUNDA LIMPIEZA
# ============================================================
print("\n")
print("=" * 60)
print("VERIFICACIÓN DESPUÉS DE LA SEGUNDA LIMPIEZA - PROFESIÓN")
print("=" * 60)
print(f"\nProfesiones únicas DESPUÉS: {df['profesion'].nunique()}")

print(f"\nResultado de correcciones aplicadas:")
print("-" * 50)
for erronea, correcta in correcciones.items():
    cantidad = (df['profesion'] == correcta).sum()
    print(f"  {erronea:<20} → {correcta:<20} ({cantidad} registros)")
print("-" * 50)

print(f"\nListado final de profesiones únicas:")
print("-" * 50)
for i, prof in enumerate(sorted(df['profesion'].dropna().unique()), 1):
    cantidad = (df['profesion'] == prof).sum()
    print(f"  {i:>3}. {prof:<30} {cantidad:>7} registros")
print("-" * 50)

# ============================================================
# GUARDAR ARCHIVO FINAL
# ============================================================
df.to_csv('data/personas_limpio.csv', index=False)
print("\n")
print("=" * 60)
print("✅ Archivo guardado como: data/personas_limpio.csv")
print("=" * 60)