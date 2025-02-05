# 创建三维茎叶图

在这一步中，我们将使用 Matplotlib 的 `stem` 函数创建三维茎叶图。我们将把 x、y 和 z 坐标作为参数传递给 `stem` 函数。

```python
fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))
ax.stem(x, y, z)

plt.show()
```
