# 定义UpdateDist类

接下来，我们定义一个名为`UpdateDist`的类，用于在观察到新数据时更新贝塔分布。`UpdateDist`类接受两个参数：Matplotlib轴对象和成功的初始概率。

```python
class UpdateDist:
    def __init__(self, ax, prob=0.5):
        self.success = 0
        self.prob = prob
        self.line, = ax.plot([], [], 'k-')
        self.x = np.linspace(0, 1, 200)
        self.ax = ax

        # 设置绘图参数
        self.ax.set_xlim(0, 1)
        self.ax.set_ylim(0, 10)
        self.ax.grid(True)

        # 这条垂直线代表理论值，绘制的分布应收敛于此。
        self.ax.axvline(prob, linestyle='--', color='black')
```

`__init__`方法通过将成功的初始次数设置为零（`self.success = 0`）以及将成功的初始概率设置为作为参数传递的值（`self.prob = prob`）来初始化类实例。我们还创建一个线条对象来表示贝塔分布并设置绘图参数。

`__call__`方法在动画每次更新时被调用。它模拟抛硬币实验并相应地更新贝塔分布。

```python
def __call__(self, i):
        # 这样绘图就能持续运行，我们只需不断观察该过程的新实现情况
        if i == 0:
            self.success = 0
            self.line.set_data([], [])
            return self.line,

        # 通过均匀选取并与阈值比较来选择成功情况
        if np.random.rand() < self.prob:
            self.success += 1
        y = beta_pdf(self.x, self.success + 1, (i - self.success) + 1)
        self.line.set_data(self.x, y)
        return self.line,
```

如果这是动画的第一帧（`if i == 0`），我们将成功次数重置为零并清除线条对象。否则，我们通过生成一个介于0和1之间的随机数（`np.random.rand()`）并将其与成功概率（`self.prob`）进行比较来模拟抛硬币实验。如果随机数小于成功概率，我们将其计为一次成功，并使用`beta_pdf`函数更新贝塔分布。最后，我们用新数据更新线条对象并返回它。
