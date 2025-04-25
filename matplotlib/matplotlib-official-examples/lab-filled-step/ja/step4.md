# 固定ビンでヒストグラム関数を設定する

`numpy.histogram` を使って固定ビンでヒストグラム関数を設定します。-3 から 3 までの範囲に 20 個のビンを作成します。

```python
edges = np.linspace(-3, 3, 20, endpoint=True)
hist_func = partial(np.histogram, bins=edges)
```
