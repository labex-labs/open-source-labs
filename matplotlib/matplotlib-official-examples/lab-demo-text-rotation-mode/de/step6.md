# Betone die Begrenzung des Texts

Wenn der `Rotationmodus` auf `'default'` gesetzt ist, werden wir die Begrenzung des Texts mit einem Rechteck betonen. Wir werden die `get_window_extent`-Funktion verwenden, um die Begrenzung zu erhalten und sie mit dem `transData`-Attribut in die Datenkoordinaten umzuwandeln.

```python
if mode == "default":
    fig.canvas.draw()
    for ax, text in texts.items():
        bb = text.get_window_extent().transformed(ax.transData.inverted())
        rect = plt.Rectangle((bb.x0, bb.y0), bb.width, bb.height,
                             facecolor="C1", alpha=0.3, zorder=2)
        ax.add_patch(rect)
```
