# Creando datos

El siguiente paso es crear los datos para la superficie 3D. Necesitamos definir `u`, `v`, `x`, `y` y `z`. Estas variables representarán los ángulos y coordenadas necesarias para representar la superficie. La función `linspace()` de NumPy se utiliza para crear los ángulos, y la función `outer()` se utiliza para crear las coordenadas.

```python
# Make data
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = 10 * np.outer(np.cos(u), np.sin(v))
y = 10 * np.outer(np.sin(u), np.sin(v))
z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))
```
