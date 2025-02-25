# Agregar botones de verificación

Ahora agregaremos los botones de verificación a nuestro gráfico utilizando la función `CheckButtons`. Pasaremos las líneas trazadas como etiquetas y estableceremos la visibilidad inicial de cada línea. También ajustaremos las propiedades de los botones de verificación para que coincidan con los colores de las líneas trazadas.

```python
lines_by_label = {l.get_label(): l for l in [l0, l1, l2]}
line_colors = [l.get_color() for l in lines_by_label.values()]

rax = fig.add_axes([0.05, 0.4, 0.1, 0.15])
check = CheckButtons(
    ax=rax,
    labels=lines_by_label.keys(),
    actives=[l.get_visible() for l in lines_by_label.values()],
    label_props={'color': line_colors},
    frame_props={'edgecolor': line_colors},
    check_props={'facecolor': line_colors},
)
```
