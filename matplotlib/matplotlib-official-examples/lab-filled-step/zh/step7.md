# 创建带阴影的填充直方图

我们将使用之前定义的 `stack_hist` 函数创建一个带阴影的填充直方图。我们将使用之前定义的 `stack_data`、`color_cycle` 和 `hist_func`。我们还将设置 `plot_kwargs` 以包含边缘颜色和方向。

```python
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 4.5), tight_layout=True)
arts = stack_hist(ax1, stack_data, color_cycle + label_cycle + hatch_cycle, hist_func=hist_func)

arts = stack_hist(ax2, stack_data, color_cycle, hist_func=hist_func, plot_kwargs=dict(edgecolor='w', orientation='h'))
ax1.set_ylabel('counts')
ax1.set_xlabel('x')
ax2.set_xlabel('counts')
ax2.set_ylabel('x')
```
