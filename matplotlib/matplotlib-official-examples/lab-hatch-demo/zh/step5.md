# 创建带有阴影线补丁的图表

你也可以在图表中对补丁使用阴影线。在这种情况下，我们将使用`fill_between`函数来创建一个带有阴影线的补丁。

```python
x = np.arange(0, 40, 0.2)
plt.fill_between(x, np.sin(x) * 4 + 30, y2=0, hatch='///', zorder=2, fc='c')
```
