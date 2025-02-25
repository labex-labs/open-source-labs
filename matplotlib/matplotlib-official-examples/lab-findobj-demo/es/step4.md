# Personalizando el gráfico

Matplotlib ofrece una amplia variedad de opciones de personalización para los gráficos. Aquí hay un ejemplo de código que personaliza nuestro gráfico de líneas simple:

```python
import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create a plot
plt.plot(x, y, color='red', linewidth=2, linestyle='--', marker='o', markersize=8, markerfacecolor='yellow')

# Add labels and title
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Gráfico personalizado')

# Display the plot
plt.show()
```

En este código, utilizamos varios parámetros del método `plot()` para personalizar el gráfico. Cambiamos el color de la línea a rojo, el ancho de línea a 2, el estilo de línea a discontinuo (`--`), el marcador a un círculo (`o`), el tamaño del marcador a 8 y el color de la cara del marcador a amarillo.
