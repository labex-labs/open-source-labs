# 创建一个旋转箭头

在这一步中，我们将创建一个旋转的带锚定方向箭头。这个箭头将旋转30度，并使用衬线字体。

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
