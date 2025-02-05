# 创建 UpdatingRect 类

我们将创建一个名为 UpdatingRect 的 Rectangle 子类。调用这个类时会传入一个 Axes 实例，使矩形更新其形状以匹配 Axes 的边界。

```python
class UpdatingRect(Rectangle):
    def __call__(self, ax):
        self.set_bounds(*ax.viewLim.bounds)
        ax.figure.canvas.draw_idle()
```
