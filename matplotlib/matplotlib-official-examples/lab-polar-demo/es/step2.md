# Generar los datos

A continuación, necesitamos generar los datos para el gráfico de líneas. Utilizaremos la librería `numpy` para generar una matriz de valores para `r` y `theta`.

```python
r = np.arange(0, 2, 0.01)
theta = 2 * np.pi * r
```
