import pandas as pd
import re

# ============================================================
# CARGA DEL ARCHIVO
# ============================================================
df = pd.read_csv('data/personas.csv')

print("=" * 60)
print("VERIFICACIÓN ANTES DE LA LIMPIEZA")
print("=" * 60)
print(f"Total de registros: {len(df)}")
print(f"\nMuestra de ciudades ANTES de limpiar:")
print(df['ciudad'].head(20).to_string())
print(f"\nValores únicos (primeros 20):")
print(df['ciudad'].unique()[:20])


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
# REGLAS EXPLÍCITAS: patrón con caracteres especiales → nombre correcto
# Se aplican ANTES de cualquier otra limpieza
# ============================================================
reglas_especiales = [
    # Captura: Snt Mrt (sin vocales completas)
    (r'(?i)snt\s+mrt', 'Santa Marta'),
    # Captura: S@nt@ M@rt@, S#nta M#rta, Snta Mrta, etc.
    (r'(?i)s.?nt.?\s+m.?rt.?', 'Santa Marta'),
]

# ============================================================
# FUNCIÓN DE LIMPIEZA
# ============================================================
def limpiar_ciudad(ciudad):
    if pd.isna(ciudad):
        return ciudad

    # 1. Convertir a string
    ciudad = str(ciudad)

    # 2. Aplicar reglas explícitas PRIMERO (antes de eliminar caracteres especiales)
    for patron, reemplazo in reglas_especiales:
        if re.search(patron, ciudad):
            return reemplazo

    # 3. Eliminar espacios adicionales (inicio, fin y dobles)
    ciudad = ciudad.strip()
    ciudad = re.sub(r'\s+', ' ', ciudad)

    # 4. Eliminar caracteres especiales (@, %, #, !, $, &, *, etc.)
    ciudad = re.sub(r'[^a-zA-Z0-9áéíóúÁÉÍÓÚñÑüÜ\s\-]', '', ciudad)

    # 5. Reemplazar números por letras
    for numero, letra in numeros_a_letras.items():
        ciudad = ciudad.replace(numero, letra)

    # 6. Corregir mayúsculas inconsistentes → Title Case
    ciudad = ciudad.title()

    # 7. Limpieza final de espacios
    ciudad = ciudad.strip()

    return ciudad


# ============================================================
# APLICAR LIMPIEZA
# ============================================================
df['ciudad_limpia'] = df['ciudad'].apply(limpiar_ciudad)


# ============================================================
# VERIFICACIÓN DESPUÉS DE LA LIMPIEZA
# ============================================================
print("\n")
print("=" * 60)
print("VERIFICACIÓN DESPUÉS DE LA LIMPIEZA")
print("=" * 60)

# Comparación lado a lado
comparacion = df[['ciudad', 'ciudad_limpia']].copy()
cambios = comparacion[comparacion['ciudad'] != comparacion['ciudad_limpia']]

print(f"\nTotal de registros modificados: {len(cambios)}")
print(f"\nEjemplos de cambios realizados (primeros 20):")
print(cambios.head(20).to_string(index=False))

# Verificar que no queden caracteres especiales
tiene_especiales = df['ciudad_limpia'].str.contains(r'[@%#!$&*]', na=False).sum()
print(f"\n✅ Ciudades con caracteres especiales restantes: {tiene_especiales}")

# Verificar que no queden números
tiene_numeros = df['ciudad_limpia'].str.contains(r'\d', na=False).sum()
print(f"✅ Ciudades con números restantes: {tiene_numeros}")

# Verificar espacios dobles
tiene_espacios = df['ciudad_limpia'].str.contains(r'\s{2,}', na=False).sum()
print(f"✅ Ciudades con espacios dobles restantes: {tiene_espacios}")

# Verificar que Santa Marta quedó bien corregida
santa_marta_ok = (df['ciudad_limpia'] == 'Santa Marta').sum()
print(f"✅ Registros corregidos como 'Santa Marta': {santa_marta_ok}")

# Valores nulos
nulos = df['ciudad_limpia'].isna().sum()
print(f"✅ Valores nulos en ciudad: {nulos}")

# Muestra final
print(f"\nMuestra de ciudades DESPUÉS de limpiar (primeros 20):")
print(df['ciudad_limpia'].head(20).to_string())

print(f"\nValores únicos después de limpieza (primeros 20):")
print(df['ciudad_limpia'].unique()[:20])


# ============================================================
# REEMPLAZAR COLUMNA ORIGINAL Y GUARDAR
# ============================================================
df['ciudad'] = df['ciudad_limpia']
df.drop(columns=['ciudad_limpia'], inplace=True)

df.to_csv('data/personas_limpio.csv', index=False)
print("\n")
print("=" * 60)
print("✅ Archivo guardado como: data/personas_limpio.csv")
print("=" * 60)