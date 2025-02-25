# Добавление текста к полярному графику

Наконец, мы добавим текст к нашему полярному графику с использованием `offset_copy` и функции `text` из `matplotlib.pyplot`.

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
