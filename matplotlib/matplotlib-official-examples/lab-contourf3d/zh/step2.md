# 创建图形和轴对象

现在我们将使用 `add_subplot()` 方法创建图形和轴对象。我们将把 `projection` 参数设置为 `'3d'` 以创建一个三维绘图。

```python
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
```
