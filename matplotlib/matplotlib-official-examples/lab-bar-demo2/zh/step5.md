# 使用标量或单位设置 x 轴范围

在这一步中，我们将使用标量或单位来设置 x 轴范围。我们将使用 `set_xlim` 方法来设置 x 轴范围。对于第二行第一列的柱状图，我们将使用当前单位的标量把 x 轴范围设置为 2 和 6。对于第二行第二列的柱状图，我们将使用单位把 x 轴范围设置为 2 厘米和 6 厘米。

```python
axs[1, 0].bar(cms, cms, bottom=bottom, width=width, xunits=inch, yunits=cm)
axs[1, 0].set_xlim(2, 6)

axs[1, 1].bar(cms, cms, bottom=bottom, width=width, xunits=inch, yunits=inch)
axs[1, 1].set_xlim(2 * cm, 6 * cm)
```
