# 创建一个图表并将x轴设置为对数刻度

我们使用`subplots()`方法创建一个图形和轴对象。然后，我们使用`semilogx()`方法绘制指数衰减函数，并使用`set_xscale()`方法将x轴设置为对数刻度。我们还使用`grid()`方法为图表添加网格。

```python
fig, ax = plt.subplots()

ax.semilogx(t, np.exp(-t / 5.0))
ax.set_xscale('log')
ax.grid()
```
