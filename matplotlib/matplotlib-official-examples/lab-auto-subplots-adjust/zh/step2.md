# 创建图表

让我们创建一个带有一些较长 y 轴标签的简单折线图。

```python
fig, ax = plt.subplots()
ax.plot(range(10))
ax.set_yticks([2, 5, 7], labels=['really, really, really', 'long', 'labels'])
```
