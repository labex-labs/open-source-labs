# Crear la figura y la cuadrícula externa

A continuación, crearemos la figura y la cuadrícula externa utilizando la función `add_gridspec`. Crearemos una cuadrícula de 4x4 sin espaciado entre las subtramas.

```python
fig = plt.figure(figsize=(8, 8))
outer_grid = fig.add_gridspec(4, 4, wspace=0, hspace=0)
```
