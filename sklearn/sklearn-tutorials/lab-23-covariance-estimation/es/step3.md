# Encogimiento Ledoit-Wolf

El método de encogimiento Ledoit-Wolf proporciona un coeficiente de encogimiento óptimo que minimiza el error cuadrático medio entre la matriz de covarianza estimada y la verdadera. El paquete `sklearn.covariance` incluye una función `ledoit_wolf` que se puede utilizar para calcular el estimador Ledoit-Wolf para un conjunto de datos dado.

```python
from sklearn.covariance import ledoit_wolf

# Compute the Ledoit-Wolf estimator of the covariance matrix
ledoit_wolf_covariance_matrix = ledoit_wolf(data)[0]
```
