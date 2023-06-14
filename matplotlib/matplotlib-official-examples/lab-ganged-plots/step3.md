# Create Subplots

We create three subplots using the `subplots` function in Matplotlib. We set the `sharex` parameter to `True` to ensure that the subplots share a common x-axis. We also remove the vertical space between the subplots using the `subplots_adjust` function.

```python
fig, axs = plt.subplots(3, 1, sharex=True)
fig.subplots_adjust(hspace=0)
```
