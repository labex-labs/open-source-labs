# 使用辅助函数的代码风格

我们将创建一个函数，该函数以数据以及行和列标签作为输入，并允许使用用于自定义绘图的参数。我们将关闭周围的坐标轴边框，并创建一个白色线条的网格来分隔单元格。在这里，我们还希望创建一个颜色条，并将标签放置在热图上方而不是下方。注释应根据阈值使用不同的颜色，以便与像素颜色形成更好的对比度。

```python
def heatmap(data, row_labels, col_labels, ax=None, cbar_kw=None, cbarlabel="", **kwargs):
    """
    从 numpy 数组和两个标签列表创建热图。

    参数
    ----------
    data
        形状为 (M, N) 的二维 numpy 数组。
    row_labels
        长度为 M 的列表或数组，包含行的标签。
    col_labels
        长度为 N 的列表或数组，包含列的标签。
    ax
        绘制热图的 `matplotlib.axes.Axes` 实例。如果未提供，则使用当前坐标轴或创建一个新的。可选。
    cbar_kw
        传递给 `matplotlib.Figure.colorbar` 的参数字典。可选。
    cbarlabel
        颜色条的标签。可选。
    **kwargs
        所有其他参数都将转发给 `imshow`。
    """

    if ax is None:
        ax = plt.gca()

    if cbar_kw is None:
        cbar_kw = {}

    # 绘制热图
    im = ax.imshow(data, **kwargs)

    # 创建颜色条
    cbar = ax.figure.colorbar(im, ax=ax, **cbar_kw)
    cbar.ax.set_ylabel(cbarlabel, rotation=-90, va="bottom")

    # 显示所有刻度并用相应的列表条目为其标注标签。
    ax.set_xticks(np.arange(data.shape[1]), labels=col_labels)
    ax.set_yticks(np.arange(data.shape[0]), labels=row_labels)

    # 让水平坐标轴标签显示在顶部。
    ax.tick_params(top=True, bottom=False, labeltop=True, labelbottom=False)

    # 旋转刻度标签并设置其对齐方式。
    plt.setp(ax.get_xticklabels(), rotation=-30, ha="right", rotation_mode="anchor")

    # 关闭边框并创建白色网格。
    ax.spines[:].set_visible(False)
    ax.set_xticks(np.arange(data.shape[1]+1)-.5, minor=True)
    ax.set_yticks(np.arange(data.shape[0]+1)-.5, minor=True)
    ax.grid(which="minor", color="w", linestyle='-', linewidth=3)
    ax.tick_params(which="minor", bottom=False, left=False)

    return im, cbar


def annotate_heatmap(im, data=None, valfmt="{x:.2f}", textcolors=("black", "white"), threshold=None, **textkw):
    """
    一个用于注释热图的函数。

    参数
    ----------
    im
        要标注的 AxesImage。
    data
        用于注释的数据。如果为 None，则使用图像的数据。可选。
    valfmt
        热图内注释的格式。这应该要么使用字符串格式化方法，例如 "$ {x:.2f}"，要么是一个 `matplotlib.ticker.Formatter`。可选。
    textcolors
        一对颜色。第一个用于低于阈值的值，第二个用于高于阈值的值。可选。
    threshold
        根据该值应用 textcolors 中的颜色的数据单位值。如果为 None（默认），则使用颜色映射的中间值作为分隔。可选。
    **kwargs
        所有其他参数都将转发给每次用于创建文本标签的 `text` 调用。
    """

    if not isinstance(data, (list, np.ndarray)):
        data = im.get_array()

    # 将阈值归一化到图像的颜色范围。
    if threshold is not None:
        threshold = im.norm(threshold)
    else:
        threshold = im.norm(data.max())/2.

    # 将默认对齐方式设置为居中，但允许通过 textkw 覆盖。
    kw = dict(horizontalalignment="center", verticalalignment="center")
    kw.update(textkw)

    # 如果提供的是字符串，则获取格式化器
    if isinstance(valfmt, str):
        valfmt = matplotlib.ticker.StrMethodFormatter(valfmt)

    # 遍历数据并为每个“像素”创建一个 `Text`。
    # 根据数据更改文本的颜色。
    texts = []
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            kw.update(color=textcolors[int(im.norm(data[i, j]) > threshold)])
            text = im.axes.text(j, i, valfmt(data[i, j], None), **kw)
            texts.append(text)

    return texts
```
