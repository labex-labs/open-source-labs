# Crear datos

Crearemos una matriz de numpy `x` que contiene 500 valores espaciados uniformemente entre 0 y 3π. También crearemos otra matriz de numpy `y` que contiene el seno de los valores en `x`. Finalmente, crearemos una matriz de numpy `dydx` que contiene la primera derivada de `y`.

```python
x = np.linspace(0, 3 * np.pi, 500)
y = np.sin(x)
dydx = np.cos(0.5 * (x[:-1] + x[1:]))
```
