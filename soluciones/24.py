import pandas as pd

# ============================================================
# CARGA DEL ARCHIVO YA LIMPIO
# ============================================================
df = pd.read_csv('data/personas_limpio.csv')

# Nombre cifrado de Ana y profesión de Médico
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

# Cifrar el nombre 'Ana' con ROT13
nombre_cifrado_ana = rot13('Ana')

# Filtrar el DataFrame por nombre cifrado y profesión
df_ana_medico = df[(df['nombre_cifrado'] == nombre_cifrado_ana) & (df['profesion'] == 'Medico')]

# Contar el número de registros
num_ana_medico = len(df_ana_medico)

print(f"Número de registros con nombre '{rot13(nombre_cifrado_ana)}' y profesión 'Medico': {num_ana_medico}")



