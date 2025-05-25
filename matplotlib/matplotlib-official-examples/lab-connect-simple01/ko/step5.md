# 다른 점들 사이의 선 그리기

마지막으로, 서로 다른 좌표계 (coordinate systems) 에서 정의된 서로 다른 점들 사이의 선을 그려보겠습니다.

```python
con = ConnectionPatch(
    # in axes coordinates
    xyA=(0.6, 1.0), coordsA=ax2.transAxes,
    # x in axes coordinates, y in data coordinates
    xyB=(0.0, 0.2), coordsB=ax2.get_yaxis_transform(),
    arrowstyle="-")
ax2.add_artist(con)
```
