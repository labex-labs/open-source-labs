# 使用简洁格式化器设置刻度标签格式

我们将使用简洁格式化器设置第二个子图上的刻度标签格式。

```python
ax = axs[1]
ax.set_title('ConciseFormatter', loc='left', y=0.85, x=0.02, fontsize='medium')
ax.xaxis.set_major_formatter(mdates.ConciseDateFormatter(ax.xaxis.get_major_locator()))
```
