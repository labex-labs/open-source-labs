# 회전된 화살표 생성

이 단계에서는 회전된 앵커된 방향 화살표를 생성합니다. 이 화살표는 30 도 회전하며 세리프 폰트를 갖습니다.

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
