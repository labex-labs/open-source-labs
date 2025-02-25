# Crear ejes flotantes

En este paso, crearemos dos ejes flotantes que se utilizarán para mostrar la curva polar en un cuadro rectangular. Utilizaremos `new_floating_axis()` para crear los ejes flotantes.

```python
# Create the floating axes
ax1.axis["lat"] = axis = ax1.new_floating_axis(0, 60)
axis.label.set_text(r"$\theta = 60^{\circ}$")
axis.label.set_visible(True)

ax1.axis["lon"] = axis = ax1.new_floating_axis(1, 6)
axis.label.set_text(r"$r = 6$")
```
