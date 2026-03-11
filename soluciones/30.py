import pandas as pd

# ============================================================
# CARGA DEL ARCHIVO YA LIMPIO
# ============================================================
df = pd.read_csv('data/personas_limpio.csv')

#Nombre de Jose y apellido Garcia cifrados con ROT13

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

# Cifrar el nombre 'Jose' y el apellido 'Garcia' con ROT13
nombre_cifrado_jose = rot13('Jose')
apellido_cifrado_garcia = rot13('Garcia')

# Filtrar el DataFrame por nombre y apellido cifrados
df_jose_garcia = df[
    (df['nombre_cifrado'] == nombre_cifrado_jose) &
    (df['apellido_cifrado'] == apellido_cifrado_garcia)
]

# Contar el número de registros
num_jose_garcia = len(df_jose_garcia)

print(f"Número de registros con nombre '{rot13(nombre_cifrado_jose)}' y apellido '{rot13(apellido_cifrado_garcia)}': {num_jose_garcia}")