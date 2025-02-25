# `ax.pie` を使ってネストされた円グラフを作成する

`ax.pie` メソッドを使ってネストされた円グラフを作成することができます。まず、3つのグループに対応するいくつかの疑似データを生成します。内側の円では、それぞれの数字を独自のグループに属するものとして扱います。外側の円では、それらを元の3つのグループのメンバーとしてプロットします。

```python
fig, ax = plt.subplots()

size = 0.3
vals = np.array([[60., 32.], [37., 40.], [29., 10.]])

cmap = plt.colormaps["tab20c"]
outer_colors = cmap(np.arange(3)*4)
inner_colors = cmap([1, 2, 5, 6, 9, 10])

ax.pie(vals.sum(axis=1), radius=1, colors=outer_colors,
       wedgeprops=dict(width=size, edgecolor='w'))

ax.pie(vals.flatten(), radius=1-size, colors=inner_colors,
       wedgeprops=dict(width=size, edgecolor='w'))

ax.set(aspect="equal", title='Pie plot with `ax.pie`')
plt.show()
```
