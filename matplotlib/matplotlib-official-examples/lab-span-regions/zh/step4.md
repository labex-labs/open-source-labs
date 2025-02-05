# 给区域着色

我们将使用 `fill_between` 分别给正弦波在水平线上方为正以及下方为负的区域进行着色。

```python
ax.fill_between(t, 1, where=s > 0, facecolor='green', alpha=.5)
ax.fill_between(t, -1, where=s < 0, facecolor='red', alpha=.5)
```
