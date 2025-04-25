# 追加のフォントプロパティを表示する

このステップでは、フェイスが拡大可能な場合にのみ利用可能な追加のフォントプロパティを表示します。

```python
if font.scalable:
    # フェイスのグローバルな境界ボックス (xmin, ymin, xmax, ymax)
    print('Bbox:               ', font.bbox)
    # EM で覆われるフォント単位の数
    print('EM:                 ', font.units_per_EM)
    # 26.6 単位での昇格部
    print('Ascender:           ', font.ascender)
    # 26.6 単位での降格部
    print('Descender:          ', font.descender)
    # 26.6 単位での高さ
    print('Height:             ', font.height)
    # 最大水平カーソル進行量
    print('Max adv width:      ', font.max_advance_width)
    # 垂直レイアウトの場合も同様
    print('Max adv height:     ', font.max_advance_height)
    # 下線の垂直位置
    print('Underline pos:      ', font.underline_position)
    # 下線の垂直太さ
    print('Underline thickness:', font.underline_thickness)
```
