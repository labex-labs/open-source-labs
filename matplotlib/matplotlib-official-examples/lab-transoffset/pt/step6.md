# Adicionar Texto ao Gráfico Polar (Polar Plot)

Finalmente, adicionaremos texto ao nosso gráfico polar usando `offset_copy` e a função `text` de `matplotlib.pyplot`.

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
