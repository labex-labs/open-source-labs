# 축 주석 (Annotate Axes)

축에 주석을 추가하려면, figure 의 축을 반복하고 `text` 함수와 `tick_params` 함수를 사용하여 텍스트를 추가하여 눈금 레이블을 제거할 수 있습니다.

```python
def annotate_axes(fig):
    for i, ax in enumerate(fig.axes):
        ax.text(0.5, 0.5, "ax%d" % (i+1), va="center", ha="center")
        ax.tick_params(labelbottom=False, labelleft=False)
```
