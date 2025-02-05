# 定义堆叠直方图函数

我们将定义一个函数来创建堆叠直方图。该函数将接受以下参数：

- `ax`：要添加艺术家对象的坐标轴
- `stacked_data`：一个形状为 (M, N) 的数组。将对第一维进行迭代，按行计算直方图
- `sty_cycle`：一个Cycler对象或可操作的字典，应用于每组的样式
- `bottoms`：一个数组，默认值为0，底部的初始位置
- `hist_func`：一个可调用对象，可选。必须具有签名 `bin_vals, bin_edges = f(data)`。预期 `bin_edges` 比 `bin_vals` 长一个
- `labels`：一个字符串列表，可选，每组的标签。如果未给出，且 `stacked_data` 是数组，则默认为 'default set {n}'。如果 `stacked_data` 是映射且 `labels` 为None，则默认为键。如果 `stacked_data` 是映射且给出了 `labels`，则只绘制列出的列
- `plot_func`：一个可调用对象，可选，用于绘制直方图的函数。必须具有签名 `ret = plot_func(ax, edges, top, bottoms=bottoms, label=label, **kwargs)`
- `plot_kwargs`：一个字典，可选，要传递给绘图函数的任何额外关键字参数。这对于绘图函数的所有调用都是相同的，并且将覆盖 `sty_cycle` 中的值

```python
def stack_hist(ax, stacked_data, sty_cycle, bottoms=None, hist_func=None, labels=None, plot_func=None, plot_kwargs=None):
    """
    参数
    ----------
    ax : axes.Axes
        要添加艺术家对象的坐标轴

    stacked_data : 数组或映射
        一个形状为 (M, N) 的数组。将对第一维进行迭代，按行计算直方图

    sty_cycle : Cycler或可操作的字典
        应用于每组的样式

    bottoms : 数组，默认值为0
        底部的初始位置

    hist_func : 可调用对象，可选
        必须具有签名 `bin_vals, bin_edges = f(data)`。
        预期 `bin_edges` 比 `bin_vals` 长一个

    labels : 字符串列表，可选
        每组的标签。

        如果未给出，且 `stacked_data` 是数组，则默认为 'default set {n}'

        如果 *stacked_data* 是映射，且 *labels* 为None，则默认为键。

        如果 *stacked_data* 是映射且 *labels* 为给定，则只绘制列出的列。

    plot_func : 可调用对象，可选
        用于绘制直方图的函数，必须具有签名：

          ret = plot_func(ax, edges, top, bottoms=bottoms,
                          label=label, **kwargs)

    plot_kwargs : 字典，可选
        要传递给绘图函数的任何额外关键字参数。
        这对于绘图函数的所有调用都是相同的，并且将覆盖 *sty_cycle* 中的值。

    返回
    -------
    arts : 字典
        以标签为键的艺术家对象字典
    """
    # 处理默认的装箱函数
    if hist_func is None:
        hist_func = np.histogram

    # 处理默认的绘图函数
    if plot_func is None:
        plot_func = filled_hist

    # 处理默认值
    if plot_kwargs is None:
        plot_kwargs = {}

    try:
        l_keys = stacked_data.keys()
        label_data = True
        if labels is None:
            labels = l_keys

    except AttributeError:
        label_data = False
        if labels is None:
            labels = itertools.repeat(None)

    if label_data:
        loop_iter = enumerate((stacked_data[lab], lab, s) for lab, s in zip(labels, sty_cycle))
    else:
        loop_iter = enumerate(zip(stacked_data, labels, sty_cycle))

    arts = {}
    for j, (data, label, sty) in loop_iter:
        if label is None:
            label = f'dflt set {j}'
        label = sty.pop('label', label)
        vals, edges = hist_func(data)
        if bottoms is None:
            bottoms = np.zeros_like(vals)
        top = bottoms + vals
        sty.update(plot_kwargs)
        ret = plot_func(ax, edges, top, bottoms=bottoms, label=label, **sty)
        bottoms = top
        arts[label] = ret
    ax.legend(fontsize=10)
    return arts
```
