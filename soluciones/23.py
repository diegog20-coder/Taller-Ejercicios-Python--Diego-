import pandas as pd

# ============================================================
# CARGA DEL ARCHIVO YA LIMPIO
# ============================================================
df = pd.read_csv('data/personas_limpio.csv')

#Descifrar el nombre de Carlos
def rot13(text):
    result = ""
    for char in text:
        if 'a' <= char <= 'z':
            start = ord('a')
            result += chr((ord(char) - start + 13) % 26 + start)
        elif 'A' <= char <= 'Z':
            start = ord('A')
            result += chr((ord(char) - start + 13) % 26 + start)
        else:
            result += char
    return result

nombre_cifrado_carlos = rot13('Carlos')
print(f"El nombre 'Carlos' cifrado con ROT13 es: '{nombre_cifrado_carlos}'")

## Número de registros con el nombre cifrado y que vivan en Cali
df_filtrado = df[(df['nombre_cifrado'] == nombre_cifrado_carlos) & (df['ciudad'] == 'Cali')]

num_registros = len(df_filtrado)
print(f"Número de registros con nombre '{rot13(nombre_cifrado_carlos)}' y ciudad 'Cali': {num_registros}")