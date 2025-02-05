# Plot data

We will plot the data on all three subplots using the `plot` function.

```python
for ax in axs:
    ax.plot('date', 'adj_close', data=data)
    ax.grid(True)
    ax.set_ylabel(r'Price [\$]')
```
