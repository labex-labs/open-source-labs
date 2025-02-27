# Berechne die Wahrscheinlichkeit für die Testdaten

Wir berechnen die negative Log-Wahrscheinlichkeit für die Testdaten mit der Klasse `ShrunkCovariance` aus dem Modul `sklearn.covariance` und der Funktion `log_likelihood` aus dem Modul `scipy.linalg`. Wir erstellen einen Bereich möglicher Werte für den Shrinkage-Koeffizienten und berechnen die Wahrscheinlichkeit für jeden Wert.

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
