import pandas as pd

# ============================================================
# CARGA DEL ARCHIVO YA LIMPIO
# ============================================================
df = pd.read_csv('data/personas_limpio.csv')

print("=" * 60)
print("ANÁLISIS DE ESPACIOS EN COLUMNA EMAIL")
print("=" * 60)
print(f"Total de registros: {len(df)}")

# ============================================================
# DETECTAR EMAILS CON ESPACIOS ADICIONALES
# ============================================================

# Espacios al inicio o al final
espacios_borde = df['email'].str.contains(r'^\s+|\s+$', na=False).sum()

# Espacios en el medio
espacios_medio = df['email'].str.contains(r'\S\s+\S', na=False).sum()

# Total con cualquier tipo de espacio
total_con_espacios = df['email'].str.contains(r'\s', na=False).sum()

print(f"\n📋 Registros con espacios al inicio o al final : {espacios_borde}")
print(f"📋 Registros con espacios en el medio          : {espacios_medio}")
print(f"📋 Total registros con algún espacio           : {total_con_espacios}")
print(f"   ({(total_con_espacios / len(df) * 100):.2f}% del total)")

# Muestra de emails con espacios
print(f"\nEjemplos de emails con espacios (primeros 10):")
print("-" * 60)
muestra = df[df['email'].str.contains(r'\s', na=False)]['email'].head(10)
for email in muestra:
    print(f"  '{email}'")
print("-" * 60)

# ============================================================
# APLICAR LIMPIEZA - ELIMINAR ESPACIOS
# ============================================================
df['email_limpio'] = df['email'].str.strip()                  # espacios borde
df['email_limpio'] = df['email_limpio'].str.replace(r'\s+',   # espacios internos
                                                    '',
                                                    regex=True)

# ============================================================
# VERIFICACIÓN DESPUÉS DE LA LIMPIEZA
# ============================================================
print("\n")
print("=" * 60)
print("VERIFICACIÓN DESPUÉS DE LA LIMPIEZA - EMAIL")
print("=" * 60)

espacios_restantes = df['email_limpio'].str.contains(r'\s', na=False).sum()
print(f"\n✅ Emails con espacios restantes: {espacios_restantes}")

cambios = df[df['email'] != df['email_limpio']][['email', 'email_limpio']]
print(f"✅ Total registros corregidos   : {len(cambios)}")

print(f"\nEjemplos de correcciones (primeros 10):")
print("-" * 60)
print(cambios.head(10).to_string(index=False))
print("-" * 60)

# ============================================================
# REEMPLAZAR COLUMNA ORIGINAL Y GUARDAR
# ============================================================
df['email'] = df['email_limpio']
df.drop(columns=['email_limpio'], inplace=True)

df.to_csv('data/personas_limpio.csv', index=False)
print("\n")
print("=" * 60)
print("✅ Archivo guardado como: data/personas_limpio.csv")
print("=" * 60)