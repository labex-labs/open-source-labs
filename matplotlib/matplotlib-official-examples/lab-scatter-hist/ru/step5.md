# Определить позиции осей с использованием inset_axes

Мы также можем использовать `inset_axes`, чтобы располагать боковые оси _за пределами_ основной оси. Преимущество этого заключается в том, что соотношение сторон основной оси может быть фиксировано, а боковые оси всегда будут рисоваться относительно положения оси.

```python
# Create a Figure, which doesn't have to be square.
fig = plt.figure(layout='constrained')
# Create the main axes, leaving 25% of the figure space at the top and on the right to position marginals.
ax = fig.add_gridspec(top=0.75, right=0.75).subplots()
# The main axes' aspect can be fixed.
ax.set(aspect=1)
# Create marginal axes, which have 25% of the size of the main axes.
# Note that the inset axes are positioned *outside* (on the right and the top) of the main axes,
# by specifying axes coordinates greater than 1.
# Axes coordinates less than 0 would likewise specify positions on the left and the bottom of the main axes.
ax_histx = ax.inset_axes([0, 1.05, 1, 0.25], sharex=ax)
ax_histy = ax.inset_axes([1.05, 0, 0.25, 1], sharey=ax)
# Draw the scatter plot and marginals.
scatter_hist(x, y, ax, ax_histx, ax_histy)
```
