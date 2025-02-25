# Создаем повернутую стрелку

В этом шаге мы создадим направленную стрелку с привязкой, которая будет повернута. Эта стрелка будет повернута на 30 градусов и будет иметь шрифт с засечками.

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
