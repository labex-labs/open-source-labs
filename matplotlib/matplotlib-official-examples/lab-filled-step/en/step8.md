# Create the labeled hatch-filled histogram

We will create a labeled hatch-filled histogram using the `stack_hist` function we defined earlier. We will use the `dict_data`, `color_cycle`, and `hist_func` we defined earlier. We will also set `labels` to `['set 0', 'set 3']` to plot only the first and last set.

```python
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 4.5), tight_layout=True, sharey=True)
dict_data = dict(zip((c['label'] for c in label_cycle), stack_data))
arts = stack_hist(ax1, dict_data, color_cycle + hatch_cycle, hist_func=hist_func)

arts = stack_hist(ax2, dict_data, color_cycle + hatch_cycle, hist_func=hist_func, labels=['set 0', 'set 3'])
ax1.xaxis.set_major_locator(mticker.MaxNLocator(5))
ax1.set_xlabel('counts')
ax1.set_ylabel('x')
ax2.set_ylabel('x')
```
