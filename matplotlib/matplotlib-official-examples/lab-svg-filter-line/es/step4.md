# Dibujar sombras

Dibujamos sombras para las líneas utilizando las mismas líneas con un ligero desplazamiento y colores grises. Ajustamos el color y el zorder de las líneas de sombra para que se dibujen por debajo de las líneas originales. También utilizamos el método `offset_copy()` para crear una transformación de desplazamiento para las líneas de sombra.

```python
for l in [l1, l2]:
    xx = l.get_xdata()
    yy = l.get_ydata()
    shadow, = ax.plot(xx, yy)
    shadow.update_from(l)

    shadow.set_color("0.2")
    shadow.set_zorder(l.get_zorder() - 0.5)

    transform = mtransforms.offset_copy(l.get_transform(), fig1, x=4.0, y=-6.0, units='points')
    shadow.set_transform(transform)

    shadow.set_gid(l.get_label() + "_shadow")
```
