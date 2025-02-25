# Creando una matriz aleatoria

A continuación, crearemos una matriz aleatoria con dimensiones (20, 20) utilizando la función `numpy.random.randn`. También estableceremos algunos elementos en cero para crear una matriz dispersa.

```python
np.random.seed(19680801)
x = np.random.randn(20, 20)
x[5, :] = 0.
x[:, 12] = 0.
```
