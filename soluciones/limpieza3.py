import pandas as pd
import re

# ============================================================
# CARGA DEL ARCHIVO YA LIMPIO
# ============================================================
df = pd.read_csv('data/personas_limpio.csv')

print("=" * 60)
print("VERIFICACIÓN ANTES DE LA LIMPIEZA - PROFESIÓN")
print("=" * 60)
print(f"Total de registros: {len(df)}")
print(f"\nProfesiones únicas ANTES: {df['profesion'].nunique()}")
print(f"\nMuestra de profesiones ANTES de limpiar:")
print(df['profesion'].head(20).to_string())
print(f"\nValores únicos (primeros 20):")
print(df['profesion'].unique()[:20])


# ============================================================
# DICCIONARIO: NÚMEROS → LETRAS
# ============================================================
numeros_a_letras = {
    '0': 'o',
    '1': 'i',
    '2': 'z',
    '3': 'e',
    '4': 'a',
    '5': 's',
    '6': 'g',
    '7': 't',
    '8': 'b',
    '9': 'q'
}

# ============================================================
# FUNCIÓN DE LIMPIEZA
# ============================================================
def limpiar_profesion(profesion):
    if pd.isna(profesion):
        return profesion

    # 1. Convertir a string
    profesion = str(profesion)

    # 2. Eliminar espacios adicionales (inicio, fin y dobles)
    profesion = profesion.strip()
    profesion = re.sub(r'\s+', ' ', profesion)

    # 3. Eliminar caracteres especiales (@, %, #, !, $, &, *, etc.)
    profesion = re.sub(r'[^a-zA-Z0-9áéíóúÁÉÍÓÚñÑüÜ\s\-]', '', profesion)

    # 4. Reemplazar números por letras
    for numero, letra in numeros_a_letras.items():
        profesion = profesion.replace(numero, letra)

    # 5. Corregir mayúsculas inconsistentes → Title Case
    profesion = profesion.title()

    # 6. Limpieza final de espacios
    profesion = profesion.strip()

    return profesion


# ============================================================
# APLICAR LIMPIEZA
# ============================================================
df['profesion_limpia'] = df['profesion'].apply(limpiar_profesion)


# ============================================================
# VERIFICACIÓN DESPUÉS DE LA LIMPIEZA
# ============================================================
print("\n")
print("=" * 60)
print("VERIFICACIÓN DESPUÉS DE LA LIMPIEZA - PROFESIÓN")
print("=" * 60)

# Comparación lado a lado
cambios = df[df['profesion'] != df['profesion_limpia']][['profesion', 'profesion_limpia']]

print(f"\nTotal de registros modificados: {len(cambios)}")
print(f"\nEjemplos de cambios realizados (primeros 20):")
print(cambios.head(20).to_string(index=False))

# Verificaciones
tiene_especiales = df['profesion_limpia'].str.contains(r'[@%#!$&*]', na=False).sum()
print(f"\n✅ Profesiones con caracteres especiales restantes : {tiene_especiales}")

tiene_numeros = df['profesion_limpia'].str.contains(r'\d', na=False).sum()
print(f"✅ Profesiones con números restantes               : {tiene_numeros}")

tiene_espacios = df['profesion_limpia'].str.contains(r'\s{2,}', na=False).sum()
print(f"✅ Profesiones con espacios dobles restantes       : {tiene_espacios}")

nulos = df['profesion_limpia'].isna().sum()
print(f"✅ Valores nulos en profesion                      : {nulos}")

print(f"\nProfesiones únicas ANTES : {df['profesion'].nunique()}")
print(f"Profesiones únicas DESPUÉS: {df['profesion_limpia'].nunique()}")

print(f"\nListado de profesiones únicas después de limpieza:")
print("-" * 45)
for i, prof in enumerate(sorted(df['profesion_limpia'].dropna().unique()), 1):
    cantidad = (df['profesion_limpia'] == prof).sum()
    print(f"  {i:>3}. {prof:<30} {cantidad:>7} registros")
print("-" * 45)


# ============================================================
# REEMPLAZAR COLUMNA ORIGINAL Y GUARDAR
# ============================================================
df['profesion'] = df['profesion_limpia']
df.drop(columns=['profesion_limpia'], inplace=True)

df.to_csv('data/personas_limpio.csv', index=False)
print("\n")
print("=" * 60)
print("✅ Archivo guardado como: data/personas_limpio.csv")
print("=" * 60)