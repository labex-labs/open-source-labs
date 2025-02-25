# Crear datos

A continuación, necesitamos crear los datos que usaremos para trazar las líneas. Usaremos `numpy` para crear una matriz bidimensional de valores de `x` e `y`.

```python
x = np.arange(100)
ys = x[:50, np.newaxis] + x[np.newaxis, :]
```
