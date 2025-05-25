# 화살표로 두 점 연결

이 단계에서는 화살표로 두 점을 연결합니다. `annotate` 함수를 사용하여 화살표를 생성하고, 화살표 스타일과 색상을 사용자 정의합니다.

```python
ax = axs.flat[0]
ax.plot([x1, x2], [y1, y2], ".")
ax.annotate("",
            xy=(x1, y1), xycoords='data',
            xytext=(x2, y2), textcoords='data',
            arrowprops=dict(arrowstyle="-",
                            color="0.5",
                            connectionstyle="arc3,rad=0.3",
                            ),
            )
```
