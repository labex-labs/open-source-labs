# Set Axes Limits and Save Figure

We set the x and y limits for the axes and save the figure as a bytes string in the SVG format using `io.BytesIO()` and `plt.savefig()`.

```python
ax.set_xlim(0., 1.)
ax.set_ylim(0., 1.)

f = io.BytesIO()
plt.savefig(f, format="svg")
```
