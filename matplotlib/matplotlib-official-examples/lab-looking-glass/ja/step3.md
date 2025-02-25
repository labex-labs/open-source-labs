# グラフと軸の作成

`subplots()` 関数を使って、グラフと軸のオブジェクトを作成します。また、`patches.Circle()` 関数を使って、軸のオブジェクトに黄色い円形のパッチを追加します。

```python
fig, ax = plt.subplots()
circ = patches.Circle((0.5, 0.5), 0.25, alpha=0.8, fc='yellow')
ax.add_patch(circ)
```
