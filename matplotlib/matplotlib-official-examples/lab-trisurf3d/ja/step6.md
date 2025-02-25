# 3D曲面を作成する

`plot_trisurf`関数を使って3D曲面を作成します。

```python
ax = plt.figure().add_subplot(projection='3d')
ax.plot_trisurf(x, y, z, linewidth=0.2, antialiased=True)

plt.show()
```
