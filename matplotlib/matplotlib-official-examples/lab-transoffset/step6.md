# Add Text to the Polar Plot

Finally, we will add text to our polar plot using `offset_copy` and the `text` function from `matplotlib.pyplot`.

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
