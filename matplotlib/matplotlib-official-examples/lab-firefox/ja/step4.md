# プロットを作成する

ここでは、Matplotlibを使って2つの`PathPatch`オブジェクトをプロットに追加することで、プロットを作成します。1つはオレンジ色で塗りつぶされた形状で、もう1つは白い輪郭になります。

```python
# プロットの範囲を設定する
xmin, ymin = verts.min(axis=0) - 1
xmax, ymax = verts.max(axis=0) + 1

# プロットを作成する
fig = plt.figure(figsize=(5, 5), facecolor="0.75")  # 灰色の背景
ax = fig.add_axes([0, 0, 1, 1], frameon=False, aspect=1,
                  xlim=(xmin, xmax),  # 中央に配置する
                  ylim=(ymax, ymin),  # 中央に配置する、上下逆
                  xticks=[], yticks=[])  # 目盛りなし

# 白い輪郭を追加する
ax.add_patch(patches.PathPatch(path, facecolor='none', edgecolor='w', lw=6))

# オレンジ色の形状を追加する
ax.add_patch(patches.PathPatch(path, facecolor='orange', edgecolor='k', lw=2))

# プロットを表示する
plt.show()
```
