# Format the plot

To make our plot more readable, we can format it using Matplotlib's formatting functions. In this example, we will format the y-axis labels to display values in millions.

```python
def millions(x):
    return '$%1.1fM' % (x * 1e-6)

ax.fmt_ydata = millions
```
