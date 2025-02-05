# 创建图表

既然我们已经有了数据，就可以创建图表了。首先，我们使用 `plt.subplots()` 创建一个图形和轴对象。然后，我们使用 `ax.plot()` 绘制数据。

```python
fig, ax = plt.subplots()
ax.plot(t, s)
```
