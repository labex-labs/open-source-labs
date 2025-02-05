# 设置图形和坐标轴

我们将创建一个图形对象，并使用 `fig.add_axes` 方法设置四个坐标轴对象。

```python
fig = plt.figure(figsize=(5.5, 4))
rect = (0.1, 0.1, 0.8, 0.8)
ax = [fig.add_axes(rect, label="%d" % i) for i in range(4)]
```
