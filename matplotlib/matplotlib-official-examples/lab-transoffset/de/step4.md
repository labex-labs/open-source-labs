# Text zum Streudiagramm hinzufügen

Jetzt werden wir mithilfe von `offset_copy` Text zu unserem Streudiagramm hinzufügen. Wir werden zunächst einen Transformationsvorgang erstellen, der den Text an einem angegebenen Offset in Bildschirmkoordinaten relativ zu einem in beliebigen Koordinaten angegebenen Ort positioniert. Anschließend werden wir die `text`-Funktion aus `matplotlib.pyplot` verwenden, um den Text zum Diagramm hinzuzufügen.

```python
# Create the transform
trans_offset = mtransforms.offset_copy(ax.transData, fig=fig,
                                       x=0.05, y=0.10, units='inches')

# Add text to the plot
for x, y in zip(xs, ys):
    plt.text(x, y, '%d, %d' % (int(x), int(y)), transform=trans_offset)
```
