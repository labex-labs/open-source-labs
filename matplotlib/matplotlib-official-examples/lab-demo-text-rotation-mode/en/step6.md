# Highlight the bounding box of the text

If the `rotation_mode` is set to `'default'`, we will highlight the bounding box of the text using a rectangle. We will use the `get_window_extent` function to get the bounding box and transform it to the data coordinates using the `transData` attribute.

```python
if mode == "default":
    fig.canvas.draw()
    for ax, text in texts.items():
        bb = text.get_window_extent().transformed(ax.transData.inverted())
        rect = plt.Rectangle((bb.x0, bb.y0), bb.width, bb.height,
                             facecolor="C1", alpha=0.3, zorder=2)
        ax.add_patch(rect)
```
