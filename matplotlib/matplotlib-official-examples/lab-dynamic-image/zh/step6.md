# 创建动画

现在我们将使用 `ArtistAnimation` 方法来创建动画。我们将传入图形对象、`ims` 列表、帧之间的时间间隔以及重复延迟。

```python
ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True, repeat_delay=1000)
```
