# Annotate the Plot

Now, we will annotate the plot by adding an arrow pointing to a specific coordinate. In this example, we will add an arrow pointing to the local maximum of the cosine function.

```python
ax.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )
```

The `ax.annotate()` function takes several arguments. The first argument is the text that will be displayed on the plot. The `xy` argument specifies the coordinates of the point that we want to annotate. The `xytext` argument specifies the coordinates of the text. The `arrowprops` argument is a dictionary that specifies the properties of the arrow.
