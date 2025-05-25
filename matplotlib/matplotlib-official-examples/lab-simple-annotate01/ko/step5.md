# 도형 주석 추가

이제 플롯에 도형 주석을 추가합니다. 다음 코드는 두 번째 데이터 포인트 주위에 사각형을 추가합니다.

```python
bbox = dict(boxstyle="round", fc="0.8")
ax.annotate("Data Point 2", xy=(2, 4), xytext=(2.5, 4.5),
            bbox=bbox,
            arrowprops=dict(facecolor="black", shrink=0.05))
```
