# Estilos de Preenchimento de Marcadores (Marker Fill Styles)

A cor da borda e a cor de preenchimento de marcadores preenchidos podem ser especificadas separadamente. Adicionalmente, o `fillstyle` pode ser configurado para ser não preenchido (unfilled), totalmente preenchido (fully filled) ou semi-preenchido (half-filled) em várias direções. Os estilos semi-preenchidos usam `markerfacecoloralt` como uma cor de preenchimento secundária. O código a seguir demonstra como criar estilos de preenchimento de marcadores:

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
