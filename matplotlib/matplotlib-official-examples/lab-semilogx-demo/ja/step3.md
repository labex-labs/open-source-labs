# グラフを作成して x 軸を対数スケールに設定する

`subplots()` メソッドを使ってグラフと軸のオブジェクトを作成します。その後、`semilogx()` メソッドを使って指数関数的減衰関数をプロットし、`set_xscale()` メソッドを使って x 軸を対数スケールに設定します。また、`grid()` メソッドを使ってグラフにグリッドを追加します。

```python
fig, ax = plt.subplots()

ax.semilogx(t, np.exp(-t / 5.0))
ax.set_xscale('log')
ax.grid()
```
