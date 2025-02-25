# Crear los ejes principales

En este paso, crearemos los ejes principales y estableceremos el ayudante de cuadrícula. Utilizaremos `fig.add_subplot()` para crear los ejes principales.

```python
# Create the host axes
fig = plt.figure(figsize=(5, 5))
ax1 = fig.add_subplot(axes_class=HostAxes, grid_helper=grid_helper)
```
