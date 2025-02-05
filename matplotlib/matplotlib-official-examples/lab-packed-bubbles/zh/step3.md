# 定义气泡图类

`BubbleChart` 类用于创建填充气泡图。该类接受一个气泡面积数组和一个气泡间距值。`__init__` 方法设置气泡的初始位置，并计算最大步长距离，即每个气泡在一次迭代中可以移动的距离。

```python
class BubbleChart:
    def __init__(self, area, bubble_spacing=0):
        """
        为气泡收缩进行设置。

        参数
        ----------
        area : 类似数组
            气泡的面积。
        bubble_spacing : 浮点数，默认值：0
            收缩后气泡之间的最小间距。

        注意事项
        -----
        如果 “area” 是排序的，结果可能看起来很奇怪。
        """
        area = np.asarray(area)
        r = np.sqrt(area / np.pi)

        self.bubble_spacing = bubble_spacing
        self.bubbles = np.ones((len(area), 4))
        self.bubbles[:, 2] = r
        self.bubbles[:, 3] = area
        self.maxstep = 2 * self.bubbles[:, 2].max() + self.bubble_spacing
        self.step_dist = self.maxstep / 2

        # 计算气泡的初始网格布局
        length = np.ceil(np.sqrt(len(self.bubbles)))
        grid = np.arange(length) * self.maxstep
        gx, gy = np.meshgrid(grid, grid)
        self.bubbles[:, 0] = gx.flatten()[:len(self.bubbles)]
        self.bubbles[:, 1] = gy.flatten()[:len(self.bubbles)]

        self.com = self.center_of_mass()
```
