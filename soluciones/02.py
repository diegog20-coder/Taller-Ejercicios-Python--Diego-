import pandas as pd
import codecs

datos = pd.read_csv('data/personas.csv')

print(datos.sample(10))

texto_original = "MARIA"

# Cifrar (ROT 13)
texto_cifrado = codecs.encode(texto_original,'rot_13')
print(f"Cifrado: {texto_cifrado}")

# MARIA = ZNEVN

condicion = datos['nombre_cifrado']=='Znevn'
datos_nuevos = datos[condicion]
print("El numero de repeticiones de Maria es:", datos_nuevos.shape[0])