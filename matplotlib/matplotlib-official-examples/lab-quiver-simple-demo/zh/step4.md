# 创建箭袋图的键

我们可以在图中添加一个箭袋图的键，以显示箭头的比例。我们使用 `ax.quiverkey()` 函数来添加该键。我们传入 `q` 对象、键的 `X` 和 `Y` 位置、箭头的长度、键的标签以及标签的位置。

```python
ax.quiverkey(q, X=0.3, Y=1.1, U=10,
             label='Quiver key, length = 10', labelpos='E')
```
