# 生成简单图表

首先，让我们使用 `pyplot` 中的 `plot` 函数生成一个简单的图表。在这个例子中，我们将绘制一个 y 值为 `[1, 2, 3, 4]` 的折线图：

```python
import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()
```

解释：

- 我们从 `matplotlib` 中导入 `pyplot` 模块并将其别名为 `plt`。
- `plot` 函数用于生成折线图。通过提供一个 y 值列表，x 值会自动生成为 `[0, 1, 2, 3]`，因为 Python 中的范围从 0 开始。
- `ylabel` 函数设置 y 轴的标签。
- 最后，`show` 函数显示图表。
