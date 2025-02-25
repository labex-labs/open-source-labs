# グラフを作成する

データがあるので、グラフを作成できます。まず、`plt.subplots()` を使ってグラフと軸のオブジェクトを作成します。その後、`ax.plot()` を使ってデータをプロットします。

```python
fig, ax = plt.subplots()
ax.plot(t, s)
```
