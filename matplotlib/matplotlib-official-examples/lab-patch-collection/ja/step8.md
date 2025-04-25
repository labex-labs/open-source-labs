# 色を設定して PatchCollection を作成する

我々は図形の色を設定し、`PatchCollection()` を作成します。

```python
colors = 100 * np.random.rand(len(patches))
p = PatchCollection(patches, alpha=0.4)
p.set_array(colors)
ax.add_collection(p)
fig.colorbar(p, ax=ax)
```
