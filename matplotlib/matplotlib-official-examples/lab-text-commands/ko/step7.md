# 플롯에 주석 추가

`ax.annotate()` 함수를 사용하여 플롯에 주석 (annotation) 을 추가할 수 있습니다. 이 함수는 세 개의 인수를 받습니다: 주석 텍스트, 주석을 달 지점의 xy 좌표, 그리고 텍스트 위치의 xy 좌표입니다. `arrowprops` 인수를 사용하여 주석 스타일을 사용자 정의할 수 있습니다.

```python
ax.annotate('annotate', xy=(2, 1), xytext=(3, 4),
            arrowprops=dict(facecolor='black', shrink=0.05))
```
