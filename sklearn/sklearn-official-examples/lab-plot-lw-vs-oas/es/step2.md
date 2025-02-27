# Generar datos

A continuación, generaremos datos distribuidos gaussianamente con una matriz de covarianza que sigue un proceso AR(1). Utilizaremos las funciones `toeplitz` y `cholesky` de `scipy.linalg` para generar la matriz de covarianza.

```python
np.random.seed(0)

n_features = 100
r = 0.1
real_cov = toeplitz(r ** np.arange(n_features))
coloring_matrix = cholesky(real_cov)
```
