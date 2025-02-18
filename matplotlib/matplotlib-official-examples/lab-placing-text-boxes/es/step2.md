# Crear datos

Para este ejemplo, crearemos un conjunto de datos aleatorio utilizando `numpy.random.randn()`.

```python
np.random.seed(19680801)
x = 30*np.random.randn(10000)
mu = x.mean()
median = np.median(x)
sigma = x.std()
```
