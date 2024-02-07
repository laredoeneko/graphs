import pandas as pd

# Especifica la ruta de tu archivo CSV
archivo_csv = 'archivo.csv'

# Lee el archivo CSV en un DataFrame de pandas
df = pd.read_csv(archivo_csv)

# Nombre de la columna que deseas leer
columna_deseada = 'a'
# Accede a la columna deseada
valores_columna_a = df[columna_deseada]
# Imprime la columna deseada
print(valores_columna_a)
print (valores_columna_a[2])
columna_deseada = 'b'
# Accede a la columna deseada
valores_columna_b = df[columna_deseada]
# Imprime la columna deseada
print(valores_columna_b)
print("----------------------------")
print (valores_columna_a, valores_columna_b)

print(len(valores_columna_a))
print(len(valores_columna_b))
