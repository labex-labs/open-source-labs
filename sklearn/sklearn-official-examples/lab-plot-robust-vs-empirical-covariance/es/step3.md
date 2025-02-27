# Estimar la matriz de covarianza robusta

En este paso, estimamos una matriz de covarianza robusta del conjunto de datos utilizando el estimador de Determinante de Covarianza Mínimo (MCD).

```python
# Estimate a robust covariance matrix of the dataset
mcd = MinCovDet().fit(X)
robust_cov = mcd.covariance_
```
