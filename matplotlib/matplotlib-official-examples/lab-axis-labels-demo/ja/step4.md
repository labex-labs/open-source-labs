# カラーバーラベルの位置を設定する

`colorbar` メソッドと `set_label` メソッドを使用して、カラーバーラベルの位置を設定することができます。位置を `'top'`、`'bottom'`、`'left'`、または `'right'` に設定できます。この例では、位置を `'top'` に設定します。

```python
cbar = fig.colorbar(sc)
cbar.set_label("ZLabel", loc='top')
```
