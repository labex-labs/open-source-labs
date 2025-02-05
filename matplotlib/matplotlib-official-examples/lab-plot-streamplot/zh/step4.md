# 变化的颜色

在这一步中，我们将创建一个具有变化颜色的流线图。`color` 参数接受一个二维数组，该数组表示向量场的大小。在这里，我们使用向量场的 `U` 分量作为颜色。

```python
strm = plt.streamplot(X, Y, U, V, color=U, linewidth=2, cmap='autumn')
plt.colorbar(strm.lines)
plt.title('Varying Color')
plt.show()
```
