# Plotting Sparsity Pattern

We will use the `spy` function to plot the sparsity pattern of the array. We will use different parameters such as `markersize` and `precision` to customize the plot.

```python
ax1.spy(x, markersize=5)
ax2.spy(x, precision=0.1, markersize=5)
ax3.spy(x)
ax4.spy(x, precision=0.1)
```
