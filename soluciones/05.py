import csv
from collections import Counter
import codecs


def rot13(s: str) -> str:
    """Devuelve la cadena decodificada/encodificada en ROT13."""
    # codecs.decode funciona para rot13 también
    return codecs.decode(s, "rot_13")


def main():
    # lee el archivo CSV, decodifica apellidos en rot13 y cuenta apariciones
    contador = Counter()
    with open("data/personas.csv", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            apellido = row.get("apellido_cifrado", "").strip()
            if apellido:
                apellido = rot13(apellido)
                contador[apellido] += 1

    if contador:
        apellido_mas_comun, veces = contador.most_common(1)[0]
        print(f"El apellido más frecuente es '{apellido_mas_comun}' y aparece {veces} veces.")
    else:
        print("No se encontraron apellidos en el archivo.")


if __name__ == "__main__":
    main()
