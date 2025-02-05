# 绘制稀疏模式

我们将使用`spy`函数来绘制数组的稀疏模式。我们将使用不同的参数，如`markersize`和`precision`来定制绘图。

```python
ax1.spy(x, markersize=5)
ax2.spy(x, precision=0.1, markersize=5)
ax3.spy(x)
ax4.spy(x, precision=0.1)
```
