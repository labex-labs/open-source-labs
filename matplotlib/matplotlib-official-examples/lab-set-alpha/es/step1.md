# Comprendiendo los valores alfa en Matplotlib

En este primer paso, crearemos un cuaderno de Jupyter (Jupyter Notebook) y aprenderemos cómo configurar una visualización básica con valores alfa.

## Creando tu primera celda de Jupyter Notebook

En esta celda, importaremos las bibliotecas necesarias y crearemos dos círculos superpuestos con diferentes valores alfa para demostrar la transparencia.

```python
import matplotlib.pyplot as plt
import numpy as np

# Create a figure and an axes
fig, ax = plt.subplots(figsize=(6, 4))

# Create a circle with alpha=1.0 (completely opaque)
circle1 = plt.Circle((0.5, 0.5), 0.3, color='blue', alpha=1.0, label='Opaque (alpha=1.0)')

# Create a circle with alpha=0.5 (semi-transparent)
circle2 = plt.Circle((0.7, 0.5), 0.3, color='red', alpha=0.5, label='Semi-transparent (alpha=0.5)')

# Add circles to the axes
ax.add_patch(circle1)
ax.add_patch(circle2)

# Set axis limits
ax.set_xlim(0, 1.2)
ax.set_ylim(0, 1)

# Add a title and legend
ax.set_title('Demonstrating Alpha Values in Matplotlib')
ax.legend(loc='upper right')

# Show the plot
plt.show()
```

Una vez que hayas ingresado este código en la celda, ejecútalo presionando Shift+Enter o haciendo clic en el botón "Run" de la barra de herramientas.

## Comprendiendo la salida

Deberías ver dos círculos superpuestos:

- El círculo azul de la izquierda es completamente opaco (alfa = 1.0)
- El círculo rojo de la derecha es semi-transparente (alfa = 0.5)

Observa cómo puedes ver el círculo azul a través del rojo en la zona donde se superponen. Este es el efecto de establecer el valor alfa en 0.5 para el círculo rojo.

Los valores alfa controlan la transparencia en las visualizaciones y pueden ser útiles cuando:

- Se muestran puntos de datos superpuestos
- Se resaltan ciertos elementos
- Se reduce el ruido visual en gráficos densos
- Se crean visualizaciones en capas

Continuemos explorando más aplicaciones de los valores alfa en el siguiente paso.
