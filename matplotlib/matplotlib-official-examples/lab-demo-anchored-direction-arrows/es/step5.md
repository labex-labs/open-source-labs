# Crear una flecha girada

En este paso, crearemos una flecha de dirección anclada girada. Esta flecha se girará 30 grados y tendrá una fuente con serif.

```python
fontprops = fm.FontProperties(family='serif')

rotated_arrow = AnchoredDirectionArrows(
                    ax.transAxes,
                    '30', '120',
                    loc='center',
                    color='w',
                    angle=30,
                    fontproperties=fontprops
                    )
ax.add_artist(rotated_arrow)
```
