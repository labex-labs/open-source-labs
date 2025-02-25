# 境界ノルムを使用する

代わりに境界ノルムを使用して線分を色付けします。赤色、緑色、青色の 3 色を含む `ListedColormap` を作成します。その後、境界値 -1、-0.5、0.5、および 1 と `ListedColormap` を持つ `BoundaryNorm` を作成します。カラーマッピングに使用する値を設定するために `set_array` 関数を使います。

```python
cmap = ListedColormap(['r', 'g', 'b'])
norm = BoundaryNorm([-1, -0.5, 0.5, 1], cmap.N)
lc = LineCollection(segments, cmap=cmap, norm=norm)
lc.set_array(dydx)
lc.set_linewidth(2)
```
