# 创建图表

我们将使用 `matplotlib.pyplot.plot()` 函数来创建图表。

```python
# plot the data
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(xdata1, ydata1, color='tab:blue')
ax.plot(xdata2, ydata2, color='tab:orange')
```
