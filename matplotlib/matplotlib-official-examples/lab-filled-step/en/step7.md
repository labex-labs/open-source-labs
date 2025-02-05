# Create the hatch-filled histogram

We will create a hatch-filled histogram using the `stack_hist` function we defined earlier. We will use the `stack_data`, `color_cycle`, and `hist_func` we defined earlier. We will also set `plot_kwargs` to include edgecolor and orientation.

```python
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 4.5), tight_layout=True)
arts = stack_hist(ax1, stack_data, color_cycle + label_cycle + hatch_cycle, hist_func=hist_func)

arts = stack_hist(ax2, stack_data, color_cycle, hist_func=hist_func, plot_kwargs=dict(edgecolor='w', orientation='h'))
ax1.set_ylabel('counts')
ax1.set_xlabel('x')
ax2.set_xlabel('counts')
ax2.set_ylabel('x')
```
