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

#============================================================
#Aplicar un filtro a la columna salario para contar cuántos registros contienen caracteres especiales como [ ] o .

salario_str = df['salario'].astype(str)
mask_special_chars = salario_str.str.contains(r'[\[\]\.]', na=False)
print(f"Number of records with special characters ([, ], .): {mask_special_chars.sum()}")

##

salarios_filtrados = df[mask_special_chars][['salario']]
print("Salarios con caracteres especiales (']', '[', '.'):")
print(salarios_filtrados)

##
# Mapear 'l' a '1' y 'O' a '0'
df['salario'] = df['salario'].astype(str).str.replace('l', '1', regex=False)
df['salario'] = df['salario'].astype(str).str.replace('L', '1', regex=False)
df['salario'] = df['salario'].astype(str).str.replace('O', '0', regex=False)
df['salario'] = df['salario'].astype(str).str.replace('o', '0', regex=False)
print("✔ 'l' y 'O' mapeados a '1' y '0' respectivamente.")

# Eliminar 'aprox.' y 'aprox' (con y sin punto)
df['salario'] = df['salario'].astype(str).str.replace(r'aprox\.?\\s*', '', regex=True, flags=re.IGNORECASE)
print("✔ 'aprox.' eliminado.")

# Eliminar todos los caracteres que no sean dígitos, puntos o comas
df['salario'] = df['salario'].astype(str).str.replace(r'[^0-9.,]', '', regex=True)
print("✔ Caracteres no numéricos restantes eliminados.")

# normalizar el separador decimal y de miles
def normalize_salario(salario_str):
    if isinstance(salario_str, (int, float)):
        return str(salario_str)
    
    salario_str = str(salario_str).strip()
    
    # Si hay coma y punto, asumimos punto miles, coma decimal
    if ',' in salario_str and '.' in salario_str:
        # Eliminar miles y reemplazar coma por punto
        if salario_str.rfind(',') > salario_str.rfind('.'): # e.g. 1.234.567,89
            salario_str = salario_str.replace('.', '').replace(',', '.')
        else: # e.g. 1,234,567.89
            salario_str = salario_str.replace(',', '')
    # Si solo hay coma, asumimos que es decimal
    elif ',' in salario_str:
        salario_str = salario_str.replace(',', '.')
        
    return salario_str

df['salario'] = df['salario'].apply(normalize_salario)
print("✔ Separadores decimales y de miles normalizados.")

# Convertir a tipo numérico
df['salario'] = pd.to_numeric(df['salario'], errors='coerce')
print("✔ Columna 'salario' convertida a tipo numérico.")

# Verificar la limpieza final
print("\nPrimeros 10 salarios después de la limpieza:")
print(df['salario'].head(10))
print(f"\nTipo de dato de la columna 'salario': {df['salario'].dtype}")

# Verificar si aún quedan valores no numéricos (NaN)
non_numeric_count = df['salario'].isnull().sum()
if non_numeric_count > 0:
    print(f"\n⚠️ Todavía quedan {non_numeric_count} valores no numéricos (NaN) después de la limpieza. Puede que necesiten un manejo adicional.")
else:
    print("\n✅ La columna 'salario' está completamente numérica.")

    ## crear máscara boleana para identificar los valores en la columna salario que son mayores que cero pero menores que 1
    mask_salarios_entre_0_y_1 = (df['salario'] > 0) & (df['salario'] < 1)
print(f"Número de salarios entre 0 y 1: {mask_salarios_entre_0_y_1.sum()}")

## Reemplazar los valores con NaN y verificar la limpieza
import numpy as np
print("✔ numpy importado como np.")

## la biblioteca numpy ya esta importada por lo que el siguiente paso es aplicar el reemplazo np.nan usando la mascara creada anteriormente para los valores entre 0 y 1

df.loc[mask_salarios_entre_0_y_1, 'salario'] = np.nan

print("\nPrimeros 10 salarios después de la limpieza de valores entre 0 y 1:")
print(df['salario'].head(10))
print(f"\nTipo de dato de la columna 'salario': {df['salario'].dtype}")

# Verificar si aún quedan valores no numéricos (NaN)
non_numeric_count_after_step = df['salario'].isnull().sum()
print(f"\nTotal de valores NaN en la columna 'salario' después de este paso: {non_numeric_count_after_step}")

## guardar el DataFrame limpio en un nuevo archivo CSV
df.to_csv('data/personas_limpio.csv', index=False)
print("✔ DataFrame 'df' guardado exitosamente en '/'data/personas_limpio.csv'")


