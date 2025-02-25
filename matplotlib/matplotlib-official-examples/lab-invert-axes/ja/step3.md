# グラフを作成する

今、Matplotlib を使ってグラフを作成することができます。データを描画するために `plot` 関数を使い、`set_xlim` 関数を使って x 軸の範囲を設定します。

```python
fig, ax = plt.subplots()

ax.plot(t, s)
ax.set_xlim(5, 0)  # decreasing time
ax.set_xlabel('decreasing time (s)')
ax.set_ylabel('voltage (mV)')
ax.set_title('Should be growing...')
ax.grid(True)

plt.show()
```
