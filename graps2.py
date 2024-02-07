import csv
import matplotlib.pyplot as plt

def plot_csv(file_path, x_column, y_column):
    # Inicializar listas para almacenar los datos
    print({file_path},{x_column},{y_column})
    x_data = []
    y_data = []

    # Leer el archivo CSV y extraer los datos de las columnas especificadas
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        print(csv_reader)
        for row in csv_reader:
           x_data.append((row[x_column]))
           # x_data.append(float(row[x_column]))
           # y_data.append(float(row[y_column]))
           print(row)
    # Crear el gráfico
    plt.plot(x_data, y_data, marker='o', linestyle='-')
    plt.title('Gráfico a partir de un archivo CSV')
    plt.xlabel(x_column)
    plt.ylabel(y_column)

    # Mostrar el gráfico
    plt.show()

# Ruta del archivo CSV y nombre de las columnas
archivo_csv = 'data.csv'
columna_x = 'Columna_X'
columna_y = 'Columna_Y'

# Llamar a la función para crear el gráfico
plot_csv(archivo_csv, columna_x, columna_y)