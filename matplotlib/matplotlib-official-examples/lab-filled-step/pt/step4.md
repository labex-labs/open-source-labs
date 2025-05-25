# Configurar a função do histograma para bins fixos

Configuraremos uma função de histograma com bins fixos usando `numpy.histogram`. Criaremos 20 bins variando de -3 a 3.

```python
edges = np.linspace(-3, 3, 20, endpoint=True)
hist_func = partial(np.histogram, bins=edges)
```
