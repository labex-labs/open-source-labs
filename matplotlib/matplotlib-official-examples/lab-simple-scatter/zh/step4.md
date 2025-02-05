# 创建动画

最后一步是创建动画。我们使用 animation 模块中的 FuncAnimation 函数来完成此操作。该函数接受几个参数，包括图形对象、将更新绘图的函数以及要使用的帧数。

```python
def animate(i):
    scat.set_offsets((x[i], 0))
    return scat,

ani = animation.FuncAnimation(fig, animate, repeat=True,
                                    frames=len(x) - 1, interval=50)
```
