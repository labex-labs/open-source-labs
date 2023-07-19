# Creating Subplots

We will now create a 2x2 grid of subplots using the `subplots` function. This will give us four plots to visualize the sparsity pattern of the array.

```python
fig, axs = plt.subplots(2, 2)
ax1 = axs[0, 0]
ax2 = axs[0, 1]
ax3 = axs[1, 0]
ax4 = axs[1, 1]
```
