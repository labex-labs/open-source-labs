# Crear datos

A continuación, crearemos algunos datos de muestra para graficar. En este ejemplo, crearemos una cuadrícula 2D de valores de x e y y los usaremos para calcular los valores de z.

```python
# invent some numbers, turning the x and y arrays into simple
# 2d arrays, which make combining them together easier.
x = np.linspace(-3, 5, 150).reshape(1, -1)
y = np.linspace(-3, 5, 120).reshape(-1, 1)
z = np.cos(x) + np.sin(y)
```
