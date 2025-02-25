# Text zum Polardiagramm hinzufügen

Schließlich werden wir mithilfe von `offset_copy` und der `text`-Funktion aus `matplotlib.pyplot` Text zu unserem Polardiagramm hinzufügen.

```python
# Create the transform
trans_offset = mtransforms.offset_copy(ax.transData, fig=fig,
                                       y=6, units='dots')

# Add text to the plot
for x, y in zip(xs, ys):
    plt.text(x, y, '%d, %d' % (int(x), int(y)),
             transform=trans_offset,
             horizontalalignment='center',
             verticalalignment='bottom')
```
