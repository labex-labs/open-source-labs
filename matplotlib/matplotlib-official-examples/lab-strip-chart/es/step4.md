# Crear la función emisor

La función emisor genera los datos que se pasarán al método de actualización. En este caso, estamos generando datos aleatorios con una probabilidad de 0.1.

```python
def emitter(p=0.1):
    while True:
        v = np.random.rand()
        if v > p:
            yield 0.
        else:
            yield np.random.rand()
```
