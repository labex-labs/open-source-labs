# 添加颜色条

使用 `inset_axes` 函数向内嵌轴添加颜色条。设置颜色条的宽度、高度、位置和边界框。

```python
cax = inset_axes(axins,
                 width="5%",  # 宽度 = 父边界框宽度的 10%
                 height="100%",  # 高度 : 50%
                 loc='lower left',
                 bbox_to_anchor=(1.05, 0., 1, 1),
                 bbox_transform=axins.transAxes,
                 borderpad=0,
                 )
fig.colorbar(im, cax=cax)
```
