# グラフを作成する

`subplots`を使ってグラフと軸のオブジェクトを作成します。`plot`を使って x と y の値をプロットします。`set_ylim`を使って y 軸の範囲を 0 から始まるように設定します。

```python
fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)
ax.set_ylim(bottom=0)
```
