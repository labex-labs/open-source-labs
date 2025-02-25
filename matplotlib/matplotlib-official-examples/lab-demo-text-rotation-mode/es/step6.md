# Resaltar la caja delimitadora del texto

Si el `rotation_mode` se establece en `'default'`, resaltaremos la caja delimitadora del texto utilizando un rectángulo. Usaremos la función `get_window_extent` para obtener la caja delimitadora y la transformaremos a coordenadas de datos utilizando el atributo `transData`.

```python
if mode == "default":
    fig.canvas.draw()
    for ax, text in texts.items():
        bb = text.get_window_extent().transformed(ax.transData.inverted())
        rect = plt.Rectangle((bb.x0, bb.y0), bb.width, bb.height,
                             facecolor="C1", alpha=0.3, zorder=2)
        ax.add_patch(rect)
```
