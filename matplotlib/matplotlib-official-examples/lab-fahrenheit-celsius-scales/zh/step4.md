# 创建图表

现在，我们使用 `matplotlib.pyplot` 的 `subplots()` 函数创建一个带有两个 y 轴的图表。我们还将第一个轴的 `ylim_changed` 事件连接到 `convert_ax_c_to_celsius()` 函数。

```python
fig, ax_f = plt.subplots()
ax_c = ax_f.twinx()

ax_f.callbacks.connect("ylim_changed", convert_ax_c_to_celsius)
```
