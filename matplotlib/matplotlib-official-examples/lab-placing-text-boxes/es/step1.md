# Creación de un Jupyter Notebook y preparación de los datos

En este primer paso, crearemos un nuevo Jupyter Notebook y prepararemos nuestros datos para la visualización.

## Creación de un nuevo cuaderno

En la primera celda del cuaderno, importemos las bibliotecas necesarias. Escriba el siguiente código y ejecútelo haciendo clic en el botón "Run" o presionando Shift+Enter:

```python
import matplotlib.pyplot as plt
import numpy as np
```

![libraries-imported](../assets/screenshot-20250306-Azb1cb3S@2x.png)

Este código importa dos bibliotecas esenciales:

- `matplotlib.pyplot`: Una colección de funciones que hace que matplotlib funcione como MATLAB
- `numpy`: Un paquete fundamental para la computación científica en Python

## Creación de datos de muestra

Ahora, creemos algunos datos de muestra que visualizaremos. En una nueva celda, ingrese y ejecute el siguiente código:

```python
# Set a random seed for reproducibility
np.random.seed(19680801)

# Generate 10,000 random numbers from a normal distribution
x = 30 * np.random.randn(10000)

# Calculate basic statistics
mu = x.mean()
median = np.median(x)
sigma = x.std()

# Display the statistics
print(f"Mean (μ): {mu:.2f}")
print(f"Median: {median:.2f}")
print(f"Standard Deviation (σ): {sigma:.2f}")
```

Cuando ejecute esta celda, debería ver una salida similar a la siguiente:

```
Mean (μ): -0.31
Median: -0.28
Standard Deviation (σ): 29.86
```

Los valores exactos pueden variar ligeramente. Hemos creado un conjunto de datos con 10,000 números aleatorios generados a partir de una distribución normal y calculado tres estadísticas importantes:

1. Media (μ): El valor promedio de todos los puntos de datos
2. Mediana: El valor central cuando los datos se ordenan
3. Desviación estándar (σ): Una medida de qué tan dispersos están los datos

Estas estadísticas se utilizarán más adelante para anotar nuestra visualización.
