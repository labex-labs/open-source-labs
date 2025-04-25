# ボクセルプロットの描画

最後に、`ax.voxels`関数を使ってボクセルプロットを描画できます。RGB 値、球体の条件、面の色、辺の色、および線幅を渡します。

```python
ax = plt.figure().add_subplot(projection='3d')
ax.voxels(r, g, b, sphere,
          facecolors=colors,
          edgecolors=np.clip(2*colors - 0.5, 0, 1),  # brighter
          linewidth=0.5)
ax.set(xlabel='r', ylabel='g', zlabel='b')
ax.set_aspect('equal')
plt.show()
```
