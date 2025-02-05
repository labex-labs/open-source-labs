# Plot the Data

Plot the data on each of the three subplots using `plot_wireframe`.

```python
for ax in axs:
    ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)
```
