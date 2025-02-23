# Anpassen des Pfeils, um ihn auf die Ellipse zu verengen

In diesem Schritt passen wir den Pfeil an, um ihn auf die Ellipse zu verengen. Wir verwenden den Parameter `shrinkB`, um die Menge anzugeben, um die der Pfeil sich auf die Ellipse zu verengen hat.

```python
ax = axs.flat[3]
ax.plot([x1, x2], [y1, y2], ".")
el = mpatches.Ellipse((x1, y1), 0.3, 0.4, angle=30, alpha=0.2)
ax.add_artist(el)
ax.annotate("",
            xy=(x1, y1), xycoords='data',
            xytext=(x2, y2), textcoords='data',
            arrowprops=dict(arrowstyle="fancy",
                            color="0.5",
                            patchB=el,
                            shrinkB=5,
                            connectionstyle="arc3,rad=0.3",
                            ),
            )
```
