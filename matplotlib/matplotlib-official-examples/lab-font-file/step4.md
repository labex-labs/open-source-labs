# Set the font for the title

We set the font for the title of the plot using the `set_title()` method of the `Axes` class. We pass the font path as the `font` parameter and the name of the font file as the title of the plot.

```python
ax.set_title(f'This is a special font: {fpath.name}', font=fpath)
```
