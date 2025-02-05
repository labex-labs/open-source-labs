# 移除主刻度标签和次刻度

为了模拟使标签在刻度之间居中的效果，我们需要移除主刻度标签和次刻度，只显示次刻度标签。我们可以使用 `tick_params()` 函数并将 `tick1On` 和 `tick2On` 参数设置为 `False` 来实现这一点。

```python
# Remove the tick lines
ax.tick_params(axis='x', which='minor', tick1On=False, tick2On=False)
```
