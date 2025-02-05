# 在子图上绘制数据

要在子图上绘制数据，你需要使用 `subfig.subplots()` 为每个子图创建一个子图对象。然后，你可以使用 Matplotlib 中的任何绘图函数来创建绘图。

```python
ax1 = subfigs[0].subplots()
ax1.plot(np.arange(10), np.random.randn(10))

ax2 = subfigs[1].subplots()
ax2.plot(np.arange(10), np.random.randn(10))
```

这将创建两个子图，每个子图都有一个随机数据的绘图。
