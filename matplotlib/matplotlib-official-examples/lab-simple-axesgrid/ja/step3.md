# グリッドを反復処理して画像を描画する

次に、`zip`関数を使って`grid`オブジェクトを反復処理し、軸と画像配列の両方を反復処理します。`imshow`関数を使って各画像を対応する軸に描画します。

```python
for ax, im in zip(grid, [im1, im2, im3, im4]):
    ax.imshow(im)
```
