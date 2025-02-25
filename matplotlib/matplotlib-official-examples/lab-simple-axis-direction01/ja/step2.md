# グラフと軸の作成

次に、`plt.subplots()` 関数を使ってグラフと軸のオブジェクトを作成します。`figsize` パラメータを使ってグラフのサイズを指定します。

```python
fig = plt.figure(figsize=(4, 2.5))
ax1 = fig.add_subplot(axes_class=axisartist.Axes)
```
