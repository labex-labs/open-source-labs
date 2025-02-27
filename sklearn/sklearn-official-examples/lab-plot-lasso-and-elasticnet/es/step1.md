# Generar un conjunto de datos sintético

Primero, generamos un conjunto de datos donde el número de muestras es menor que el número total de características. Esto conduce a un sistema subdeterminado, es decir, la solución no es única y no podemos aplicar un método de mínimos cuadrados ordinarios por sí solo. La regularización introduce un término de penalización en la función objetivo, lo que modifica el problema de optimización y puede ayudar a aliviar la naturaleza subdeterminada del sistema. Generaremos un objetivo `y` que sea una combinación lineal con signos alternados de señales senoidales. Solo las 10 frecuencias más bajas de las 100 en `X` se utilizan para generar `y`, mientras que el resto de las características no son informativas. Esto resulta en un espacio de características disperso de alta dimensión, donde es necesaria cierta penalización L1.

```python
import numpy as np

rng = np.random.RandomState(0)
n_samples, n_features, n_informative = 50, 100, 10
time_step = np.linspace(-2, 2, n_samples)
freqs = 2 * np.pi * np.sort(rng.rand(n_features)) / 0.01
X = np.zeros((n_samples, n_features))

for i in range(n_features):
    X[:, i] = np.sin(freqs[i] * time_step)

idx = np.arange(n_features)
true_coef = (-1) ** idx * np.exp(-idx / 10)
true_coef[n_informative:] = 0  # sparsify coef
y = np.dot(X, true_coef)

# introduce random phase using numpy.random.random_sample
# add some gaussian noise using numpy.random.normal
for i in range(n_features):
    X[:, i] = np.sin(freqs[i] * time_step + 2 * (rng.random_sample() - 0.5))
    X[:, i] += 0.2 * rng.normal(0, 1, n_samples)

y += 0.2 * rng.normal(0, 1, n_samples)

# split the data into train and test sets using train_test_split from sklearn
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, shuffle=False)
```
