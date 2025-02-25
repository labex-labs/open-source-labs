# 回転させた矢印を作成する

このステップでは、回転させた固定方向矢印を作成します。この矢印は30度回転させ、明朝体のフォントを持ちます。

```python
fontprops = fm.FontProperties(family='serif')

rotated_arrow = AnchoredDirectionArrows(
                    ax.transAxes,
                    '30', '120',
                    loc='center',
                    color='w',
                    angle=30,
                    fontproperties=fontprops
                    )
ax.add_artist(rotated_arrow)
```
