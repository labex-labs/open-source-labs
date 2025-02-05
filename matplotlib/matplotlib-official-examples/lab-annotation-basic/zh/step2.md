# 创建一个图表

接下来，我们将使用 Matplotlib 创建一个图表。在这个例子中，我们将在一系列值上绘制余弦函数。

```python
fig, ax = plt.subplots()

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
line, = ax.plot(t, s, lw=2)
```
