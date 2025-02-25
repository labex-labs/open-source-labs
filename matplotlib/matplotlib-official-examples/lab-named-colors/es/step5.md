# Creando un gráfico de barras

También podemos utilizar Matplotlib para crear un gráfico de barras. En este ejemplo, crearemos un gráfico de barras que muestre la cantidad de manzanas, plátanos y naranjas vendidas.

```python
import matplotlib.pyplot as plt

# datos para graficar
manzanas = 10
plátanos = 15
naranjas = 5

# creando el gráfico de barras
plt.bar(["Manzanas", "Plátanos", "Naranjas"], [manzanas, plátanos, naranjas])

# estableciendo el título
plt.title("Gráfico de barras simple")

# estableciendo la etiqueta del eje x
plt.xlabel("Frutas")

# estableciendo la etiqueta del eje y
plt.ylabel("Cantidad")

# mostrando el gráfico
plt.show()
```
