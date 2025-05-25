# hatches_plot 함수 생성

`hatches_plot` 함수는 지정된 해칭 패턴 (hatching pattern) 을 가진 사각형을 생성하고 이를 축에 추가합니다. 또한 해칭 패턴과 함께 텍스트를 추가합니다.

```python
def hatches_plot(ax, h):
    ax.add_patch(Rectangle((0, 0), 2, 2, fill=False, hatch=h))
    ax.text(1, -0.5, f"' {h} '", size=15, ha="center")
    ax.axis('equal')
    ax.axis('off')
```
