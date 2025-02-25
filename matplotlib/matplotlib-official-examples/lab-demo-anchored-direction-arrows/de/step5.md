# Erstellen eines gedrehten Pfeils

In diesem Schritt werden wir einen gedrehten ankergestützten Richtungspfeil erstellen. Dieser Pfeil wird um 30 Grad gedreht und eine serifenhaltige Schriftart haben.

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
