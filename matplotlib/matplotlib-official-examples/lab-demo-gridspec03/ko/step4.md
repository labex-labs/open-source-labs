# 축 주석 (Annotate Axes)

이 단계에서는 해당 서브플롯 번호로 축에 주석을 추가합니다.

```python
def annotate_axes(fig):
    for i, ax in enumerate(fig.axes):
        ax.text(0.5, 0.5, "ax%d" % (i+1), va="center", ha="center")
        ax.tick_params(labelbottom=False, labelleft=False)

annotate_axes(fig)
```
