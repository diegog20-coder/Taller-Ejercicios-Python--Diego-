import pandas as pd

RUTA_ARCHIVO='data/personas.csv'

datos = pd.read_csv(RUTA_ARCHIVO)
## print(datos.head())

def decifrar_palabra(palabra_cifrada):
    import codecs
    nueva_palabra = codecs.encode(palabra_cifrada,'rot_13')
    return nueva_palabra

datos['nombre'] = datos['nombre_cifrado'].apply(decifrar_palabra)
condicion = datos ['nombre']=="Gabriel"
print("Gabriel aparece:",datos[condicion].shape[0])
