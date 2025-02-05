# Define a function to annotate axes

We define a function `annotate_axes` that we will use later to label each of the primary 3D view planes with their respective angles.

```python
def annotate_axes(ax, text, fontsize=18):
    ax.text(x=0.5, y=0.5, z=0.5, s=text,
            va="center", ha="center", fontsize=fontsize, color="black")
```
