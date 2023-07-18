# Customize subplots

We can customize the subplots as needed. For example, we can set the title of the figure using the `fig.suptitle()` function, and we can format the axes using the `format_axes()` function.

```python
fig.suptitle("GridSpec")

def format_axes(fig):
    for i, ax in enumerate(fig.axes):
        ax.text(0.5, 0.5, "ax%d" % (i+1), va="center", ha="center")
        ax.tick_params(labelbottom=False, labelleft=False)

format_axes(fig)
```
