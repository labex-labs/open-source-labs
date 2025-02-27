# Crear el conjunto de datos

En este paso, crearemos un conjunto de datos con una característica de entrada continua y una característica de salida continua. Utilizaremos el método `numpy.random.RandomState()` para generar números aleatorios para la característica de entrada y el método `numpy.sin()` para generar la característica de salida.

```python
rnd = np.random.RandomState(42)
X = rnd.uniform(-3, 3, size=100)
y = np.sin(X) + rnd.normal(size=len(X)) / 3
X = X.reshape(-1, 1)
```
