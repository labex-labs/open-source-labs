# 3D ボクセルプロットの作成

ここでは、`ax.voxels` 関数を使って 3D ボクセルプロットを作成します。パラメータとして `x`、`y`、`z`、および `sphere` を渡します。また、先ほど定義した `colors` 配列を使って `facecolors` と `edgecolors` を追加します。

```python
ax = plt.figure().add_subplot(projection='3d')
ax.voxels(x, y, z, sphere,
          facecolors=colors,
          edgecolors=np.clip(2*colors - 0.5, 0, 1),  # brighter
          linewidth=0.5)
```
