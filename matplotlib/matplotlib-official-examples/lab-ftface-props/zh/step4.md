# 打印其他字体属性

在这一步中，我们将打印仅在字体面可缩放时才可用的其他字体属性。

```python
if font.scalable:
    # 字体面的全局边界框 (xmin, ymin, xmax, ymax)
    print('Bbox:               ', font.bbox)
    # EM 所覆盖的字体单位数量
    print('EM:                 ', font.units_per_EM)
    # 以 26.6 个单位表示的上行线高度
    print('Ascender:           ', font.ascender)
    # 以 26.6 个单位表示的下行线高度
    print('Descender:          ', font.descender)
    # 以 26.6 个单位表示的高度
    print('Height:             ', font.height)
    # 最大水平光标前进距离
    print('Max adv width:      ', font.max_advance_width)
    # 垂直布局时同理
    print('Max adv height:     ', font.max_advance_height)
    # 下划线的垂直位置
    print('Underline pos:      ', font.underline_position)
    # 下划线的垂直厚度
    print('Underline thickness:', font.underline_thickness)
```
