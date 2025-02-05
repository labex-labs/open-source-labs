# 定义绘图函数

现在，你需要定义 `plot_figure()` 函数，该函数将使用给定的样式设置并绘制演示图形。此函数将调用步骤 2 中定义的每个绘图函数。

```python
def plot_figure(style_label=""):
    """使用给定的样式设置并绘制演示图形。"""
    # 使用专用的 RandomState 实例来绘制不同图形上相同的“随机”值
    prng = np.random.RandomState(96917002)

    fig, axs = plt.subplots(ncols=6, nrows=1, num=style_label,
                            figsize=(14.8, 2.8), layout='constrained')

    # 制作一个总标题，所有子图使用相同的样式，
    # 除了那些背景较暗的子图，它们使用较浅的颜色：
    background_color = mcolors.rgb_to_hsv(
        mcolors.to_rgb(plt.rcParams['figure.facecolor']))[2]
    if background_color < 0.5:
        title_color = [0.8, 0.8, 1]
    else:
        title_color = np.array([19, 6, 84]) / 256
    fig.suptitle(style_label, x=0.01, ha='left', color=title_color,
                 fontsize=14, fontfamily='DejaVu Sans', fontweight='normal')

    plot_scatter(axs[0], prng)
    plot_image_and_patch(axs[1], prng)
    plot_bar_graphs(axs[2], prng)
    plot_colored_lines(axs[3])
    plot_histograms(axs[4], prng)
    plot_colored_circles(axs[5], prng)

    # 添加分隔线
    rec = Rectangle((1 + 0.025, -2), 0.05, 16,
                    clip_on=False, color='gray')

    axs[4].add_artist(rec)
```
