# 定义函数

现在，我们将定义一个名为 `survey` 的函数，它接受 `results` 和 `category_names` 作为参数，并创建一个水平堆叠条形图可视化。

```python
def survey(results, category_names):
    """
    参数
    ----------
    results : dict
        从问题标签到每个类别的答案列表的映射。
        假设所有列表包含相同数量的条目，并且与 *category_names* 的长度匹配。
    category_names : list of str
        类别标签。
    """
    # 将结果和类别转换为 numpy 数组
    labels = list(results.keys())
    data = np.array(list(results.values()))

    # 计算数据的累积和以进行水平堆叠
    data_cum = data.cumsum(axis=1)

    # 定义类别颜色
    category_colors = plt.colormaps['RdYlGn'](
        np.linspace(0.15, 0.85, data.shape[1]))

    # 创建绘图并设置轴属性
    fig, ax = plt.subplots(figsize=(9.2, 5))
    ax.invert_yaxis()
    ax.xaxis.set_visible(False)
    ax.set_xlim(0, np.sum(data, axis=1).max())

    # 创建堆叠条形图并添加条形标签
    for i, (colname, color) in enumerate(zip(category_names, category_colors)):
        widths = data[:, i]
        starts = data_cum[:, i] - widths
        rects = ax.barh(labels, widths, left=starts, height=0.5,
                        label=colname, color=color)
        r, g, b, _ = color
        text_color = 'white' if r * g * b < 0.5 else 'darkgrey'
        ax.bar_label(rects, label_type='center', color=text_color)

    # 添加图例
    ax.legend(ncols=len(category_names), bbox_to_anchor=(0, 1),
              loc='lower left', fontsize='small')

    return fig, ax
```
