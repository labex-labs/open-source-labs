# ボクセルプロットを作成する

最後に、Matplotlibの`Axes3D`クラスの`voxels`関数を使って3Dボクセルプロットを作成します。

```python
ax = plt.figure().add_subplot(projection='3d')
ax.voxels(x, y, z, filled_2, facecolors=fcolors_2, edgecolors=ecolors_2)
ax.set_aspect('equal')

plt.show()
```
