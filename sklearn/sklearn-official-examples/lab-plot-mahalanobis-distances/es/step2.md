# Ajustar los estimadores de covarianza MCD y MLE a los datos

Ajustaremos los estimadores de covarianza basados en MCD y MLE a nuestros datos e imprimiremos las matrices de covarianza estimadas. Tenga en cuenta que la varianza estimada de la característica 2 es mucho más alta con el estimador basado en MLE (7.5) que con el estimador robusto MCD (1.2). Esto muestra que el estimador robusto basado en MCD es mucho más resistente a las muestras atípicas, que se diseñaron para tener una varianza mucho mayor en la característica 2.

```python
from sklearn.covariance import EmpiricalCovariance, MinCovDet

# fit a MCD robust estimator to data
robust_cov = MinCovDet().fit(X)
# fit a MLE estimator to data
emp_cov = EmpiricalCovariance().fit(X)
print(
    "Estimated covariance matrix:\nMCD (Robust):\n{}\nMLE:\n{}".format(
        robust_cov.covariance_, emp_cov.covariance_
    )
)
```
