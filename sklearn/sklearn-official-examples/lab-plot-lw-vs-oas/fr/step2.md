# Générer des données

Ensuite, nous allons générer des données distribuées selon une loi normale avec une matrice de covariance qui suit un processus AR(1). Nous utiliserons les fonctions `toeplitz` et `cholesky` de `scipy.linalg` pour générer la matrice de covariance.

```python
np.random.seed(0)

n_features = 100
r = 0.1
real_cov = toeplitz(r ** np.arange(n_features))
coloring_matrix = cholesky(real_cov)
```
