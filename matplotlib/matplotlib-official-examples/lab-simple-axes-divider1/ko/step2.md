# 헬퍼 함수 정의

축의 중앙에 레이블을 배치하고 축 눈금을 제거하는 데 사용될 헬퍼 함수 `label_axes()`를 정의합니다.

```python
def label_axes(ax, text):
    """Place a label at the center of an Axes, and remove the axis ticks."""
    ax.text(.5, .5, text, transform=ax.transAxes,
            horizontalalignment="center", verticalalignment="center")
    ax.tick_params(bottom=False, labelbottom=False,
                   left=False, labelleft=False)
```
