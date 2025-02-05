# 使用 `axhspan` 和 `axvspan` 突出显示坐标轴的跨度

填充区域的另一个方便用途是突出显示坐标轴的水平或垂直跨度。为此，Matplotlib 提供了辅助函数 `axhspan` 和 `axvspan`。有关更多信息，请参阅 `axhspan_demo` 示例库。

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

ax.axhspan(0.25, 0.75, facecolor='0.5', alpha=0.5)
ax.axvspan(6, 7, facecolor='r', alpha=0.5)

plt.show()
```
