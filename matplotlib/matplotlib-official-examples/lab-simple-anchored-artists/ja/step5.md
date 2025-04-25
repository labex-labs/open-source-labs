# サイズバーの追加

データ座標において長さ 0.1 の水平バーを描画し、その下に固定ラベルを付けます。

```python
asb = AnchoredSizeBar(ax.transData,
                      0.1,
                      r"1$^{\prime}$",
                      loc='lower center',
                      pad=0.1, borderpad=0.5, sep=5,
                      frameon=False)
ax.add_artist(asb)
```
