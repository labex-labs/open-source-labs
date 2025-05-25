# 삽입 플롯 추가

이 단계에서는 메인 플롯에 삽입 플롯을 추가합니다. 이 삽입 플롯은 메인 플롯의 확대된 영역을 보여줍니다.

```python
# inset axes....
x1, x2, y1, y2 = -1.5, -0.9, -2.5, -1.9  # subregion of the original image
axins = ax.inset_axes(
    [0.5, 0.5, 0.47, 0.47],
    xlim=(x1, x2), ylim=(y1, y2), xticklabels=[], yticklabels=[])
axins.imshow(Z2, extent=extent, origin="lower")
```
