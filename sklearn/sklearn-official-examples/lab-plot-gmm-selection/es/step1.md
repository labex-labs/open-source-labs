# Generación de datos

Generamos dos componentes (cada uno contiene `n_samples`) mediante la muestra aleatoria de la distribución normal estándar devuelta por `numpy.random.randn`. Una componente se mantiene esférica pero desplazada y reescalada. La otra se deforma para tener una matriz de covarianza más general.

```python
import numpy as np

n_samples = 500
np.random.seed(0)
C = np.array([[0.0, -0.1], [1.7, 0.4]])
component_1 = np.dot(np.random.randn(n_samples, 2), C)  # general
component_2 = 0.7 * np.random.randn(n_samples, 2) + np.array([-4, 1])  # spherical

X = np.concatenate([component_1, component_2])
```
