# Generar datos de muestra

Generaremos un conjunto de datos que consta de una función objetivo senoidal y ruido fuerte agregado a cada quinto dato.

```python
import numpy as np

# Generate sample data
rng = np.random.RandomState(42)
X = 5 * rng.rand(10000, 1)
y = np.sin(X).ravel()

# Add noise to targets
y[::5] += 3 * (0.5 - rng.rand(X.shape[0] // 5))

X_plot = np.linspace(0, 5, 100000)[:, None]
```
