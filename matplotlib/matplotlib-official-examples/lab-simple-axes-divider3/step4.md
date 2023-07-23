# Customize the axes limits and appearance

We will customize the limits and appearance of each axis using the `set_xlim`, `set_ylim`, and `tick_params` methods.

```python
ax[0].set_xlim(0, 2)
ax[1].set_xlim(0, 1)
ax[0].set_ylim(0, 1)
ax[2].set_ylim(0, 2)
for ax1 in ax:
    ax1.tick_params(labelbottom=False, labelleft=False)
```
