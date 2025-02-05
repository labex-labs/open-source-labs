# 创建误差框函数

现在我们将创建一个名为 `make_error_boxes` 的函数，该函数将创建一个由x和y方向上的误差线限制定义的矩形补丁。

```python
def make_error_boxes(ax, xdata, ydata, xerror, yerror, facecolor='r',
                     edgecolor='none', alpha=0.5):

    # 遍历数据点；根据每个点的误差创建框
    errorboxes = [Rectangle((x - xe[0], y - ye[0]), xe.sum(), ye.sum())
                  for x, y, xe, ye in zip(xdata, ydata, xerror.T, yerror.T)]

    # 使用指定的颜色/透明度创建补丁集合
    pc = PatchCollection(errorboxes, facecolor=facecolor, alpha=alpha,
                         edgecolor=edgecolor)

    # 将集合添加到坐标轴
    ax.add_collection(pc)

    # 绘制误差线
    artists = ax.errorbar(xdata, ydata, xerr=xerror, yerr=yerror,
                          fmt='none', ecolor='k')

    return artists
```
