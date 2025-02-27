# Creando una malla para graficar

Ahora, crearemos una malla para graficar. La malla se utilizará para graficar las probabilidades predichas para cada punto de la malla. También definiremos el tamaño del paso para la malla.

```python
h = 0.02  # tamaño del paso en la malla

x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
```
