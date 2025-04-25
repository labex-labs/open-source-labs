# 创建一个示例绘图

让我们创建一个示例绘图，看看 y 轴刻度标签在右侧时的样子。

```python
x = np.arange(10)

fig, (ax0, ax1) = plt.subplots(2, 1, sharex=True, figsize=(6, 6))

ax0.plot(x)
ax0.yaxis.tick_left()

ax1.plot(x)

plt.show()
```
