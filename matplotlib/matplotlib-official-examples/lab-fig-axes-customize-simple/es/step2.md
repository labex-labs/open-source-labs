# Creando una figura y configurando el fondo

Crearemos una figura utilizando el método `plt.figure()`, que crea una instancia de `matplotlib.figure.Figure`. Estableceremos el color de fondo de la figura utilizando el método `rect.set_facecolor()`.

```python
fig = plt.figure()
rect = fig.patch  # una instancia de rectángulo
rect.set_facecolor('lightgoldenrodyellow')
```
