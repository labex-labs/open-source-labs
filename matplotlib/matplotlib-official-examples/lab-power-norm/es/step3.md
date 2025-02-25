# Crear datos

En este paso, debe crear datos utilizando `multivariate_normal()`. Esta función genera una muestra aleatoria de una distribución normal multivariada.

```python
data = np.vstack([
    multivariate_normal([10, 10], [[3, 2], [2, 3]], size=100000),
    multivariate_normal([30, 20], [[3, 1], [1, 3]], size=1000)
])
```
