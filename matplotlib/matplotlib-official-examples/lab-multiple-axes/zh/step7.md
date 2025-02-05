# 创建动画

第七步是使用`FuncAnimation`函数创建动画对象。我们传入图形对象、动画函数、帧之间的时间间隔（以毫秒为单位）、帧数以及动画重复前的延迟时间。

```python
ani = animation.FuncAnimation(
    fig,
    animate,
    interval=50,
    blit=False,  # blitting can't be used with Figure artists
    frames=x,
    repeat_delay=100,
)
```
