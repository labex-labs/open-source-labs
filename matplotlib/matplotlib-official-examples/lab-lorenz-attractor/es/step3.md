# Configurar los parámetros iniciales

Configuramos los parámetros iniciales para la simulación, incluyendo el paso de tiempo `dt`, el número de pasos `num_steps` y los valores iniciales para `x`, `y` y `z`.

```python
dt = 0.01
num_steps = 10000

xyzs = np.empty((num_steps + 1, 3))  # Need one more for the initial values
xyzs[0] = (0., 1., 1.05)  # Set initial values
```
