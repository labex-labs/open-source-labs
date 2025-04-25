# グラフを作成してホスト軸を追加する

`plt.figure()`メソッドを使ってグラフを作成し、`fig.add_axes()`メソッドを使ってホスト軸を追加します。ホスト軸は寄生虫軸と x スケールを共有します。

```python
fig = plt.figure()
host = fig.add_axes([0.15, 0.1, 0.65, 0.8], axes_class=HostAxes)
```
