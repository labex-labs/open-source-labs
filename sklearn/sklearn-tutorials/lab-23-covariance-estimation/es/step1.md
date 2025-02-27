# Covarianza Empírica

La matriz de covarianza empírica es un método comúnmente utilizado para estimar la matriz de covarianza de un conjunto de datos. Se basa en el principio de estimación de máxima verosimilitud y asume que las observaciones son independientes e idénticamente distribuidas (i.i.d.). La función `empirical_covariance` en el paquete `sklearn.covariance` se puede utilizar para calcular la matriz de covarianza empírica de un conjunto de datos dado.

```python
from sklearn.covariance import empirical_covariance

# Compute the empirical covariance matrix
covariance_matrix = empirical_covariance(data)
```
