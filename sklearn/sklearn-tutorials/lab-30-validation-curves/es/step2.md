# Mezclar los datos

Para garantizar la aleatoriedad en nuestro análisis, vamos a mezclar el orden de las muestras en nuestro conjunto de datos.

```python
indices = np.arange(y.shape[0])
np.random.shuffle(indices)
X, y = X[indices], y[indices]
```
