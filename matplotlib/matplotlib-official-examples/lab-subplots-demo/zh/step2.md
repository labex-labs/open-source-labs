# 沿一个方向堆叠子图

要创建垂直或水平堆叠的多个子图，我们可以将行数和列数作为参数传递给 `subplots()` 函数。返回的 `axs` 对象是一个一维 numpy 数组，其中包含创建的 `Axes` 列表。

```python
fig, axs = plt.subplots(2)
axs[0].plot(x, y)
axs[1].plot(x, -y)
```
