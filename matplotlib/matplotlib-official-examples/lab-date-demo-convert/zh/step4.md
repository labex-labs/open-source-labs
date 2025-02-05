# 创建图表

现在，我们可以使用日期和 y 值来创建图表。我们将首先使用 subplots 函数创建一个图形和轴对象。然后，我们将使用 plot 函数绘制图表。复制并粘贴以下代码：

```python
fig, ax = plt.subplots()
ax.plot(dates, y**2, 'o')
```
