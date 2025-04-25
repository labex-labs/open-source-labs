# 定义动画

在这一步中，我们将定义想要创建的动画。我们将创建一个动画，该动画展示一个正态分布，并且每一帧都向右移动。

```python
class PauseAnimation:
    def __init__(self):
        # 创建图形和坐标轴
        fig, ax = plt.subplots()
        ax.set_title('Click to pause/resume the animation')

        # 创建 x 轴的值
        x = np.linspace(-0.1, 0.1, 1000)

        # 从一个正态分布开始
        self.n0 = (1.0 / ((4 * np.pi * 2e-4 * 0.1) ** 0.5)
                   * np.exp(-x ** 2 / (4 * 2e-4 * 0.1)))

        # 创建绘图
        self.p, = ax.plot(x, self.n0)

        # 创建动画
        self.animation = animation.FuncAnimation(
            fig, self.update, frames=200, interval=50, blit=True)

        # 将动画设置为未暂停
        self.paused = False

        # 添加一个按钮按下事件来切换暂停状态
        fig.canvas.mpl_connect('button_press_event', self.toggle_pause)

    def toggle_pause(self, *args, **kwargs):
        # 在暂停和未暂停之间切换
        if self.paused:
            self.animation.resume()
        else:
            self.animation.pause()
        self.paused = not self.paused

    def update(self, i):
        # 更新正态分布
        self.n0 += i / 100 % 5
        self.p.set_ydata(self.n0 % 20)
        return (self.p,)
```
