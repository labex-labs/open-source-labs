# 在坐标轴外部创建内嵌图

我们可以通过使用 `bbox_to_anchor` 参数在坐标轴坐标中指定一个延伸到坐标轴外部的边界框，从而在坐标轴外部创建一个内嵌图。

```python
# 在坐标轴外部创建一个内嵌图
axins = inset_axes(ax, width="100%", height="100%",
                   bbox_to_anchor=(1.05,.6,.5,.4),
                   bbox_transform=ax.transAxes, loc=2, borderpad=0)
```
