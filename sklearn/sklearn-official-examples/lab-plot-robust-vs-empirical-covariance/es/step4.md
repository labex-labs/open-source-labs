# Estimar la matriz de covarianza empírica

En este paso, estimamos una matriz de covarianza empírica del conjunto de datos utilizando el estimador de Estimación de Verosimilitud Máxima (MLE).

```python
# Estimate an empirical covariance matrix of the dataset
emp_cov = EmpiricalCovariance().fit(X).covariance_
```
