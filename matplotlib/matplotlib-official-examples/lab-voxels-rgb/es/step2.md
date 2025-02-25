# Definiendo las coordenadas y los colores

A continuación, necesitamos definir las coordenadas y los colores para el gráfico. En este ejemplo, usaremos la función `np.indices` para crear una cuadrícula de valores de 17x17x17 para los colores RGB.

```python
r, g, b = np.indices((17, 17, 17)) / 16.0
```

También definiremos una función `midpoints` para encontrar los puntos medios entre los valores de la cuadrícula. Esto se usará más adelante para crear la esfera.

```python
def midpoints(x):
    sl = ()
    for _ in range(x.ndim):
        x = (x[sl + np.index_exp[:-1]] + x[sl + np.index_exp[1:]]) / 2.0
        sl += np.index_exp[:]
    return x
```
