# Generar datos de muestra

Primero, generamos un conjunto de datos de muestra compuesto por 40 valores aleatorios entre 0 y 5. Luego, calculamos la función seno de cada valor y agregamos ruido a cada quinto valor.

```python
import numpy as np

# Generate sample data
X = np.sort(5 * np.random.rand(40, 1), axis=0)
y = np.sin(X).ravel()

# add noise to targets
y[::5] += 3 * (0.5 - np.random.rand(8))
```
