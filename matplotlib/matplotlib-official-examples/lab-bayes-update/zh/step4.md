# 创建动画

既然我们已经定义了`UpdateDist`类，那么我们可以使用Matplotlib的`FuncAnimation`类来创建动画。我们创建一个图形对象和一个轴对象，并将轴对象传递给`UpdateDist`类以创建该类的一个新实例。

```python
fig, ax = plt.subplots()
ud = UpdateDist(ax, prob=0.7)
anim = FuncAnimation(fig, ud, frames=100, interval=100, blit=True)
plt.show()
```

`FuncAnimation`类接受几个参数：

- `fig`：图形对象
- `ud`：`UpdateDist`实例
- `frames`：要制作动画的帧数
- `interval`：帧之间的时间间隔（以毫秒为单位）
- `blit`：是否仅更新绘图中已更改的部分
