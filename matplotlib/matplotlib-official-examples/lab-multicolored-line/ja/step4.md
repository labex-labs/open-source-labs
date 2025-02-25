# 連続ノルムの作成

データポイントから色にマッピングするための連続ノルムを作成します。`matplotlib.pyplot` の `Normalize` 関数を使って、`dydx` の値をその最小値と最大値の間で正規化します。その後、`LineCollection` 関数を使って線分のセットを作成し、それぞれの微分に基づいて個別に色付けします。カラーマッピングに使用する値を設定するために `set_array` 関数を使います。

```python
norm = plt.Normalize(dydx.min(), dydx.max())
lc = LineCollection(segments, cmap='viridis', norm=norm)
lc.set_array(dydx)
lc.set_linewidth(2)
```
