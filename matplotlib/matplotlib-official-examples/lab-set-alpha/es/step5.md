# Creando una visualización combinada con diferentes técnicas de alfa

En este último paso, combinaremos múltiples técnicas para crear una visualización más compleja que demuestre tanto valores alfa uniformes como variables en un solo gráfico.

## Agregando una nueva celda

Agrega una nueva celda a tu Jupyter Notebook haciendo clic en el botón "+" de la barra de herramientas o presionando "Esc" seguido de "b" mientras estás en modo de comando.

## Creando una visualización combinada

Ingresa y ejecuta el siguiente código en la nueva celda:

```python
import matplotlib.pyplot as plt
import numpy as np

# Set a random seed for reproducibility
np.random.seed(19680801)

# Create a figure with two subplots side by side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Generate some common data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(x) * np.cos(x)

# First subplot: Fixed alpha for all lines
ax1.plot(x, y1, color='red', linewidth=2, label='sin(x)', alpha=0.7)
ax1.plot(x, y2, color='blue', linewidth=2, label='cos(x)', alpha=0.7)
ax1.plot(x, y3, color='green', linewidth=2, label='sin(x)cos(x)', alpha=0.7)

# Add title and legend to first subplot
ax1.set_title("Multiple Lines with Uniform Alpha")
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.legend()
ax1.grid(True, linestyle='--', alpha=0.5)

# Second subplot: Scatter plot with varying alpha based on y-value
sizes = np.abs(y3 * 100) + 10  # Vary point sizes based on y3
colors = y3  # Use y3 values for coloring

# Calculate varying alpha values between 0.3 and 1.0 based on absolute y3 values
alphas = 0.3 + 0.7 * (np.abs(y3) / max(np.abs(y3)))

# Create a scatter plot with varying sizes, colors, and alphas
scatter = ax2.scatter(x, y3, s=sizes, c=colors, cmap='viridis',
                     alpha=alphas)

# Add title and labels to second subplot
ax2.set_title("Scatter Plot with Varying Alpha Based on Y-Value")
ax2.set_xlabel("x")
ax2.set_ylabel("sin(x)cos(x)")
ax2.grid(True, linestyle='--', alpha=0.5)

# Add a colorbar to the second subplot
cbar = plt.colorbar(scatter, ax=ax2)
cbar.set_label('Value of sin(x)cos(x)')

# Adjust layout and show the plot
plt.tight_layout()
plt.show()
```

## Comprendiendo el código y la salida

Después de ejecutar el código, deberías ver una figura con dos subgráficos uno al lado del otro:

1. **Subgráfico izquierdo (Alfa uniforme)**: Muestra tres funciones trigonométricas trazadas con el mismo valor alfa (0.7).

2. **Subgráfico derecho (Alfa variable)**: Muestra un diagrama de dispersión donde:
   - La coordenada x es el valor de entrada.
   - La coordenada y es sin(x)cos(x).
   - El tamaño de cada punto varía en función del valor absoluto de y.
   - El color de cada punto varía en función del valor de y.
   - El alfa (transparencia) de cada punto varía en función del valor absoluto de y.

Analicemos las partes clave del código:

1. `fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))` - Crea una figura con dos subgráficos uno al lado del otro.

2. Para el primer subgráfico:
   - `ax1.plot(..., alpha=0.7)` - Utiliza un valor alfa uniforme para las tres líneas.

3. Para el segundo subgráfico:
   - `alphas = 0.3 + 0.7 * (np.abs(y3) / max(np.abs(y3)))` - Calcula valores alfa variables entre 0.3 y 1.0.
   - `ax2.scatter(..., alpha=alphas)` - Utiliza valores alfa variables para los puntos de dispersión.

Esta combinación de técnicas demuestra cómo los valores alfa se pueden utilizar de diversas maneras para mejorar las visualizaciones:

- **Alfa uniforme** es útil cuando necesitas mostrar múltiples elementos superpuestos con igual importancia.

- **Alfa variable** es útil cuando quieres resaltar ciertos puntos de datos en función de sus valores.

Al dominar estas técnicas, puedes crear visualizaciones de datos más efectivas y visualmente atractivas.
