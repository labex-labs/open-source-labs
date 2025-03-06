# Creando un gráfico de barras con valores alfa variables

En este paso, utilizaremos el formato de tupla `(matplotlib_color, alpha)` para asignar diferentes niveles de transparencia a cada barra en función de su valor de datos.

## Agregando una nueva celda

Agrega una nueva celda a tu Jupyter Notebook haciendo clic en el botón "+" de la barra de herramientas o presionando "Esc" seguido de "b" mientras estás en modo de comando.

## Creando el gráfico de barras con valores alfa variables

Ingresa y ejecuta el siguiente código en la nueva celda:

```python
import matplotlib.pyplot as plt
import numpy as np

# Set a random seed for reproducibility
np.random.seed(19680801)

# Create a figure and an axes
fig, ax = plt.subplots(figsize=(10, 6))

# Generate data (using the same data as in Step 2 for comparison)
x_values = list(range(20))  # 0 to 19
y_values = np.random.randn(20)  # 20 random values from standard normal distribution

# Determine bar colors based on y-values (green for positive, red for negative)
facecolors = ['green' if y > 0 else 'red' for y in y_values]
edgecolors = facecolors  # Same color for edges

# Calculate alpha values based on the absolute y-values
# Normalize y values to get alpha values between 0.2 and 1.0
abs_y = [abs(y) for y in y_values]
max_abs_y = max(abs_y)
face_alphas = [0.2 + 0.8 * (val / max_abs_y) for val in abs_y]

# Create color-alpha tuples for each bar
colors_with_alphas = list(zip(facecolors, face_alphas))

# Create the bar chart with varying alpha values
ax.bar(x_values, y_values, color=colors_with_alphas, edgecolor=edgecolors)

# Add a title and labels
ax.set_title("Bar Chart with Varying Alpha Values Based on Bar Height")
ax.set_xlabel("X Values")
ax.set_ylabel("Y Values")

# Add a grid for better readability
ax.grid(True, linestyle='--', alpha=0.7)

# Show the plot
plt.show()
```

## Comprendiendo el código y la salida

Después de ejecutar el código, deberías ver un gráfico de barras con 20 barras. Cada barra tiene un nivel de transparencia proporcional a su valor absoluto en el eje y: las barras más altas son más opacas y las más cortas son más transparentes.

Desglosemos las partes clave del código:

1. `abs_y = [abs(y) for y in y_values]` - Esto crea una lista de los valores absolutos de todos los valores en el eje y.

2. `max_abs_y = max(abs_y)` - Encuentra el valor absoluto máximo para normalizar los datos.

3. `face_alphas = [0.2 + 0.8 * (val / max_abs_y) for val in abs_y]` - Calcula valores alfa entre 0.2 y 1.0 en función de los valores absolutos normalizados en el eje y.

4. `colors_with_alphas = list(zip(facecolors, face_alphas))` - Crea una lista de tuplas (color, alfa) emparejando cada color con su correspondiente valor alfa.

5. `ax.bar(..., color=colors_with_alphas, ...)` - Utiliza las tuplas (color, alfa) para establecer diferentes valores alfa para cada barra.

Este enfoque de utilizar niveles de transparencia variables es efectivo para:

- Resaltar los puntos de datos más significativos
- Minimizar la importancia de los puntos de datos menos significativos
- Crear una jerarquía visual basada en los valores de los datos
- Añadir una dimensión adicional de información a tu visualización

Puedes ver claramente cómo los valores alfa variables crean un efecto visual en el que la magnitud de un punto de datos se resalta tanto por la altura de la barra como por su opacidad.
