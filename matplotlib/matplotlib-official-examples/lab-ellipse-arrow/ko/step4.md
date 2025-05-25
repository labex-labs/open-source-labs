# 방향 화살표 반전

방향 화살표를 반전시키려면 마커 유형을 `>`에서 `<`로 변경할 수 있습니다.

```python
# To reverse the orientation arrow, switch the marker type from > to <.
ax.plot(
    vertices[0][0],
    vertices[0][1],
    color="b",
    marker=MarkerStyle("<", "full", t),
    markersize=10
)
```
