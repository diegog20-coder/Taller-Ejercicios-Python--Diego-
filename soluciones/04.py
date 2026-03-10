import csv
from collections import Counter
import codecs
import os

# Función para decodificar ROT13
def decode_rot13(text):
    return codecs.decode(text, 'rot_13')

# Ruta al archivo CSV
csv_file = os.path.join(os.path.dirname(__file__), '..', 'data', 'personas.csv')

# Contador para los nombres decodificados
name_counter = Counter()

# Leer el archivo CSV
with open(csv_file, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Decodificar el nombre cifrado
        decoded_name = decode_rot13(row['nombre_cifrado'])
        # Incrementar el contador
        name_counter[decoded_name] += 1

# Encontrar el nombre más frecuente
if name_counter:
    most_common_name, count = name_counter.most_common(1)[0]
    print(f"El nombre más frecuente es '{most_common_name}' y aparece {count} veces.")
else:
    print("No se encontraron nombres en el archivo.")