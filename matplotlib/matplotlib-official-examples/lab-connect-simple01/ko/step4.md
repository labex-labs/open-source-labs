# 다른 축 사이의 화살표 그리기

데이터 좌표 (data coordinates) 에서 동일한 점이지만 다른 축 사이의 화살표를 그려보겠습니다.

```python
xy = (0.3, 0.2)
con = ConnectionPatch(
    xyA=xy, coordsA=ax2.transData,
    xyB=xy, coordsB=ax1.transData,
    arrowstyle="->", shrinkB=5)
fig.add_artist(con)
```
