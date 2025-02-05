# 定义误差带

现在我们将定义要在曲线周围绘制的误差带。在本示例中，我们假设误差可以表示为标量*err*，它描述了曲线上每个点垂直方向的不确定性。

```python
def draw_error_band(ax, x, y, err, **kwargs):
    # 通过中心有限差分计算法线（除了第一个点使用前向差分，最后一个点使用后向差分）。
    dx = np.concatenate([[x[1] - x[0]], x[2:] - x[:-2], [x[-1] - x[-2]]])
    dy = np.concatenate([[y[1] - y[0]], y[2:] - y[:-2], [y[-1] - y[-2]]])
    l = np.hypot(dx, dy)
    nx = dy / l
    ny = -dx / l

    # 误差的端点
    xp = x + nx * err
    yp = y + ny * err
    xn = x - nx * err
    yn = y - ny * err

    vertices = np.block([[xp, xn[::-1]],
                         [yp, yn[::-1]]]).T
    codes = np.full(len(vertices), Path.LINETO)
    codes[0] = codes[len(xp)] = Path.MOVETO
    path = Path(vertices, codes)
    ax.add_patch(PathPatch(path, **kwargs))
```
