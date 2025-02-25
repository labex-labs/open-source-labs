# ユーザ指定の三角分割を描画する

triplot関数を使って、ユーザ指定の三角分割を描画します。

```python
fig2, ax2 = plt.subplots()
ax2.set_aspect('equal')
ax2.triplot(x, y, triangles, 'go-', lw=1.0)
ax2.set_title('Triplot of User-Specified Triangulation')
ax2.set_xlabel('Longitude (degrees)')
ax2.set_ylabel('Latitude (degrees)')
```
