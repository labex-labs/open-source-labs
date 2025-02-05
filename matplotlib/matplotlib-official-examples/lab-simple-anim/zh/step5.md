# 创建动画对象

现在我们可以使用 `FuncAnimation()` 函数创建动画对象。我们将传入图形对象、动画函数、更新间隔以及要保存的帧数。

```python
ani = animation.FuncAnimation(
    fig, animate, interval=20, blit=True, save_count=50)
```
