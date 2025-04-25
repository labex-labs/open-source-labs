# 创建具有任意位置的内嵌图

我们可以通过使用 `bbox_to_anchor` 参数在数据坐标中指定一个边界框，并使用 `bbox_transform` 参数指定边界框的变换，来创建具有任意位置的内嵌图。

```python
# 使用 ax.transData 作为变换在数据坐标中创建内嵌图
axins3 = inset_axes(ax2, width="100%", height="100%",
                    bbox_to_anchor=(1e-2, 2, 1e3, 3),
                    bbox_transform=ax2.transData, loc=2, borderpad=0)
```
