import pandas as pd
import codecs

datos = pd.read_csv('data/personas.csv')

print(datos.sample(10))

