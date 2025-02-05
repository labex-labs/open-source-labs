# 创建子图

我们可以使用 `plt.subplot()` 方法创建子图。在这个例子中，我们将创建三个子图，第一个子图占据第一行和所有三列，第二个和第三个子图分别占据第二行和第三行，并与第一个子图共享 x 轴。

```python
ax1 = plt.subplot(311)
ax2 = plt.subplot(312, sharex=ax1)
ax3 = plt.subplot(313, sharex=ax1, sharey=ax1)
```
