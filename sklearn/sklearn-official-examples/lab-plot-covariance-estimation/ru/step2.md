# Вычисление правдоподобия на тестовых данных

Мы вычисляем отрицательный логарифм правдоподобия на тестовых данных с использованием класса `ShrunkCovariance` из модуля `sklearn.covariance` и функции `log_likelihood` из модуля `scipy.linalg`. Мы рассчитываем ряд возможных значений коэффициента сужения и вычисляем правдоподобие для каждого значения.

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
