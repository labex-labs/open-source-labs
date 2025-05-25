# 타원에 맞춰 화살표 축소 사용자 정의

이 단계에서는 타원에 맞춰 화살표를 축소하도록 사용자 정의합니다. `shrinkB` 매개변수를 사용하여 화살표가 타원을 향해 축소되어야 하는 양을 지정합니다.

```python
ax = axs.flat[3]
ax.plot([x1, x2], [y1, y2], ".")
el = mpatches.Ellipse((x1, y1), 0.3, 0.4, angle=30, alpha=0.2)
ax.add_artist(el)
ax.annotate("",
            xy=(x1, y1), xycoords='data',
            xytext=(x2, y2), textcoords='data',
            arrowprops=dict(arrowstyle="fancy",
                            color="0.5",
                            patchB=el,
                            shrinkB=5,
                            connectionstyle="arc3,rad=0.3",
                            ),
            )
```
