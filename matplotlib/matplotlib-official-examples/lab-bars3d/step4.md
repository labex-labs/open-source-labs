# Customize the Bar Graphs

We will now customize the bar graphs. We will create an array of colors and use the `bar()` method to plot the bar graphs. We will set the `zdir` parameter to 'y' to project the bar graphs onto the y-axis planes. We will also set the `alpha` parameter to 0.8 to adjust the transparency of the bars.

```python
    cs = [c] * len(xs)
    cs[0] = 'c'
    ax.bar(xs, ys, zs=k, zdir='y', color=cs, alpha=0.8)
```
