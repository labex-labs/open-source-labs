# 创建子图

现在，我们将使用 `subplots` 函数创建子图。我们将创建一个具有相同纵横比的子图网格，并去除x轴和y轴上的刻度。我们还将在每个子图的中心添加一条垂直线和一条水平线，以帮助直观地显示对齐方式。

```python
axs = fig.subplots(len(va_list), len(ha_list), sharex=True, sharey=True,
                   subplot_kw=dict(aspect=1),
                   gridspec_kw=dict(hspace=0, wspace=0))

for i, va in enumerate(va_list):
    for j, ha in enumerate(ha_list):
        ax = axs[i, j]
        ax.set(xticks=[], yticks=[])
        ax.axvline(0.5, color="skyblue", zorder=0)
        ax.axhline(0.5, color="skyblue", zorder=0)
        ax.plot(0.5, 0.5, color="C0", marker="o", zorder=1)
```
