# Gerar Dados

Em seguida, geraremos dados distribuídos gaussianamente com uma matriz de covariância que segue um processo AR(1). Usaremos as funções `toeplitz` e `cholesky` de `scipy.linalg` para gerar a matriz de covariância.

```python
np.random.seed(0)

n_features = 100
r = 0.1
real_cov = toeplitz(r ** np.arange(n_features))
coloring_matrix = cholesky(real_cov)
```
