# 주석 위치 지정

다양한 좌표계 (coordinate systems) 를 사용하여 주석의 위치를 지정할 수 있습니다. 다음 코드는 데이터 좌표 (data coordinates) 를 사용하여 텍스트 주석을 배치하고, 그림 좌표 (figure coordinates) 를 사용하여 화살표 주석을 배치합니다.

```python
ax.annotate("Data Point 1", xy=(1, 3), xytext=(1.5, 3.5),
            arrowprops=dict(facecolor="black", shrink=0.05),
            xycoords="data", textcoords="data")
ax.annotate("", xy=(1, 3), xytext=(0.5, 0.5),
            arrowprops=dict(facecolor="black", shrink=0.05),
            xycoords="data", textcoords="figure fraction")
```
