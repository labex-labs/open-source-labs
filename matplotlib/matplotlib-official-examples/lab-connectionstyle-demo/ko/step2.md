# 주석 연결 스타일을 생성하기 위한 함수 정의

두 개의 매개변수, 즉 축 객체와 연결 스타일을 입력으로 받는 함수를 정의합니다. 이 함수는 두 개의 데이터 포인트를 플롯하고 지정된 연결 스타일로 주석을 생성합니다.

```python
def demo_con_style(ax, connectionstyle):
    x1, y1 = 0.3, 0.2
    x2, y2 = 0.8, 0.6

    ax.plot([x1, x2], [y1, y2], ".")
    ax.annotate("",
                xy=(x1, y1), xycoords='data',
                xytext=(x2, y2), textcoords='data',
                arrowprops=dict(arrowstyle="->", color="0.5",
                                shrinkA=5, shrinkB=5,
                                patchA=None, patchB=None,
                                connectionstyle=connectionstyle,
                                ),
                )

    ax.text(.05, .95, connectionstyle.replace(",", ",\n"),
            transform=ax.transAxes, ha="left", va="top")
```
