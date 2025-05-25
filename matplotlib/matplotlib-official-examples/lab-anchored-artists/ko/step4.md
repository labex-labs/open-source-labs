# 앵커된 원 추가

이 단계에서는 앵커된 객체 (Anchored Objects) 를 사용하여 플롯에 두 개의 원을 추가합니다.

```python
def draw_circles(ax):
    """Draw circles in axes coordinates."""
    area = DrawingArea(width=40, height=20)
    area.add_artist(Circle((10, 10), 10, fc="tab:blue"))
    area.add_artist(Circle((30, 10), 5, fc="tab:red"))
    box = AnchoredOffsetbox(
        child=area, loc="upper right", pad=0, frameon=False)
    ax.add_artist(box)

draw_circles(ax)
```
