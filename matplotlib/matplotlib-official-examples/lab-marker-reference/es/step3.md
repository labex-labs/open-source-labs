# Estilos de relleno de marcadores

El color del borde y el color de relleno de los marcadores con relleno se pueden especificar por separado. Además, se puede configurar el `fillstyle` para que sea sin relleno, completamente relleno o relleno a la mitad en varias direcciones. Los estilos de relleno a la mitad utilizan `markerfacecoloralt` como color de relleno secundario. El siguiente código demuestra cómo crear estilos de relleno de marcadores:

```python
fig, ax = plt.subplots()
fig.suptitle('Marker fillstyle', fontsize=14)
fig.subplots_adjust(left=0.4)

filled_marker_style = dict(marker='o', linestyle=':', markersize=15,
                           color='darkgrey',
                           markerfacecolor='tab:blue',
                           markerfacecoloralt='lightsteelblue',
                           markeredgecolor='brown')

for y, fill_style in enumerate(Line2D.fillStyles):
    ax.text(-0.5, y, repr(fill_style), **text_style)
    ax.plot([y] * 3, fillstyle=fill_style, **filled_marker_style)
format_axes(ax)
```
