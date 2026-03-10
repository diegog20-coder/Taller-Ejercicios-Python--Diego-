import pandas as pd

# ============================================================
# CARGA DEL ARCHIVO YA LIMPIO
# ============================================================
df = pd.read_csv('data/personas_limpio.csv')

print("=" * 60)
print("VERIFICACIÓN ANTES DE LA SEGUNDA LIMPIEZA")
print("=" * 60)
print(f"Total de registros: {len(df)}")
print(f"\nCiudades únicas ANTES: {df['ciudad'].nunique()}")

# ============================================================
# DICCIONARIO DE CORRECCIONES
# ============================================================
correcciones = {
    'Armeni'       : 'Armenia',
    'Bogot'        : 'Bogota',
    'Brrnquill'    : 'Barranquilla',
    'Bucrmng'      : 'Bucaramanga',
    'Cli'          : 'Cali',
    'Crtgen'       : 'Cartagena',
    'Cucut'        : 'Cucuta',
    'Ibgue'        : 'Ibague',
    'Mnizles'      : 'Manizales',
    'Monteri'      : 'Monteria',
    'Neiv'         : 'Neiva',
    'Pereir'       : 'Pereira',
    'Popyn'        : 'Popayan',
    'Psto'         : 'Pasto',
    'Tunj'         : 'Tunja',
    'Villvicencio' : 'Villavicencio',
    'Vlledupr'     : 'Valledupar',
}

# ============================================================
# APLICAR CORRECCIONES (coincidencia exacta)
# ============================================================
df['ciudad'] = df['ciudad'].replace(correcciones)

# ============================================================
# VERIFICACIÓN DESPUÉS DE LA SEGUNDA LIMPIEZA
# ============================================================
print("\n")
print("=" * 60)
print("VERIFICACIÓN DESPUÉS DE LA SEGUNDA LIMPIEZA")
print("=" * 60)
print(f"\nCiudades únicas DESPUÉS: {df['ciudad'].nunique()}")

print(f"\nResultado de correcciones aplicadas:")
print("-" * 45)
for erronea, correcta in correcciones.items():
    cantidad = (df['ciudad'] == correcta).sum()
    print(f"  {erronea:<20} → {correcta:<15} ({cantidad} registros)")
print("-" * 45)

print(f"\nListado final de ciudades únicas:")
print("-" * 45)
for i, ciudad in enumerate(sorted(df['ciudad'].dropna().unique()), 1):
    cantidad = (df['ciudad'] == ciudad).sum()
    print(f"  {i:>3}. {ciudad:<25} {cantidad:>7} registros")
print("-" * 45)

# ============================================================
# GUARDAR ARCHIVO FINAL
# ============================================================
df.to_csv('data/personas_limpio.csv', index=False)
print("\n")
print("=" * 60)
print("✅ Archivo guardado como: data/personas_limpio.csv")
print("=" * 60)