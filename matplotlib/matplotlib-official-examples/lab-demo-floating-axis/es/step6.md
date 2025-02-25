# Establecer los límites y mostrar la cuadrícula

En este paso, estableceremos los límites para los ejes y mostraremos la cuadrícula. Utilizaremos `set_aspect()` para establecer la relación de aspecto de los ejes y `grid()` para mostrar la cuadrícula.

```python
# Set the limits and display the grid
ax1.set_aspect(1.)
ax1.set_xlim(-5, 12)
ax1.set_ylim(-5, 10)
ax1.grid(True)
```
