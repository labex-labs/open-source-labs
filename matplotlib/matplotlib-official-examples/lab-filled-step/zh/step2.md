# 定义直方图函数

我们将定义一个函数，用于绘制作为阶梯状补丁的直方图。该函数将接受以下参数：

- `ax`：要绘制到的Axes对象
- `edges`：一个长度为n + 1的数组，给出每个区间的左边缘以及最后一个区间的右边缘
- `values`：一个长度为n的区间计数或值的数组
- `bottoms`：一个浮点数或数组，可选，一个长度为n的数组，表示条形的底部。如果为None，则使用零
- `orientation`：一个字符串，可选，直方图的方向。'v'（默认）表示条形在正y方向上增加

```python
def filled_hist(ax, edges, values, bottoms=None, orientation='v', **kwargs):
    """
    绘制作为阶梯状补丁的直方图。

    参数
    ----------
    ax : Axes
        要绘制到的轴

    edges : 数组
        一个长度为n + 1的数组，给出每个区间的左边缘以及最后一个区间的右边缘。

    values : 数组
        一个长度为n的区间计数或值的数组

    bottoms : 浮点数或数组，可选
        一个长度为n的数组，表示条形的底部。如果为None，则使用零。

    orientation : {'v', 'h'}
        直方图的方向。'v'（默认）表示条形在正y方向上增加。

    **kwargs
        额外的关键字参数将传递给`.fill_between`。

    返回
    -------
    ret : PolyCollection
        添加到Axes的艺术家对象
    """
    if orientation not in 'hv':
        raise ValueError(f"方向必须在{{'h', 'v'}}中，而不是{orientation}")

    kwargs.setdefault('step', 'post')
    kwargs.setdefault('alpha', 0.7)
    edges = np.asarray(edges)
    values = np.asarray(values)
    if len(edges) - 1!= len(values):
        raise ValueError(f'必须提供比值多一个区间边缘，而不是：{len(edges)=} {len(values)=}')

    if bottoms is None:
        bottoms = 0
    bottoms = np.broadcast_to(bottoms, values.shape)

    values = np.append(values, values[-1])
    bottoms = np.append(bottoms, bottoms[-1])
    if orientation == 'h':
        return ax.fill_betweenx(edges, values, bottoms, **kwargs)
    elif orientation == 'v':
        return ax.fill_between(edges, values, bottoms, **kwargs)
    else:
        raise AssertionError("你不应该在这里")
```
