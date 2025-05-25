# 앵커된 텍스트 추가

이 단계에서는 figure 의 왼쪽 상단 모서리에 앵커된 텍스트 상자를 추가합니다.

```python
def draw_text(ax):
    """Draw a text-box anchored to the upper-left corner of the figure."""
    box = AnchoredOffsetbox(child=TextArea("Figure 1a"),
                            loc="upper left", frameon=True)
    box.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
    ax.add_artist(box)

draw_text(ax)
```
