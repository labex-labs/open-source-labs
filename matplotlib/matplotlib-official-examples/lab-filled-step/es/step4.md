# Configurar la función de histograma con intervalos fijos

Configuraremos una función de histograma con intervalos fijos utilizando `numpy.histogram`. Crearemos 20 intervalos que van desde -3 hasta 3.

```python
edges = np.linspace(-3, 3, 20, endpoint=True)
hist_func = partial(np.histogram, bins=edges)
```
