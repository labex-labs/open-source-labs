# 极坐标图

通过将 `projection='polar'` 参数传递给 `subplots()` 函数，我们可以创建极坐标 `Axes` 的网格。

```python
fig, (ax1, ax2) = plt.subplots(1, 2, subplot_kw=dict(projection='polar'))
ax1.plot(x, y)
ax2.plot(x, y ** 2)
```
