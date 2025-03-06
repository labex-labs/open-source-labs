# Crear un gráfico básico con configuraciones predeterminadas

Ahora que hemos importado Matplotlib, creemos un gráfico simple con configuraciones predeterminadas para entender cómo se posicionan los ejes y las etiquetas de las marcas por defecto.

## Comprender los componentes de Matplotlib

En Matplotlib, los gráficos constan de varios componentes:

- **Figura (Figure)**: El contenedor general del gráfico.
- **Ejes (Axes)**: El área donde se representa los datos con su propio sistema de coordenadas.
- **Eje (Axis)**: Los objetos similares a una recta numérica que definen el sistema de coordenadas.
- **Marcas (Ticks)**: Las marcas en los ejes que indican valores específicos.
- **Etiquetas de las marcas (Tick Labels)**: Las etiquetas de texto que indican el valor en cada marca.

Por defecto, las etiquetas de las marcas del eje x aparecen en la parte inferior del gráfico.

## Crear un gráfico simple

En una nueva celda de tu cuaderno, creemos un gráfico de línea simple:

```python
# Create a figure and a set of axes
fig, ax = plt.subplots(figsize=(8, 5))

# Generate some data
x = np.arange(0, 10, 1)
y = np.sin(x)

# Plot the data
ax.plot(x, y, marker='o', linestyle='-', color='blue', label='sin(x)')

# Add a title and labels
ax.set_title('A Simple Sine Wave Plot')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis (sin(x))')

# Add a grid and legend
ax.grid(True, linestyle='--', alpha=0.7)
ax.legend()

# Display the plot
plt.show()

print("Notice that the x-axis tick labels are at the bottom of the plot by default.")
```

Cuando ejecutes este código, verás un gráfico de onda sinusoidal con las etiquetas de las marcas del eje x en la parte inferior del gráfico, que es la posición predeterminada en Matplotlib.

Tómate un momento para observar cómo está estructurado el gráfico y dónde se encuentran las etiquetas de las marcas. Esta comprensión nos ayudará a valorar los cambios que realizaremos en el siguiente paso.
