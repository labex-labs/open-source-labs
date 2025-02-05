# 创建图表

现在，我们将使用 `matplotlib` 创建图表。我们将在同一图表上绘制三个正弦波，并将第一个波的可见性设置为 `False`，因为我们希望开始时它是隐藏的。

```python
fig, ax = plt.subplots()
l0, = ax.plot(t, s0, visible=False, lw=2, color='black', label='1 Hz')
l1, = ax.plot(t, s1, lw=2, color='red', label='2 Hz')
l2, = ax.plot(t, s2, lw=2, color='green', label='3 Hz')
fig.subplots_adjust(left=0.2)
```
