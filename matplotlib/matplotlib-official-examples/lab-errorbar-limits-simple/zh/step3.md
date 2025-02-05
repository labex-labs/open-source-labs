# 创建带上下限的误差线图（默认）

在这一步中，我们创建一个带有上限和下限的误差线图，这是默认行为。

```python
plt.errorbar(x, y + 3, yerr=yerr, label='both limits (default)')
```
