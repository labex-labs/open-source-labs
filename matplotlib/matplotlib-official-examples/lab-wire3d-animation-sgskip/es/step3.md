# Crear una malla (Meshgrid)

El tercer paso es crear una malla utilizando `linspace`.

```python
xs = np.linspace(-1, 1, 50)
ys = np.linspace(-1, 1, 50)
X, Y = np.meshgrid(xs, ys)
```
