# 创建带标签的阴影填充直方图

我们将使用之前定义的 `stack_hist` 函数创建一个带标签的阴影填充直方图。我们将使用之前定义的 `dict_data`、`color_cycle` 和 `hist_func`。我们还将把 `labels` 设置为 `['set 0','set 3']`，以便只绘制第一组和最后一组。

```python
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 4.5), tight_layout=True, sharey=True)
dict_data = dict(zip((c['label'] for c in label_cycle), stack_data))
arts = stack_hist(ax1, dict_data, color_cycle + hatch_cycle, hist_func=hist_func)

arts = stack_hist(ax2, dict_data, color_cycle + hatch_cycle, hist_func=hist_func, labels=['set 0','set 3'])
ax1.xaxis.set_major_locator(mticker.MaxNLocator(5))
ax1.set_xlabel('counts')
ax1.set_ylabel('x')
ax2.set_ylabel('x')
```
