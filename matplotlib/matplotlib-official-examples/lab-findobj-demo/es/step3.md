# Creando un gráfico simple

El gráfico más básico en Matplotlib es un gráfico de líneas. Puedes crear un gráfico de líneas utilizando el método `plot()`. Aquí hay un ejemplo de código que crea un gráfico de líneas simple:

```python
import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create a plot
plt.plot(x, y)

# Add labels and title
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Gráfico simple')

# Display the plot
plt.show()
```

En este código, primero definimos nuestros puntos de datos como dos listas `x` e `y`. Luego creamos un gráfico utilizando el método `plot()` y pasamos nuestros puntos de datos. Luego agregamos etiquetas a los ejes X e Y y un título al gráfico utilizando los métodos `xlabel()`, `ylabel()` y `title()`. Finalmente, mostramos el gráfico utilizando el método `show()`.
