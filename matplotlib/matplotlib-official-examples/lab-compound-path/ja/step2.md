# 頂点とコードの作成

複合パスに結合したい 2 つの多角形の頂点とコードを作成します。多角形の始点にカーソルを移動するには `Path.MOVETO`、始点から次の点までの線を作成するには `Path.LINETO`、多角形を閉じるには `Path.CLOSEPOLY` を使用します。

```python
vertices = []
codes = []

# 最初の多角形 - 四角形
codes = [Path.MOVETO] + [Path.LINETO]*3 + [Path.CLOSEPOLY]
vertices = [(1, 1), (1, 2), (2, 2), (2, 1), (0, 0)]

# 2 番目の多角形 - 三角形
codes += [Path.MOVETO] + [Path.LINETO]*2 + [Path.CLOSEPOLY]
vertices += [(4, 4), (5, 5), (5, 4), (0, 0)]
```
