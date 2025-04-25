# 添加一个尺寸条

在数据坐标中绘制一个长度为 0.1 的水平条，并在其下方添加一个固定的标签。

```python
asb = AnchoredSizeBar(ax.transData,
                      0.1,
                      r"1$^{\prime}$",
                      loc='lower center',
                      pad=0.1, borderpad=0.5, sep=5,
                      frameon=False)
ax.add_artist(asb)
```
