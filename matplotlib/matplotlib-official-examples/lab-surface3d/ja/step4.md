# 曲面を描画する

```python
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
```

`plot_surface()` 関数を使って曲面を描画します。曲面に coolwarm カラーマップで色を付けるために、`X`、`Y`、`Z` の値とともに、`cmap` パラメータを `cm.coolwarm` に設定して渡します。ワイヤーフレームを削除するために `linewidth=0` も設定し、曲面を不透明にするために `antialiased=False` も設定します。
