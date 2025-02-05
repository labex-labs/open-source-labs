# Create the hatches_plot function

The hatches_plot function will create a rectangle with the specified hatching pattern and add it to the axis. It will also add a text with the hatching pattern.

```python
def hatches_plot(ax, h):
    ax.add_patch(Rectangle((0, 0), 2, 2, fill=False, hatch=h))
    ax.text(1, -0.5, f"' {h} '", size=15, ha="center")
    ax.axis('equal')
    ax.axis('off')
```
