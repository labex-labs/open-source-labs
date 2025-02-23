# Zwei Punkte mit einem Pfeil verbinden

In diesem Schritt verbinden wir die beiden Punkte mit einem Pfeil. Wir verwenden die `annotate`-Funktion, um den Pfeil zu erstellen, und passen den Pfeilstil und die Farbe an.

```python
ax = axs.flat[0]
ax.plot([x1, x2], [y1, y2], ".")
ax.annotate("",
            xy=(x1, y1), xycoords='data',
            xytext=(x2, y2), textcoords='data',
            arrowprops=dict(arrowstyle="-",
                            color="0.5",
                            connectionstyle="arc3,rad=0.3",
                            ),
            )
```
