# 设置绘图

现在，我们可以设置绘图了。我们将使用 `plt.subplots()` 创建一个图形和轴对象。然后，我们将使用 `ax.triplot()` 绘制三角剖分图。

```python
fig, ax = plt.subplots()
ax.triplot(triang)
```
