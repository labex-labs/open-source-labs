# 反转坐标轴

要反转x轴，我们只需使用`set_xlim`函数颠倒限制的顺序。在这个例子中，我们将x轴限制设置为从5到0，这实际上就反转了x轴。

```python
ax.set_xlim(5, 0)  # decreasing time
```
