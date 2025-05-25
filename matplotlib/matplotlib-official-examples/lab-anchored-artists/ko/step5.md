# 앵커된 타원 추가

이 단계에서는 앵커된 객체 (Anchored Objects) 를 사용하여 플롯에 타원을 추가합니다.

```python
def draw_ellipse(ax):
    """Draw an ellipse of width=0.1, height=0.15 in data coordinates."""
    aux_tr_box = AuxTransformBox(ax.transData)
    aux_tr_box.add_artist(Ellipse((0, 0), width=0.1, height=0.15))
    box = AnchoredOffsetbox(child=aux_tr_box, loc="lower left", frameon=True)
    ax.add_artist(box)

draw_ellipse(ax)
```
