# Generar datos

Primero, necesitamos generar algunos datos de muestra que podamos utilizar para ajustar nuestros modelos. Utilizaremos numpy para generar 100 muestras, cada una con 30 características y 40 tareas. También seleccionaremos al azar 5 características relevantes y crearemos coeficientes para ellas utilizando ondas sinusoidales con frecuencia y fase aleatorias. Finalmente, agregaremos algo de ruido aleatorio a los datos.

```python
import numpy as np

rng = np.random.RandomState(42)

# Generate some 2D coefficients with sine waves with random frequency and phase
n_samples, n_features, n_tasks = 100, 30, 40
n_relevant_features = 5
coef = np.zeros((n_tasks, n_features))
times = np.linspace(0, 2 * np.pi, n_tasks)
for k in range(n_relevant_features):
    coef[:, k] = np.sin((1.0 + rng.randn(1)) * times + 3 * rng.randn(1))

X = rng.randn(n_samples, n_features)
Y = np.dot(X, coef.T) + rng.randn(n_samples, n_tasks)
```
