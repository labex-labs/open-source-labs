# Crear datos sintéticos

En este paso, crearemos un conjunto de datos sintético que consta de dos curvas con forma de "hacha", una negativa y una positiva, donde la amplitud de la curva positiva es ocho veces mayor que la de la curva negativa. Luego, aplicaremos `SymLogNorm` para visualizar los datos.

```python
def rbf(x, y):
    return 1.0 / (1 + 5 * ((x ** 2) + (y ** 2)))

N = 200
gain = 8
X, Y = np.mgrid[-3:3:complex(0, N), -2:2:complex(0, N)]
Z1 = rbf(X + 0.5, Y + 0.5)
Z2 = rbf(X - 0.5, Y - 0.5)
Z = gain * Z1 - Z2

shadeopts = {'cmap': 'PRGn','shading': 'gouraud'}
colormap = 'PRGn'
lnrwidth = 0.5
```
