# Calcular la verosimilitud en los datos de prueba

Calculamos la log-verosimilitud negativa en los datos de prueba utilizando la clase `ShrunkCovariance` del módulo `sklearn.covariance` y la función `log_likelihood` del módulo `scipy.linalg`. Recorremos una gama de valores posibles del coeficiente de encogimiento y calculamos la verosimilitud para cada valor.

```python
from sklearn.covariance import ShrunkCovariance, empirical_covariance, log_likelihood
from scipy import linalg

shrinkages = np.logspace(-2, 0, 30)
negative_logliks = [
    -ShrunkCovariance(shrinkage=s).fit(X_train).score(X_test) for s in shrinkages
]

real_cov = np.dot(coloring_matrix.T, coloring_matrix)
emp_cov = empirical_covariance(X_train)
loglik_real = -log_likelihood(emp_cov, linalg.inv(real_cov))
```
