# 축 형식 지정

`format_axes` 함수를 사용하여 모든 서브플롯의 축 형식을 지정합니다. 이 함수는 각 서브플롯에 텍스트 레이블을 추가하고 눈금 레이블을 제거합니다.

```python
def format_axes(fig):
    for i, ax in enumerate(fig.axes):
        ax.text(0.5, 0.5, "ax%d" % (i+1), va="center", ha="center")
        ax.tick_params(labelbottom=False, labelleft=False)

format_axes(fig)
```
