# 단위화된 xy 및 텍스트를 사용한 화살표 주석 추가

이 단계에서는 `annotate()` 함수를 사용하여 플롯에 화살표 주석을 추가합니다. 화살표의 위치, 표시할 텍스트 및 화살표 속성을 제공합니다. 또한 위치 및 텍스트에 대한 측정 단위를 지정합니다.

```python
ax.annotate('local max', xy=(3*cm, 1*cm), xycoords='data',
            xytext=(0.8*cm, 0.95*cm), textcoords='data',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='right', verticalalignment='top')
```
