# ボクセルプロットを作成する

最後に、Matplotlib の`Axes3D`クラスの`voxels`関数を使って 3D ボクセルプロットを作成します。

```python
ax = plt.figure().add_subplot(projection='3d')
ax.voxels(x, y, z, filled_2, facecolors=fcolors_2, edgecolors=ecolors_2)
ax.set_aspect('equal')

plt.show()
```
