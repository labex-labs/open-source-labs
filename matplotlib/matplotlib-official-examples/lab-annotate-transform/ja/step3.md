# グラフの作成

次に、`matplotlib.pyplot` ライブラリを使ってグラフを作成します。グラフの x 軸と y 軸の範囲を設定した後、データを描画します。

```python
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlim(0, 10)
ax.set_ylim(-1, 1)
```
