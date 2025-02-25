# クイバープロットの作成

`ax.quiver()` 関数を使ってクイバープロットを作成できます。パラメータとして `X`、`Y`、`U`、および `V` 配列を渡します。

```python
fig, ax = plt.subplots()
q = ax.quiver(X, Y, U, V)
```
