# 创建动画

我们使用 `matplotlib.animation` 中的 `FuncAnimation` 类创建一个动画。我们将图形对象、更新函数、总帧数（等于随机游走中的步数）、所有随机游走的列表以及所有线条的列表作为参数传递给 `FuncAnimation` 构造函数。

```python
# 创建动画对象
ani = animation.FuncAnimation(
    fig, update_lines, num_steps, fargs=(walks, lines), interval=100)
```
