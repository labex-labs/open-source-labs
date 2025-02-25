# グラフを作成する

`subplots`を使ってグラフと軸のオブジェクトを作成します。`plot`を使ってxとyの値をプロットします。`set_ylim`を使ってy軸の範囲を0から始まるように設定します。

```python
fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)
ax.set_ylim(bottom=0)
```
