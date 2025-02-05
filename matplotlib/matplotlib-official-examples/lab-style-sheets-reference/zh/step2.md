# 定义绘图函数

接下来，你需要定义用于创建示例图表的绘图函数。在这一步中，你将定义以下绘图函数：

- `plot_scatter()`：创建散点图
- `plot_colored_lines()`：按照样式颜色循环绘制带颜色的线条
- `plot_bar_graphs()`：创建条形图
- `plot_colored_circles()`：绘制圆形补丁
- `plot_image_and_patch()`：绘制带有圆形补丁的图像
- `plot_histograms()`：创建直方图

```python
def plot_scatter(ax, prng, nb_samples=100):
    """散点图。"""
    for mu, sigma, marker in [(-.5, 0.75, 'o'), (0.75, 1.,'s')]:
        x, y = prng.normal(loc=mu, scale=sigma, size=(2, nb_samples))
        ax.plot(x, y, ls='none', marker=marker)
    ax.set_xlabel('X 轴标签')
    ax.set_title('坐标轴标题')
    return ax


def plot_colored_lines(ax):
    """按照样式颜色循环绘制带颜色的线条。"""
    t = np.linspace(-10, 10, 100)

    def sigmoid(t, t0):
        return 1 / (1 + np.exp(-(t - t0)))

    nb_colors = len(plt.rcParams['axes.prop_cycle'])
    shifts = np.linspace(-5, 5, nb_colors)
    amplitudes = np.linspace(1, 1.5, nb_colors)
    for t0, a in zip(shifts, amplitudes):
        ax.plot(t, a * sigmoid(t, t0), '-')
    ax.set_xlim(-10, 10)
    return ax


def plot_bar_graphs(ax, prng, min_value=5, max_value=25, nb_samples=5):
    """并排绘制两个条形图，x 轴刻度标签为字母。"""
    x = np.arange(nb_samples)
    ya, yb = prng.randint(min_value, max_value, size=(2, nb_samples))
    width = 0.25
    ax.bar(x, ya, width)
    ax.bar(x + width, yb, width, color='C2')
    ax.set_xticks(x + width, labels=['a', 'b', 'c', 'd', 'e'])
    return ax


def plot_colored_circles(ax, prng, nb_samples=15):
    """
    绘制圆形补丁。

    注意：绘制固定数量的样本，而不是使用颜色循环的长度，因为不同的样式可能有不同数量的颜色。
    """
    for sty_dict, j in zip(plt.rcParams['axes.prop_cycle'](),
                           range(nb_samples)):
        ax.add_patch(plt.Circle(prng.normal(scale=3, size=2),
                                radius=1.0, color=sty_dict['color']))
    ax.grid(visible=True)

    # 添加标题以启用网格
    plt.title('ax.grid(True)', family='monospace', fontsize='small')

    ax.set_xlim([-4, 8])
    ax.set_ylim([-5, 6])
    ax.set_aspect('equal', adjustable='box')  # 将圆形绘制为圆形
    return ax


def plot_image_and_patch(ax, prng, size=(20, 20)):
    """绘制具有随机值的图像并叠加一个圆形补丁。"""
    values = prng.random_sample(size=size)
    ax.imshow(values, interpolation='none')
    c = plt.Circle((5, 5), radius=5, label='patch')
    ax.add_patch(c)
    # 移除刻度
    ax.set_xticks([])
    ax.set_yticks([])


def plot_histograms(ax, prng, nb_samples=10000):
    """绘制 4 个直方图和一个文本注释。"""
    params = ((10, 10), (4, 12), (50, 12), (6, 55))
    for a, b in params:
        values = prng.beta(a, b, size=nb_samples)
        ax.hist(values, histtype="stepfilled", bins=30,
                alpha=0.8, density=True)

    # 添加一个小注释。
    ax.annotate('注释', xy=(0.25, 4.25),
                xytext=(0.9, 0.9), textcoords=ax.transAxes,
                va="top", ha="right",
                bbox=dict(boxstyle="round", alpha=0.2),
                arrowprops=dict(
                          arrowstyle="->",
                          connectionstyle="angle,angleA=-95,angleB=35,rad=10"),
                )
    return ax
```
