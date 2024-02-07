import pandas as pd
import matplotlib.pyplot as plt

# Cargamos los datos desde el archivo CSV
# formato del archivo
#   a,b,
#   1,1000
#   2,3000
#   3,4000
#   4,5000
#   5,6000




archivo_csv = "data.csv"  # Reemplaza con la ruta real de tu archivo
datos = pd.read_csv("archivo.csv", sep=",")

# Supongamos que tus columnas se llaman "a" y "b"
columna_a = datos["a"]
columna_b = datos["b"]

# Crear un gráfico de dispersión
plt.plot(columna_a, columna_b,  marker='o', linestyle='-')
#plt.scatter(columna_a, columna_b)
plt.xlabel("Etiqueta para el eje X")
plt.ylabel("Etiqueta para el eje Y")
plt.title("Gráfico de dispersión a vs b")
plt.grid(True)
plt.show()