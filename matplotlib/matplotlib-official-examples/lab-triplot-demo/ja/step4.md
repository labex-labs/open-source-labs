# デロネ三角分割を描画する

triplot 関数を使って三角分割を描画します。

```python
fig1, ax1 = plt.subplots()
ax1.set_aspect('equal')
ax1.triplot(triang, 'bo-', lw=1)
ax1.set_title('Triplot of Delaunay Triangulation')
```
