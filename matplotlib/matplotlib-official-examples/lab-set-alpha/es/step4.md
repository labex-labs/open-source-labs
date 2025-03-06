# Creando un diagrama de dispersión con valores alfa

En este paso, aplicaremos nuestro conocimiento de los valores alfa para crear un diagrama de dispersión. Esto demostrará cómo la transparencia puede ayudar a visualizar la densidad de datos en diagramas de dispersión con puntos superpuestos.

## Agregando una nueva celda

Agrega una nueva celda a tu Jupyter Notebook haciendo clic en el botón "+" de la barra de herramientas o presionando "Esc" seguido de "b" mientras estás en modo de comando.

## Creando un diagrama de dispersión con transparencia

Ingresa y ejecuta el siguiente código en la nueva celda:

```python
import matplotlib.pyplot as plt
import numpy as np

# Set a random seed for reproducibility
np.random.seed(19680801)

# Create a figure and an axes
fig, ax = plt.subplots(figsize=(10, 6))

# Create two clusters of points
cluster1_x = np.random.normal(0.3, 0.15, 500)
cluster1_y = np.random.normal(0.3, 0.15, 500)

cluster2_x = np.random.normal(0.7, 0.15, 500)
cluster2_y = np.random.normal(0.7, 0.15, 500)

# Combine the clusters
x = np.concatenate([cluster1_x, cluster2_x])
y = np.concatenate([cluster1_y, cluster2_y])

# Create a scatter plot with alpha=0.5
scatter = ax.scatter(x, y, s=30, c='blue', alpha=0.5)

# Add a title and labels
ax.set_title("Scatter Plot with Alpha=0.5 Showing Data Density")
ax.set_xlabel("X")
ax.set_ylabel("Y")

# Set axis limits
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

# Add a grid
ax.grid(True, linestyle='--', alpha=0.7)

# Show the plot
plt.show()
```

## Comprendiendo el código y la salida

Después de ejecutar el código, deberías ver un diagrama de dispersión con dos grupos de puntos. Cada punto tiene un nivel de transparencia de 0.5, lo que te permite ver dónde se superponen los puntos.

Desglosemos las partes clave del código:

1. `cluster1_x = np.random.normal(0.3, 0.15, 500)` - Genera 500 coordenadas x aleatorias que siguen una distribución normal con media 0.3 y desviación estándar 0.15.

2. `cluster1_y = np.random.normal(0.3, 0.15, 500)` - Genera 500 coordenadas y aleatorias para el primer grupo.

3. `cluster2_x` y `cluster2_y` - De manera similar, generan coordenadas para el segundo grupo centrado en (0.7, 0.7).

4. `ax.scatter(..., alpha=0.5)` - Crea un diagrama de dispersión con puntos al 50% de opacidad.

Las ventajas de usar el valor alfa en diagramas de dispersión incluyen:

1. **Visualización de la densidad**: Las áreas donde muchos puntos se superponen parecen más oscuras, lo que revela la densidad de los datos.

2. **Reducción de la superposición de puntos**: Sin transparencia, los puntos superpuestos se ocultarían completamente entre sí.

3. **Reconocimiento de patrones**: La transparencia ayuda a identificar grupos y patrones en los datos.

Observa cómo las áreas con más puntos superpuestos parecen más oscuras en la visualización. Esta es una forma poderosa de visualizar la densidad de los datos sin necesidad de técnicas adicionales como la estimación de densidad.
