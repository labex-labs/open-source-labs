# Calculer la vraisemblance sur les données de test

Nous calculons la log-vraisemblance négative sur les données de test en utilisant la classe `ShrunkCovariance` du module `sklearn.covariance` et la fonction `log_likelihood` du module `scipy.linalg`. Nous parcourons une plage de valeurs possibles pour le coefficient de rétrécissement et calculons la vraisemblance pour chaque valeur.

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
