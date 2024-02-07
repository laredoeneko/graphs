import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")

fechas = data["Fecha"]
valor1 = data["Valor1"]
valor2 = data["Valor2"]

plt.plot(fechas, valor1, color="red", marker="o", label="Valor 1")
plt.plot(fechas, valor2, color="blue", marker="x", label="Valor 2")

plt.title("Gráfica de Valores")
plt.xlabel("Fecha")
plt.ylabel("Valor")

plt.legend()
plt.savefig("grafica.png")
plt.show()