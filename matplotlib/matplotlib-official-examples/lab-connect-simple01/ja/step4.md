# 異なる軸間に矢印を描画する

データ座標における同じ点の間に、異なる軸間に矢印を描画しましょう。

```python
xy = (0.3, 0.2)
con = ConnectionPatch(
    xyA=xy, coordsA=ax2.transData,
    xyB=xy, coordsB=ax1.transData,
    arrowstyle="->", shrinkB=5)
fig.add_artist(con)
```
