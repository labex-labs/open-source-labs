# ボクセル配列をプロットする

最後に、`Axes3D.voxels` 関数を使用して、指定された色でボクセル配列をプロットできます。

```python
ax = plt.figure().add_subplot(projection='3d')
ax.voxels(voxelarray, facecolors=colors, edgecolor='k')

plt.show()
```
