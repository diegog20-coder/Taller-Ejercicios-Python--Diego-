import pandas as pd
import re
from collections import Counter

# ============================================================
# CARGA DEL ARCHIVO YA LIMPIO
# ============================================================
df = pd.read_csv('data/personas_limpio.csv')

print("=" * 60)
print("ANÁLISIS DE COLUMNA SALARIO")
print("=" * 60)
print(f"Total de registros: {len(df)}")

# ============================================================
# PASO 1: REGISTROS CON CARACTERES NO NUMÉRICOS
# ============================================================
con_no_numericos = df['salario'].astype(str).str.contains(r'[^0-9]', na=False).sum()

print(f"\n📋 Registros con caracteres NO numéricos: {con_no_numericos}")
print(f"   ({(con_no_numericos / len(df) * 100):.2f}% del total)")

# ============================================================
# PASO 2: ¿QUÉ CARACTERES NO NUMÉRICOS EXISTEN?
# ============================================================
todos_caracteres = ''.join(df['salario'].astype(str).tolist())
caracteres_no_num = [c for c in todos_caracteres if not c.isdigit()]
conteo_caracteres = Counter(caracteres_no_num)

print(f"\n📋 Caracteres NO numéricos encontrados y su frecuencia:")
print("-" * 45)
for caracter, cantidad in sorted(conteo_caracteres.items(), key=lambda x: -x[1]):
    if caracter == ' ':
        print(f"  ESPACIO              : {cantidad} veces")
    elif caracter == '.':
        print(f"  PUNTO       '.'      : {cantidad} veces")
    elif caracter == ',':
        print(f"  COMA        ','      : {cantidad} veces")
    else:
        print(f"  '{caracter}'                  : {cantidad} veces")
print("-" * 45)

# ============================================================
# PASO 3: MUESTRA DE SALARIOS CON CARACTERES EXTRAÑOS
# ============================================================
mask = df['salario'].astype(str).str.contains(r'[^0-9.]', na=False)
muestra = df[mask]['salario'].head(30)

print(f"\n📋 Muestra de salarios con caracteres no numéricos (primeros 30):")
print("-" * 45)
for val in muestra:
    print(f"  '{val}'")
print("-" * 45)

# ============================================================
# PASO 4: RESUMEN DE PATRONES DETECTADOS
# ============================================================
salarios_str = df['salario'].astype(str)

tiene_letras   = salarios_str.str.contains(r'[a-zA-Z]', na=False).sum()
tiene_puntos   = salarios_str.str.contains(r'\.', na=False).sum()
tiene_comas    = salarios_str.str.contains(r',', na=False).sum()
tiene_espacios = salarios_str.str.contains(r'\s', na=False).sum()
tiene_signos   = salarios_str.str.contains(r'[\$\-\+\*\/]', na=False).sum()
tiene_otros    = salarios_str.str.contains(r'[^0-9a-zA-Z\s\.\,\$\-\+]', na=False).sum()

print(f"\n📊 Resumen de patrones detectados:")
print("-" * 45)
print(f"  Con letras           : {tiene_letras:>7} registros")
print(f"  Con puntos    '.'    : {tiene_puntos:>7} registros")
print(f"  Con comas     ','    : {tiene_comas:>7} registros")
print(f"  Con espacios         : {tiene_espacios:>7} registros")
print(f"  Con signos ($,-,+)   : {tiene_signos:>7} registros")
print(f"  Con otros caracteres : {tiene_otros:>7} registros")
print("-" * 45)

# Mostrar qué letras específicas aparecen (clave para el siguiente paso)
letras_encontradas = set(re.findall(r'[a-zA-Z]', ''.join(salarios_str.tolist())))
if letras_encontradas:
    print(f"\n⚠️  Letras específicas encontradas en salarios:")
    print(f"  {sorted(letras_encontradas)}")
    print(f"\n  → Estas letras pueden estar reemplazando números.")
    print(f"  → Ejemplo: 'L' puede ser '1', 'O' puede ser '0', etc.")
    print(f"  → Revisar antes de aplicar la limpieza.")

print("\n")
print("=" * 60)
print("✅ Análisis completo. Revisar resultados antes de limpiar.")
print("=" * 60)