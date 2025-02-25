# Establecer los límites y etiquetas para los ejes

Establecemos los límites y etiquetas para cada eje y utilizando el método `set`. También establecemos el color de las etiquetas para que coincida con el color de las líneas utilizando el método `set_color`.

```python
ax.set(xlim=(0, 2), ylim=(0, 2), xlabel="Distance", ylabel="Density")
twin1.set(ylim=(0, 4), ylabel="Temperature")
twin2.set(ylim=(1, 65), ylabel="Velocity")

ax.yaxis.label.set_color(p1.get_color())
twin1.yaxis.label.set_color(p2.get_color())
twin2.yaxis.label.set_color(p3.get_color())
```
