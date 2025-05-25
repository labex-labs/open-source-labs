# 텍스트 주석 추가

이제 플롯에 텍스트 주석을 추가합니다. 다음 코드는 첫 번째 데이터 포인트에 "Data Point 1" 텍스트를 추가합니다.

```python
ax.annotate("Data Point 1", xy=(1, 3), xytext=(1.5, 3.5),
            arrowprops=dict(facecolor="black", shrink=0.05))
```
