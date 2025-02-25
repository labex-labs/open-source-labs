# Crear datos para las elipses

Creamos los datos para nuestras elipses en forma de matrices de coordenadas x, coordenadas y, ancho, alto y ángulo.

```python
x = np.arange(10)
y = np.arange(15)
X, Y = np.meshgrid(x, y)

XY = np.column_stack((X.ravel(), Y.ravel()))

ww = X / 10.0
hh = Y / 15.0
aa = X * 9
```
