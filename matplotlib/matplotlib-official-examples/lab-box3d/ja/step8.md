# カラーバーを追加する

`colorbar` メソッドを使ってカラーバーを追加します。カラーバーの位置を調整するために fraction と pad パラメータを設定し、データの名前と単位を表示するためにラベルを設定します。

```python
# Colorbar
fig.colorbar(C, ax=ax, fraction=0.02, pad=0.1, label='Name [units]')
```
