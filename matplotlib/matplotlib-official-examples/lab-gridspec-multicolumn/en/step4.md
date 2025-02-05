# Add subplots to the GridSpec

We can add subplots to the GridSpec using the `fig.add_subplot()` function. We can specify the location of the subplot in the grid using the indexing notation of the GridSpec object. For example, `gs[0, :]` specifies the first row and all columns.

```python
ax1 = fig.add_subplot(gs[0, :])
ax2 = fig.add_subplot(gs[1, :-1])
ax3 = fig.add_subplot(gs[1:, -1])
ax4 = fig.add_subplot(gs[-1, 0])
ax5 = fig.add_subplot(gs[-1, -2])
```
