# 绘制数据

对于每个子图，我们将绘制x和y数据点，并添加一条线性回归线。我们还将添加一个文本框，其中包含有关数据的一些统计信息。

```python
datasets = {
    'I': (x, y1),
    'II': (x, y2),
    'III': (x, y3),
    'IV': (x4, y4)
}

for ax, (label, (x, y)) in zip(axs.flat, datasets.items()):
    ax.text(0.1, 0.9, label, fontsize=20, transform=ax.transAxes, va='top')
    ax.tick_params(direction='in', top=True, right=True)
    ax.plot(x, y, 'o')

    # 线性回归
    p1, p0 = np.polyfit(x, y, deg=1)  # 斜率，截距
    ax.axline(xy1=(0, p0), slope=p1, color='r', lw=2)

    # 添加统计信息的文本框
    stats = (f'$\\mu$ = {np.mean(y):.2f}\n'
             f'$\\sigma$ = {np.std(y):.2f}\n'
             f'$r$ = {np.corrcoef(x, y)[0][1]:.2f}')
    bbox = dict(boxstyle='round', fc='blanchedalmond', ec='orange', alpha=0.5)
    ax.text(0.95, 0.07, stats, fontsize=9, bbox=bbox,
            transform=ax.transAxes, horizontalalignment='right')

plt.show()
```
