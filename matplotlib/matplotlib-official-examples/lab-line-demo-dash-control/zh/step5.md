# 使用`.Line2D.set_dashes()`修改虚线序列

我们可以使用`.Line2D.set_dashes()`来修改虚线序列。在这个例子中，我们修改`line1`的虚线序列，以创建一个由 2 点长的线、2 点的间隔、10 点长的线和 2 点的间隔组成的虚线图案。我们还使用`line1.set_dash_capstyle()`将端点样式设置为'round'。

```python
line1, = ax.plot(x, y, label='Using set_dashes() and set_dash_capstyle()')
line1.set_dashes([2, 2, 10, 2])  # 2pt line, 2pt break, 10pt line, 2pt break.
line1.set_dash_capstyle('round')
```
