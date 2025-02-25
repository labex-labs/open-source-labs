# Créez une flèche tournée

Dans cette étape, nous allons créer une flèche de direction ancrée tournée. Cette flèche sera tournée de 30 degrés et aura une police de caractères à serifs.

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
