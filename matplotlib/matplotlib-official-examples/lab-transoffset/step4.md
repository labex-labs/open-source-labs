# Add Text to the Scatter Plot

Now we will add text to our scatter plot using `offset_copy`. We will first create a transform that positions the text at a specified offset in screen coordinates relative to a location given in any coordinates. Then, we will use the `text` function from `matplotlib.pyplot` to add the text to the plot.

```python
# Create the transform
trans_offset = mtransforms.offset_copy(ax.transData, fig=fig,
                                       x=0.05, y=0.10, units='inches')

# Add text to the plot
for x, y in zip(xs, ys):
    plt.text(x, y, '%d, %d' % (int(x), int(y)), transform=trans_offset)
```
