# Calcular a Probabilidade nos Dados de Teste

Calculamos a probabilidade logarítmica negativa nos dados de teste utilizando a classe `ShrunkCovariance` do módulo `sklearn.covariance` e a função `log_likelihood` do módulo `scipy.linalg`. Abrangemos uma gama de valores possíveis para o coeficiente de encolhimento e calculamos a probabilidade para cada valor.

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
