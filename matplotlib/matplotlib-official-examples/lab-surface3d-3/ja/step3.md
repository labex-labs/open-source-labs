# サーフェスプロット用の色を作成する

このステップでは、サーフェスプロット用の色を作成します。メッシュグリッドと同じ形状の空の文字列配列を作成し、チェッカーボード模様で2つの色で埋めます。

```python
# Create colors for the surface plot
colortuple = ('y', 'b')
colors = np.empty(X.shape, dtype=str)
for y in range(ylen):
    for x in range(xlen):
        colors[y, x] = colortuple[(x + y) % len(colortuple)]
```
