# Creando un gráfico de barras con un valor alfa uniforme

En este paso, crearemos un gráfico de barras donde todas las barras tienen el mismo nivel de transparencia utilizando el argumento de palabra clave `alpha`.

## Agregando una nueva celda

Agrega una nueva celda a tu Jupyter Notebook haciendo clic en el botón "+" de la barra de herramientas o presionando "Esc" seguido de "b" mientras estás en modo de comando.

## Creando el gráfico de barras con un alfa uniforme

Ingresa y ejecuta el siguiente código en la nueva celda:

```python
import matplotlib.pyplot as plt
import numpy as np

# Set a random seed for reproducibility
np.random.seed(19680801)

# Create a figure and an axes
fig, ax = plt.subplots(figsize=(10, 6))

# Generate data
x_values = list(range(20))  # 0 to 19
y_values = np.random.randn(20)  # 20 random values from standard normal distribution

# Determine bar colors based on y-values (green for positive, red for negative)
facecolors = ['green' if y > 0 else 'red' for y in y_values]
edgecolors = facecolors  # Same color for edges

# Create the bar chart with alpha=0.5 for all bars
ax.bar(x_values, y_values, color=facecolors, edgecolor=edgecolors, alpha=0.5)

# Add a title and labels
ax.set_title("Bar Chart with Uniform Alpha Value (alpha=0.5)")
ax.set_xlabel("X Values")
ax.set_ylabel("Y Values")

# Add a grid for better readability
ax.grid(True, linestyle='--', alpha=0.7)

# Show the plot
plt.show()
```

## Comprendiendo el código y la salida

Después de ejecutar el código, deberías ver un gráfico de barras con 20 barras. Cada barra es verde (valor positivo en el eje y) o roja (valor negativo en el eje y) con el mismo nivel de transparencia (alfa = 0.5).

Desglosemos las partes clave:

1. `np.random.seed(19680801)` - Esto asegura que los números aleatorios generados sean los mismos cada vez que ejecutas el código.

2. `x_values = list(range(20))` - Crea una lista de enteros del 0 al 19 para el eje x.

3. `y_values = np.random.randn(20)` - Genera 20 valores aleatorios de una distribución normal estándar para el eje y.

4. `facecolors = ['green' if y > 0 else 'red' for y in y_values]` - Esta comprensión de lista asigna el color verde a los valores positivos y el rojo a los valores negativos.

5. `ax.bar(..., alpha=0.5)` - La parte clave que establece un valor alfa uniforme de 0.5 para todas las barras.

El valor alfa uniforme hace que todas las barras sean igualmente transparentes, lo cual puede ser útil cuando se desea:

- Mostrar las líneas de la cuadrícula de fondo a través de las barras
- Crear una visualización más sutil
- Reducir igualmente la dominancia visual de todos los elementos

En el siguiente paso, exploraremos cómo establecer diferentes valores alfa para diferentes barras.
