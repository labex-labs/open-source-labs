# Crear una figura con dos ejes ajustables

En este paso, creamos una figura con dos ejes ajustables. Usamos el método `make_axes_locatable` para crear un divisor que permite ajustar los ejes. Agregamos un nuevo eje a la derecha del primer eje usando el método `append_axes`.

```python
fig = plt.figure()
ax1 = fig.add_axes([0, 0, 1, 1])
divider = make_axes_locatable(ax1)
ax2 = divider.append_axes("right", "100%", pad=0.3, sharey=ax1)
fig.add_axes(ax2)
```
