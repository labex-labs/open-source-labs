# Generar datos

Primero, generamos un conjunto de datos de 125 muestras y 2 características. Ambas características se distribuyen gaussianamente con una media de 0. Sin embargo, la característica 1 tiene una desviación estándar igual a 2 y la característica 2 tiene una desviación estándar igual a 1. A continuación, reemplazamos 25 muestras con muestras atípicas gaussianas donde la característica 1 tiene una desviación estándar igual a 1 y la característica 2 tiene una desviación estándar igual a 7.

```python
import numpy as np

# for consistent results
np.random.seed(7)

n_samples = 125
n_outliers = 25
n_features = 2

# generate Gaussian data of shape (125, 2)
gen_cov = np.eye(n_features)
gen_cov[0, 0] = 2.0
X = np.dot(np.random.randn(n_samples, n_features), gen_cov)
# add some outliers
outliers_cov = np.eye(n_features)
outliers_cov[np.arange(1, n_features), np.arange(1, n_features)] = 7.0
X[-n_outliers:] = np.dot(np.random.randn(n_outliers, n_features), outliers_cov)
```
