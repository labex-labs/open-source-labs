# 타원에 연결되도록 화살표 사용자 정의

이 단계에서는 타원에 연결되도록 화살표를 사용자 정의합니다. `arrowprops` 매개변수를 사용하여 화살표가 타원에 연결되도록 지정하고, 화살표 스타일과 색상도 사용자 정의합니다.

```python
ax = axs.flat[2]
ax.plot([x1, x2], [y1, y2], ".")
el = mpatches.Ellipse((x1, y1), 0.3, 0.4, angle=30, alpha=0.2)
ax.add_artist(el)
ax.annotate("",
            xy=(x1, y1), xycoords='data',
            xytext=(x2, y2), textcoords='data',
            arrowprops=dict(arrowstyle="-",
                            color="0.5",
                            patchB=el,
                            connectionstyle="arc3,rad=0.3",
                            ),
            )
```
