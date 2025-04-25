# 座標フォーマッタを変更する

次に、座標フォーマッタを変更して、与えられた x と y に対して最も近いピクセルの画像「z」値を報告します。これは、`~.axes.Axes.format_coord` 関数をカスタマイズすることで達成できます。

```python
def format_coord(x, y):
    col = round(x)
    row = round(y)
    nrows, ncols = X.shape
    if 0 <= col < ncols and 0 <= row < nrows:
        z = X[row, col]
        return f'x={x:1.4f}, y={y:1.4f}, z={z:1.4f}'
    else:
        return f'x={x:1.4f}, y={y:1.4f}'

ax.format_coord = format_coord
```
