# Anpassen des Pfeils, um ihn an die Ellipse anzuschließen

In diesem Schritt passen wir den Pfeil an, um ihn an die Ellipse anzuschließen. Wir verwenden den Parameter `arrowprops`, um anzugeben, dass der Pfeil an die Ellipse angeschlossen werden soll, und passen auch den Pfeilstil und die Farbe an.

```python
ax = axs.flat[2]
ax.plot([x1, x2], [y1, y2], ".")
el = mpatches.Ellipse((x1, y1), 0.3, 0.4, angle=30, alpha=0.2)
ax.add_artist(el)
ax.annotate("",
            xy=(x1, y1), xycoords='data',
            xytext=(x2, y2), textcoords='data',
            arrowprops=dict(arrowstyle="-",
                            color="0.5",
                            patchB=el,
                            connectionstyle="arc3,rad=0.3",
                            ),
            )
```
