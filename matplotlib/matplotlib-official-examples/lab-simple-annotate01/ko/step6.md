# 주석 사용자 정의

글꼴 크기, 글꼴 색상 및 화살표 스타일을 변경하여 주석을 사용자 정의할 수 있습니다. 다음 코드는 텍스트 주석의 글꼴 크기, 글꼴 색상 및 화살표 스타일을 변경합니다.

```python
ax.annotate("Data Point 1", xy=(1, 3), xytext=(1.5, 3.5),
            arrowprops=dict(facecolor="black", shrink=0.05, arrowstyle="->"),
            fontsize=12, color="red")
```
