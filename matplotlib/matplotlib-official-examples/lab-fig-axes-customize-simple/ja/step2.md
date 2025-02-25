# グラフの作成と背景の設定

`plt.figure()` メソッドを使ってグラフを作成します。これにより、`matplotlib.figure.Figure` インスタンスが生成されます。`rect.set_facecolor()` メソッドを使って、グラフの背景色を設定します。

```python
fig = plt.figure()
rect = fig.patch  # a rectangle instance
rect.set_facecolor('lightgoldenrodyellow')
```
