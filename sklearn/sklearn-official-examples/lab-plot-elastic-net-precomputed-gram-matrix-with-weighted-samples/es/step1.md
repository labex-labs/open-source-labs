# Carga del conjunto de datos y creación de pesos de muestra

Comenzamos cargando el conjunto de datos y creando algunos pesos de muestra. Utilizamos la función `make_regression` de scikit-learn para generar un conjunto de datos de regresión aleatorio con 100.000 muestras. Luego, generamos un vector de pesos lognormal y lo normalizamos para que sume el número total de muestras.

```python
import numpy as np
from sklearn.datasets import make_regression

rng = np.random.RandomState(0)

n_samples = int(1e5)
X, y = make_regression(n_samples=n_samples, noise=0.5, random_state=rng)

sample_weight = rng.lognormal(size=n_samples)
# normalize the sample weights
normalized_weights = sample_weight * (n_samples / (sample_weight.sum()))
```
