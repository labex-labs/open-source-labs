# Creando diferentes tipos de gráficos

Matplotlib admite una amplia variedad de tipos de gráficos, incluyendo gráficos de líneas, gráficos de dispersión, gráficos de barras y más. Aquí hay un ejemplo de código que crea un gráfico de dispersión:

```python
import matplotlib.pyplot as plt
import numpy as np

# Generate some random data
x = np.random.rand(50)
y = np.random.rand(50)
colors = np.random.rand(50)
sizes = 1000 * np.random.rand(50)

# Create a scatter plot
plt.scatter(x, y, c=colors, s=sizes, alpha=0.5)

# Add labels and title
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Gráfico de dispersión')

# Display the plot
plt.show()
```

En este código, utilizamos el método `scatter()` para crear un gráfico de dispersión. Generamos algunos datos aleatorios utilizando la biblioteca NumPy y los pasamos al método `scatter()`. También utilizamos el parámetro `c` para especificar los colores de los puntos de datos, el parámetro `s` para especificar los tamaños de los puntos de datos y el parámetro `alpha` para especificar la transparencia de los puntos de datos.
