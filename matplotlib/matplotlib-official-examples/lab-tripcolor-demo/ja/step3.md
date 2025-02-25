# 疑似カラープロットの作成

次に、`tripcolor()` 関数を使って疑似カラープロットを作成します。異なる陰影付け方法を使って 2 つのプロットを作成します。

```python
# Flat shading plot
fig1, ax1 = plt.subplots()
ax1.set_aspect('equal')
tpc = ax1.tripcolor(triang, z, shading='flat')
fig1.colorbar(tpc)
ax1.set_title('tripcolor of Delaunay triangulation, flat shading')

# Gouraud shading plot
fig2, ax2 = plt.subplots()
ax2.set_aspect('equal')
tpc = ax2.tripcolor(triang, z, shading='gouraud')
fig2.colorbar(tpc)
ax2.set_title('tripcolor of Delaunay triangulation, gouraud shading')
```
