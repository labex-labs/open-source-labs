# グラフの作成

グラフを作成し、そのグラフに `PathPatch` を追加します。グラフのタイトルを `'A Compound Path'` に設定します。

```python
fig, ax = plt.subplots()
ax.add_patch(pathpatch)
ax.set_title('A Compound Path')

ax.autoscale_view()

plt.show()
```
