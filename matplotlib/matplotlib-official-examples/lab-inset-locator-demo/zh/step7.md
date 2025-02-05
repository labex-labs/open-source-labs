# 使用二元组边界框创建内嵌图

通过以英寸为单位指定宽度和高度，并使用 `bbox_to_anchor` 参数指定内嵌图的左下角，我们可以创建一个具有二元组边界框的内嵌图。

```python
# 使用二元组边界框创建一个内嵌图。请注意，这会创建一个
# 没有范围的边界框。因此，只有在以绝对单位（英寸）指定
# 宽度和高度时才有意义。
axins2 = inset_axes(ax, width=0.5, height=0.4,
                    bbox_to_anchor=(0.33, 0.25),
                    bbox_transform=ax.transAxes, loc=3, borderpad=0)
```
