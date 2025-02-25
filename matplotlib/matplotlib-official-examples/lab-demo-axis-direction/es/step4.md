# Cambiando la dirección del eje

Ahora, crearemos un bucle para configurar cuatro gráficas diferentes con el eje flotante en cada una de las cuatro direcciones cardinales. En el bucle, usaremos `add_floating_axis1()` y `add_floating_axis2()` para agregar los ejes flotantes, y `set_axis_direction()` para establecer la dirección del eje.

```python
fig = plt.figure(figsize=(8, 4), layout="constrained")

for i, d in enumerate(["bottom", "left", "top", "right"]):
    ax = setup_axes(fig, rect=241+i)
    axis = add_floating_axis1(ax)
    axis.set_axis_direction(d)
    ax.set(title=d)

for i, d in enumerate(["bottom", "left", "top", "right"]):
    ax = setup_axes(fig, rect=245+i)
    axis = add_floating_axis2(ax)
    axis.set_axis_direction(d)
    ax.set(title=d)

plt.show()
```
