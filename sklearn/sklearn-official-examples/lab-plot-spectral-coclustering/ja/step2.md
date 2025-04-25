# データセットを生成する

`make_biclusters` 関数を使用して、形状が (300, 300) で、5 つの二部クラスタとノイズが 5 のデータセットを生成します。

```python
data, rows, columns = make_biclusters(shape=(300, 300), n_clusters=5, noise=5, shuffle=False, random_state=0)
```
