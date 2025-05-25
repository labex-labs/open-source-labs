# Criar Dados

Nesta etapa, você precisa criar dados usando `multivariate_normal()`. Esta função gera uma amostra aleatória de uma distribuição normal multivariada.

```python
data = np.vstack([
    multivariate_normal([10, 10], [[3, 2], [2, 3]], size=100000),
    multivariate_normal([30, 20], [[3, 1], [1, 3]], size=1000)
])
```
